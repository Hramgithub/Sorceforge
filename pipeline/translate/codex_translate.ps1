<#
.SYNOPSIS
  Translate pages of a book with OpenAI Codex (codex exec) by the template codex_prompt.md (Р-251, skill kb-translate-codex).

.DESCRIPTION
  Task file (JSON, UTF-8): book, tr_dir, pages, title_en, credits, part, terms_md, art_glob, atmo, img_prefix, write_meta (bool),
  meta (object written into meta.json by Codex when write_meta). Renders the prompt, runs Codex in the repository with
  write access to the workspace only, saves the log and Codex's final report under .cache/codex/, then runs
  check_translation.py. The HTML is built by the lead (the library is outside the Codex sandbox).

.EXAMPLE
  pwsh -NoProfile -File pipeline/translate/codex_translate.ps1 -Task .cache/codex/tasks/goat-1.json
  pwsh -NoProfile -File pipeline/translate/codex_translate.ps1 -Task .cache/codex/tasks/goat-1.json -DryRun
#>
param(
    [Parameter(Mandatory)] [string]$Task,
    [string]$Model = 'gpt-6.2-sol', # owner's choice 2026-11-26 (trial until 2026-12-26); list: `codex debug models` or ~/.codex/models_cache.json
    [string]$Effort,                # low | medium | high | xhigh; default from config
    [switch]$DryRun                 # only render the prompt
)

$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [Text.Encoding]::UTF8
$OutputEncoding = [Text.Encoding]::UTF8

$root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$t = Get-Content -LiteralPath $Task -Raw -Encoding UTF8 | ConvertFrom-Json
$name = [IO.Path]::GetFileNameWithoutExtension($Task)
$out = Join-Path $root '.cache\codex'
New-Item -ItemType Directory -Force $out | Out-Null

$metaLine = if ($t.write_meta) {
    "- ``$($t.tr_dir)/meta.json`` — ровно это (дополни ``unnumbered``: физические страницы без печатного номера, если такие есть): ``$(($t.meta | ConvertTo-Json -Compress -Depth 5))``"
} else { "- ``meta.json`` пишет другая часть — не трогай." }

$vals = @{
    TITLE_EN = $t.title_en; CREDITS = $t.credits; PART = $t.part; BOOK = $t.book; TR_DIR = $t.tr_dir; PAGES = $t.pages
    TERMS_MD = $t.terms_md; TERMS_OUT = "$((Split-Path $t.tr_dir -Parent) -replace '\\','/')/codex-terms-$name.json"; ART_GLOB = $t.art_glob; ATMO = $t.atmo; IMG_PREFIX = $t.img_prefix; META_LINE = $metaLine
}
$prompt = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'codex_prompt.md') -Raw -Encoding UTF8
foreach ($k in $vals.Keys) { $prompt = $prompt.Replace("{$k}", [string]$vals[$k]) }
if ($prompt -match '\{[A-Z_]+\}') { throw "в шаблоне остался незаполненный ключ: $($Matches[0])" }
$promptFile = Join-Path $out "$name.prompt.md"
[IO.File]::WriteAllText($promptFile, $prompt, [Text.UTF8Encoding]::new($false))
if ($DryRun) { "промпт: $promptFile"; exit 0 }

# newest codex.exe (the desktop app keeps it in a hashed folder that changes on updates)
$candidates = @(
    Get-ChildItem "$env:LOCALAPPDATA\OpenAI\Codex\bin" -Recurse -Filter codex.exe -ErrorAction SilentlyContinue
    Get-Item "$env:LOCALAPPDATA\Programs\OpenAI\Codex\bin\codex.exe" -ErrorAction SilentlyContinue
    Get-Command codex -CommandType Application -ErrorAction SilentlyContinue | ForEach-Object { Get-Item $_.Source }
) | Where-Object { $_ }
if (-not $candidates) { throw 'codex.exe не найден' }
function Get-CodexVersion($exe) {
    $v = (& $exe --version 2>$null) -replace '^codex-cli\s+', ''
    try { [version](($v -split '-')[0]) } catch { [version]'0.0' }
}
$codex = $candidates | Sort-Object FullName -Unique | Sort-Object { Get-CodexVersion $_.FullName }, LastWriteTime -Descending | Select-Object -First 1

$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$log = Join-Path $out "$name-$stamp.log"
$report = Join-Path $out "$name.report.md"
$args2 = @('exec', '--json', '--skip-git-repo-check', '--color', 'never', '-s', 'workspace-write', '-c', 'approval_policy="never"', '-C', $root, '-o', $report)
# Lean run for our work only (the global ~/.codex/config.toml stays as the owner keeps it for other projects):
# no memories of other projects, no web search, no MCP servers (node_repl may take up to 2 min to start), no app plugins,
# no desktop notify hook — the translator needs only the shell, files and image viewing.
$args2 += @('--disable', 'memories', '-c', 'web_search="disabled"', '-c', 'notify=[]')
# The owner's config sets PATH for Codex shells without Python (2026-11-26: Codex could not run pages.py / the checker).
# Put the Python of this machine and the PDF/OCR tools in front of it; TOML literal string — no escaping of backslashes.
$py = (Get-Command python -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1).Source
$extra = @($(if ($py) { Split-Path $py }), $(if ($py) { Join-Path (Split-Path $py) 'Scripts' })) + ($env:PATH -split ';') |
    Where-Object { $_ -and $_ -notmatch "'" } | Select-Object -Unique
$args2 += @('-c', "shell_environment_policy.set.PATH='$($extra -join ';')'")
foreach ($s in 'node_repl', 'filesystem', 'microsoft-docs') { $args2 += @('-c', "mcp_servers.$s.enabled=false") }
foreach ($p in 'documents@openai-primary-runtime', 'spreadsheets@openai-primary-runtime', 'presentations@openai-primary-runtime',
    'pdf@openai-primary-runtime', 'computer-use@openai-bundled', 'visualize@openai-bundled', 'browser@openai-bundled',
    'template-creator@openai-primary-runtime', 'codex-app-tools@openai-bundled', 'unified-computer-use@openai-bundled', 'plan@openai-bundled') {
    $args2 += @('-c', "plugins.`"$p`".enabled=false")
}
if ($Model) { $args2 += @('-m', $Model) }
if ($Effort) { $args2 += @('-c', "model_reasoning_effort=`"$Effort`"") }
$args2 += '-'

"codex $(Get-CodexVersion $codex.FullName): $name, страницы $($t.pages); лог $log"
$started = Get-Date
$prompt | & $codex.FullName @args2 *> $log
$code = $LASTEXITCODE
"codex завершился с кодом $code за $([int]((Get-Date) - $started).TotalMinutes) мин; отчёт: $report"
# token use of the run (JSON events in the log); errors such as a usage limit or an unknown model
$in = 0; $outTok = 0
foreach ($line in Get-Content -LiteralPath $log -Encoding UTF8) {
    if ($line -like '{"type":"turn.completed"*') { $u = ($line | ConvertFrom-Json).usage; $in += $u.input_tokens; $outTok += $u.output_tokens + $u.reasoning_output_tokens }
    elseif ($line -match 'not supported|usage limit|rate limit|ERROR') { "  ! $($line.Substring(0, [Math]::Min(200, $line.Length)))" }
}
"токены Codex: вход $in, выход $outTok"

Push-Location $root
try { python -I -B pipeline/translate/check_translation.py $t.tr_dir $t.book --pages $t.pages | Select-Object -Last 6 }
finally { Pop-Location }
exit $code
