param(
  [string]$ServerHost = "109.73.207.66",
  [string]$ServerUser = "kb",
  [string]$ServerKey = "",
  [string]$RemoteRoot = "/srv/kb",

  [int]$Keep = 5,
  [string]$Rollback = "",

  [switch]$Build,
  [switch]$DryRun
)

# Deploys the static viewer (app/) to the knowledge-base site next to Foundry VTT.
# Server layout: $RemoteRoot/releases/<release-id>/ and the $RemoteRoot/current
# symlink that nginx serves. The kb user owns only /srv/kb; it has no sudo and no
# access to /home/foundry. nginx site: /etc/nginx/sites-available/kb.
#
#   .\tools\deploy_kb.ps1 -Build              # rebuild app/kb.html, upload, switch current
#   .\tools\deploy_kb.ps1 -DryRun             # show what would happen
#   .\tools\deploy_kb.ps1 -Rollback list      # list releases on the server
#   .\tools\deploy_kb.ps1 -Rollback <id>      # point current at an older release

$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$appPath = Join-Path $repoRoot "app"

function Resolve-ServerKey {
  $candidates = @(
    $ServerKey,
    $env:KB_SERVER_KEY_PATH,
    (Join-Path $repoRoot "..\NRI\.ssh\kb_deploy"),
    (Join-Path $HOME ".ssh\kb_deploy")
  )
  foreach ($path in $candidates) {
    if (-not [string]::IsNullOrWhiteSpace($path) -and (Test-Path $path)) {
      return (Resolve-Path $path).Path
    }
  }
  throw "SSH key for user kb not found. Pass -ServerKey <path> or set KB_SERVER_KEY_PATH."
}

$key = Resolve-ServerKey
$sshTarget = "$ServerUser@$ServerHost"
$sshOptions = @("-i", $key, "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=accept-new")

function Invoke-Remote {
  param([string]$Command)

  $commandBase64 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($Command))
  ssh @sshOptions $sshTarget "printf '%s' '$commandBase64' | base64 -d | bash"
  if ($LASTEXITCODE -ne 0) {
    throw "Remote command failed with exit code $LASTEXITCODE."
  }
}

if ($Rollback) {
  if ($Rollback -eq "list") {
    Invoke-Remote "ls -1 '$RemoteRoot/releases'; echo; echo current: `$(readlink '$RemoteRoot/current')"
    return
  }
  if ($Rollback -notmatch '^[0-9A-Za-z._-]+$') {
    throw "Invalid release id: $Rollback"
  }
  if ($DryRun) {
    Write-Host "[dry-run] Would point $RemoteRoot/current at releases/$Rollback"
    return
  }
  Invoke-Remote @"
set -e
cd '$RemoteRoot'
test -d 'releases/$Rollback'
ln -sfn 'releases/$Rollback' current.tmp && mv -T current.tmp current
echo current: `$(readlink current)
"@
  return
}

if ($Build) {
  python (Join-Path $repoRoot "tools\build_viewer.py")
  if ($LASTEXITCODE -ne 0) {
    throw "build_viewer.py failed."
  }
}

foreach ($file in @("index.html", "kb.html")) {
  if (-not (Test-Path (Join-Path $appPath $file))) {
    throw "Missing app\$file. Run with -Build."
  }
}

$commit = (git -C $repoRoot rev-parse --short HEAD 2>$null)
$releaseId = (Get-Date -Format "yyyyMMdd-HHmmss") + $(if ($commit) { "-$commit" } else { "" })
$archivePath = Join-Path ([IO.Path]::GetTempPath()) "kb-$releaseId.tgz"
$remoteArchive = "$RemoteRoot/releases/$releaseId.tgz"

if ($DryRun) {
  Write-Host "[dry-run] Would pack $appPath and upload it to ${sshTarget}:$remoteArchive"
  Write-Host "[dry-run] Would unpack to $RemoteRoot/releases/$releaseId, switch current, keep $Keep releases"
  return
}

tar -czf $archivePath -C $appPath .
if ($LASTEXITCODE -ne 0) {
  throw "tar failed."
}

try {
  scp @sshOptions $archivePath "${sshTarget}:$remoteArchive"
  if ($LASTEXITCODE -ne 0) {
    throw "scp failed with exit code $LASTEXITCODE."
  }

  Invoke-Remote @"
set -e
cd '$RemoteRoot/releases'
mkdir '$releaseId'
tar -xzf '$releaseId.tgz' -C '$releaseId'
rm -f '$releaseId.tgz'
chmod -R a+rX '$releaseId'
cd '$RemoteRoot'
ln -sfn 'releases/$releaseId' current.tmp && mv -T current.tmp current
ls -1dt releases/*/ | tail -n +$($Keep + 1) | xargs -r rm -rf
echo current: `$(readlink current)
ls -1 releases
"@
} finally {
  Remove-Item -LiteralPath $archivePath -Force -ErrorAction SilentlyContinue
}

Write-Host "Deployed release $releaseId to $ServerHost`:$RemoteRoot/current"
