<#
.SYNOPSIS
  Run MinerU (CPU pipeline profile) on page ranges of one book and record the run.

.DESCRIPTION
  Layout (decision R-16): <DataRoot>\<BookId>\source.json and
  <DataRoot>\<BookId>\runs\<run-id>\{run.json, mineru.log, output\, runtime\}.
  Each page range is a separate MinerU invocation inside the same run folder
  (output\pNNN-MMM). Models are used offline; nothing is downloaded.

.EXAMPLE
  .\run_mineru.ps1 -Pdf 'C:\books\keeper.pdf' -BookId keeper-rulebook-ru -Ranges '363-395','7-10'
#>
param(
  [Parameter(Mandatory)] [string]   $Pdf,
  [Parameter(Mandatory)] [string]   $BookId,
  [Parameter(Mandatory)] [string[]] $Ranges,            # physical 1-based pages, e.g. '363-395'
  [string] $Method   = 'ocr',                           # ocr | txt | auto
  [string] $Lang     = 'east_slavic',
  [string] $DataRoot = 'C:\_Hobby\_work\NRI\Mineru_tmp',
  [string] $ToolRoot = 'C:\_Hobby\_work\NRI\.tools\MinerU',
  [string] $Profile  = 'pipeline-cpu-v1',
  [string] $Purpose  = ''
)
$ErrorActionPreference = 'Stop'

$mineru = Join-Path $ToolRoot "profiles\$Profile\.venv\Scripts\mineru.exe"
$config = Join-Path $ToolRoot "runtime\$Profile\mineru.json"
foreach ($p in @($Pdf, $mineru, $config)) { if (-not (Test-Path -LiteralPath $p)) { throw "missing: $p" } }

$bookDir = Join-Path $DataRoot $BookId
New-Item -ItemType Directory -Force $bookDir | Out-Null
$pdfItem = Get-Item -LiteralPath $Pdf
$sha = (Get-FileHash -Algorithm SHA256 -LiteralPath $Pdf).Hash
$sourceFile = Join-Path $bookDir 'source.json'
if (Test-Path $sourceFile) {
  $known = Get-Content $sourceFile -Raw | ConvertFrom-Json
  if ($known.sha256 -ne $sha) { throw "PDF hash differs from $sourceFile ($($known.sha256) vs $sha)" }
} else {
  [ordered]@{ book_id = $BookId; file_name = $pdfItem.Name; local_path = $pdfItem.FullName; size_bytes = $pdfItem.Length; sha256 = $sha } |
    ConvertTo-Json | Set-Content -Encoding utf8NoBOM $sourceFile
}

$rangeTag = ($Ranges -join '_') -replace '[^0-9_\-]', ''
$runId = '{0}_pipeline-{1}-{2}_p{3}' -f (Get-Date -Format 'yyyy-MM-dd-HHmm'), $Method, ($Lang -replace '_', ''), $rangeTag
$runDir = Join-Path $bookDir "runs\$runId"
$runtime = Join-Path $runDir 'runtime'
New-Item -ItemType Directory -Force (Join-Path $runDir 'output'), (Join-Path $runtime 'tmp') | Out-Null

$env:MINERU_TOOLS_CONFIG_JSON = $config
$env:MINERU_DEVICE_MODE = 'cpu'
$env:MINERU_PROCESSING_WINDOW_SIZE = '1'
$env:HF_HUB_OFFLINE = '1'
$env:HF_HOME = Join-Path $runtime 'hf'
$env:MODELSCOPE_CACHE = Join-Path $runtime 'modelscope'
$env:TEMP = Join-Path $runtime 'tmp'
$env:TMP = $env:TEMP
$env:NO_PROXY = '*'

$version = (& $mineru --version 2>&1 | Out-String).Trim()
$record = [ordered]@{
  run_id = $runId; purpose = $Purpose; mineru_version = $version; profile = $Profile
  backend = 'pipeline'; method = $Method; lang = $Lang; formula = $false; table = $true
  source_sha256 = $sha; started_at = (Get-Date).ToString('o'); ranges = @()
}
$log = Join-Path $runDir 'mineru.log'
foreach ($r in $Ranges) {
  $a, $b = $r -split '-'
  if (-not $b) { $b = $a }
  $out = Join-Path $runDir ("output\p{0:d3}-{1:d3}" -f [int]$a, [int]$b)
  New-Item -ItemType Directory -Force $out | Out-Null
  $sw = [Diagnostics.Stopwatch]::StartNew()
  "=== range $r (physical) ===" | Add-Content -Encoding utf8 $log
  & $mineru -p $Pdf -o $out -b pipeline -m $Method -l $Lang -s ([int]$a - 1) -e ([int]$b - 1) -f False -t True *>> $log
  $record.ranges += [ordered]@{ pages = $r; output = (Split-Path $out -Leaf); exit_code = $LASTEXITCODE; seconds = [int]$sw.Elapsed.TotalSeconds }
  $record | ConvertTo-Json -Depth 4 | Set-Content -Encoding utf8NoBOM (Join-Path $runDir 'run.json')
}
$record.finished_at = (Get-Date).ToString('o')
$record | ConvertTo-Json -Depth 4 | Set-Content -Encoding utf8NoBOM (Join-Path $runDir 'run.json')
"run: $runDir"
$record.ranges | ForEach-Object { "{0}: exit={1} {2}s" -f $_.pages, $_.exit_code, $_.seconds }
