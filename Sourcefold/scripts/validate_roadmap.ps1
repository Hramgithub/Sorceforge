<#
.SYNOPSIS
Runs the package-backed Sourcefold roadmap validator.
#>

[CmdletBinding()]
param(
    [string]$RoadmapPath,
    [switch]$Quiet
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $PSCommandPath
$projectRoot = (Resolve-Path (Join-Path $scriptDir "..")).Path

$arguments = @("run", "--silent", "validate:roadmap", "--")
if ($RoadmapPath) {
    $arguments += @("--file", $RoadmapPath)
}
if ($Quiet) {
    $arguments += "--quiet"
}

Push-Location $projectRoot
try {
    & npm @arguments
    if ($LASTEXITCODE -ne 0) {
        exit $LASTEXITCODE
    }
}
finally {
    Pop-Location
}
