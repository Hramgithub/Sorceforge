<#
.SYNOPSIS
Creates a Sourcefold documentation/status checkpoint.

.DESCRIPTION
Dry-run is the default. Use -Apply to append checkpoint evidence to the
project rollup, the selected goal plan/context, and roadmap.yaml.
#>

[CmdletBinding(PositionalBinding = $false)]
param(
    [string]$GoalId,
    [string]$Summary,
    [string[]]$Completed = @(),
    [string[]]$Next = @(),
    [string[]]$Blockers = @(),
    [string[]]$RoadmapNode = @(),
    [string[]]$Decision = @(),
    [ValidateSet("documentation", "status", "roadmap", "release", "general")]
    [string]$CheckpointType = "documentation",
    [switch]$SkipRoadmapValidation,
    [switch]$Apply
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-ProjectRoot {
    $scriptDir = Split-Path -Parent $PSCommandPath
    return (Resolve-Path (Join-Path $scriptDir "..")).Path
}

function Get-CheckpointTimestamp {
    return (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
}

function Get-CheckpointId([string]$timestamp) {
    return "doc-checkpoint-" + ($timestamp -replace "[-:]", "" -replace "Z$", "Z")
}

function Invoke-RoadmapValidation([string]$projectRoot) {
    if ($SkipRoadmapValidation) { return }
    $validator = Join-Path $projectRoot "scripts\validate_roadmap.ps1"
    if (-not (Test-Path -LiteralPath $validator)) {
        throw "Roadmap validator not found: $validator"
    }
    & $validator -Quiet
    if ($LASTEXITCODE -ne 0) {
        throw "Roadmap validation failed. Run scripts\validate_roadmap.ps1 for details."
    }
}

function ConvertTo-YamlScalar([string]$value) {
    if ($null -eq $value) { return '""' }
    $escaped = $value.Replace("\", "\\").Replace('"', '\"')
    return '"' + $escaped + '"'
}

function ConvertTo-YamlInlineList([string[]]$items) {
    if (-not $items -or $items.Count -eq 0) { return "[]" }
    return "[" + (($items | ForEach-Object { ConvertTo-YamlScalar $_ }) -join ", ") + "]"
}

function Format-MarkdownList([string[]]$items, [string]$emptyText) {
    if (-not $items -or $items.Count -eq 0) { return "- $emptyText" }
    return (($items | ForEach-Object { "- $_" }) -join [Environment]::NewLine)
}

function Add-TextIfMissing([string]$path, [string]$text) {
    $content = Get-Content -Raw -LiteralPath $path
    if (-not $content.EndsWith([Environment]::NewLine)) {
        $content += [Environment]::NewLine
    }
    Set-Content -LiteralPath $path -Value ($content + $text) -Encoding UTF8
}

function Resolve-GoalId([string]$projectRoot, [string]$requestedGoalId) {
    $plansRoot = Join-Path $projectRoot "docs\plans"
    if ($requestedGoalId) {
        $goalPath = Join-Path $plansRoot $requestedGoalId
        if (-not (Test-Path -LiteralPath $goalPath)) {
            throw "Goal directory not found: $goalPath"
        }
        return [pscustomobject]@{
            Id = $requestedGoalId
            Path = $goalPath
            Inferred = $false
        }
    }

    $candidate = Get-ChildItem -LiteralPath $plansRoot -Directory |
        Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName "plan.md") } |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1

    if (-not $candidate) {
        throw "No goal plan directories found under $plansRoot"
    }

    return [pscustomobject]@{
        Id = $candidate.Name
        Path = $candidate.FullName
        Inferred = $true
    }
}

function Get-Targets([string]$projectRoot, [object]$goal) {
    return @(
        [pscustomobject]@{
            Kind = "rollup"
            Path = Join-Path $projectRoot "PROJECT_STATUS.md"
            Action = "append documentation checkpoint row"
        },
        [pscustomobject]@{
            Kind = "goal-plan"
            Path = Join-Path $goal.Path "plan.md"
            Action = "append checkpoint note"
        },
        [pscustomobject]@{
            Kind = "goal-context"
            Path = Join-Path $goal.Path "context.md"
            Action = "append orchestrator context checkpoint"
        },
        [pscustomobject]@{
            Kind = "roadmap"
            Path = Join-Path $projectRoot "docs\roadmap\roadmap.yaml"
            Action = "append documentation_checkpoints entry"
        },
        [pscustomobject]@{
            Kind = "decision-log"
            Path = Join-Path $projectRoot "docs\architecture\decision_log.md"
            Action = "append accepted decisions only when -Decision is provided"
        }
    )
}

function Write-DryRun([object[]]$targets, [object]$goal, [string]$checkpointId, [string]$timestamp) {
    Write-Host "Sourcefold documentation checkpoint"
    Write-Host "Mode: dry-run"
    Write-Host "Checkpoint: $checkpointId"
    Write-Host "Timestamp: $timestamp"
    Write-Host "Goal: $($goal.Id)" -NoNewline
    if ($goal.Inferred) { Write-Host " (inferred from latest plan directory)" } else { Write-Host "" }
    Write-Host ""
    Write-Host "Files that would be updated with -Apply:"
    foreach ($target in $targets) {
        Write-Host "- [$($target.Kind)] $($target.Path)"
        Write-Host "  action: $($target.Action)"
    }
    Write-Host ""
    Write-Host "Payload:"
    Write-Host "- type: $CheckpointType"
    Write-Host "- summary: $Summary"
    Write-Host "- completed: $($Completed.Count)"
    Write-Host "- next: $($Next.Count)"
    Write-Host "- blockers: $($Blockers.Count)"
    Write-Host "- roadmap nodes: $($RoadmapNode -join ', ')"
    Write-Host "- decisions: $($Decision.Count)"
    Write-Host ""
    Write-Host "Run again with -Apply to write the checkpoint."
}

function Update-ProjectStatus([string]$path, [string]$timestamp, [string]$checkpointId, [object]$goal) {
    $section = "## Documentation Checkpoints"
    $row = "| ``$checkpointId`` | $timestamp | $CheckpointType | $Summary | ``$($goal.Id)`` | $($RoadmapNode -join ', ') | |"
    $content = Get-Content -Raw -LiteralPath $path

    if ($content -notmatch [regex]::Escape($section)) {
        $append = @"

$section

| Checkpoint | Created | Type | Summary | Goal | Roadmap Nodes | Notes |
|---|---|---|---|---|---|---|
$row
"@
        Add-TextIfMissing $path $append
        return
    }

    $content = $content -replace "(\|---\|---\|---\|---\|---\|---\|---\|\r?\n)", ('$1' + $row + [Environment]::NewLine)
    Set-Content -LiteralPath $path -Value $content -Encoding UTF8
}

function Update-GoalFiles([object]$goal, [string]$timestamp, [string]$checkpointId) {
    $completedText = Format-MarkdownList $Completed "No completed items supplied."
    $nextText = Format-MarkdownList $Next "No next items supplied."
    $blockerText = Format-MarkdownList $Blockers "No blockers supplied."
    $nodeText = Format-MarkdownList $RoadmapNode "No roadmap nodes supplied."
    $decisionText = Format-MarkdownList $Decision "No accepted decisions supplied."

    $block = @"

## Documentation Checkpoint: $checkpointId

- Created: $timestamp
- Type: $CheckpointType
- Summary: $Summary

Completed:
$completedText

Next:
$nextText

Blockers:
$blockerText

Roadmap nodes:
$nodeText

Accepted decisions:
$decisionText
"@

    Add-TextIfMissing (Join-Path $goal.Path "plan.md") $block
    Add-TextIfMissing (Join-Path $goal.Path "context.md") $block
}

function Update-Roadmap([string]$path, [string]$timestamp, [string]$checkpointId, [object]$goal) {
    $entry = @"

documentation_checkpoints:
  - id: $checkpointId
    created_at: $(ConvertTo-YamlScalar $timestamp)
    type: $(ConvertTo-YamlScalar $CheckpointType)
    goal: $(ConvertTo-YamlScalar $goal.Id)
    summary: $(ConvertTo-YamlScalar $Summary)
    roadmap_nodes: $(ConvertTo-YamlInlineList $RoadmapNode)
    blockers: $(ConvertTo-YamlInlineList $Blockers)
"@

    $content = Get-Content -Raw -LiteralPath $path
    if ($content -match "(?m)^documentation_checkpoints:\s*$") {
        $item = @"
  - id: $checkpointId
    created_at: $(ConvertTo-YamlScalar $timestamp)
    type: $(ConvertTo-YamlScalar $CheckpointType)
    goal: $(ConvertTo-YamlScalar $goal.Id)
    summary: $(ConvertTo-YamlScalar $Summary)
    roadmap_nodes: $(ConvertTo-YamlInlineList $RoadmapNode)
    blockers: $(ConvertTo-YamlInlineList $Blockers)
"@
        Add-TextIfMissing $path $item
        return
    }

    Add-TextIfMissing $path $entry
}

function Update-DecisionLog([string]$path, [string]$timestamp, [string]$checkpointId) {
    if (-not $Decision -or $Decision.Count -eq 0) { return }
    $decisionText = Format-MarkdownList $Decision "No accepted decisions supplied."
    $block = @"

## $timestamp - $checkpointId

$decisionText
"@
    Add-TextIfMissing $path $block
}

if (-not $Summary) {
    $Summary = "Documentation/status checkpoint."
}

$projectRoot = Get-ProjectRoot
$goal = Resolve-GoalId $projectRoot $GoalId
$timestamp = Get-CheckpointTimestamp
$checkpointId = Get-CheckpointId $timestamp
$targets = Get-Targets $projectRoot $goal

foreach ($target in $targets) {
    if (-not (Test-Path -LiteralPath $target.Path)) {
        throw "Required target missing: $($target.Path)"
    }
}

if (-not $Apply) {
    Invoke-RoadmapValidation $projectRoot
    Write-DryRun $targets $goal $checkpointId $timestamp
    exit 0
}

Invoke-RoadmapValidation $projectRoot
Update-ProjectStatus (Join-Path $projectRoot "PROJECT_STATUS.md") $timestamp $checkpointId $goal
Update-GoalFiles $goal $timestamp $checkpointId
Update-Roadmap (Join-Path $projectRoot "docs\roadmap\roadmap.yaml") $timestamp $checkpointId $goal
Update-DecisionLog (Join-Path $projectRoot "docs\architecture\decision_log.md") $timestamp $checkpointId
Invoke-RoadmapValidation $projectRoot

Write-Host "Sourcefold documentation checkpoint written: $checkpointId"
Write-Host "Updated files:"
foreach ($target in $targets) {
    if ($target.Kind -eq "decision-log" -and (-not $Decision -or $Decision.Count -eq 0)) { continue }
    Write-Host "- $($target.Path)"
}
