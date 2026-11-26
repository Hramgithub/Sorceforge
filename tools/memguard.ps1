<#
.SYNOPSIS
  Memory guard for long parallel work (owner's rule 2026-11-26: system RAM never above 85 %).

.DESCRIPTION
  Every few seconds reads the used share of physical memory. Above -Limit it stops the largest worker processes of this
  repository (python / pdftoppm / tesseract / pdftotext started for our tools and helper scripts) until usage is back
  under the limit, and logs each stop to .cache/memguard.log. It never touches anything else (no browsers, no Claude,
  no Codex). Run it in the background for the whole session:

    pwsh -NoProfile -File tools/memguard.ps1            # limit 85 %
    pwsh -NoProfile -File tools/memguard.ps1 -Once      # print current usage and exit

  The lead checks usage before launching each helper: `pwsh -NoProfile -File tools/memguard.ps1 -Once`.
#>
param(
    [int]$Limit = 85,
    [int]$IntervalSec = 3,
    [switch]$Once
)

$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$log = Join-Path $root '.cache\memguard.log'

function Get-UsedPercent {
    $os = Get-CimInstance Win32_OperatingSystem
    [math]::Round(100 * (1 - $os.FreePhysicalMemory / $os.TotalVisibleMemorySize), 1)
}

if ($Once) {
    $os = Get-CimInstance Win32_OperatingSystem
    $py = @(Get-Process python -ErrorAction SilentlyContinue)
    "память занята: $(Get-UsedPercent)% (свободно {0:N1} из {1:N1} ГБ); python: {2} процессов, {3:N1} ГБ" -f `
        ($os.FreePhysicalMemory / 1MB), ($os.TotalVisibleMemorySize / 1MB), $py.Count, (($py | Measure-Object WorkingSet64 -Sum).Sum / 1GB)
    exit 0
}

# our workers: python running repo tools/scripts, and the PDF/OCR tools they start
$pattern = 'tools[\\/]|pipeline[\\/]|lead-tools|Sorceforge|pdftoppm|pdftotext|tesseract'
while ($true) {
    $used = Get-UsedPercent
    if ($used -gt $Limit) {
        $victims = Get-CimInstance Win32_Process -Filter "Name='python.exe' or Name='pdftoppm.exe' or Name='pdftotext.exe' or Name='tesseract.exe'" |
            Where-Object { ($_.CommandLine -match $pattern) -or ($_.Name -ne 'python.exe') } |
            Sort-Object WorkingSetSize -Descending
        foreach ($v in $victims) {
            if ((Get-UsedPercent) -le $Limit - 5) { break }
            Stop-Process -Id $v.ProcessId -Force -ErrorAction SilentlyContinue
            $line = '{0:yyyy-MM-dd HH:mm:ss} память {1}% > {2}%: остановлен {3} pid {4} ({5:N0} МБ): {6}' -f (Get-Date), $used, $Limit,
                $v.Name, $v.ProcessId, ($v.WorkingSetSize / 1MB), ($v.CommandLine -replace '\s+', ' ').Substring(0, [math]::Min(200, ($v.CommandLine ?? '').Length))
            Add-Content -LiteralPath $log -Value $line -Encoding utf8
            Start-Sleep -Milliseconds 500
        }
    }
    Start-Sleep -Seconds $IntervalSec
}
