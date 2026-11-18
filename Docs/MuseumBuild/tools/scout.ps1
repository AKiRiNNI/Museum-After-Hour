# Asset scouting helper: runs Sozai searches, prints one line per hit, and builds a labelled
# thumbnail contact sheet so candidates can be judged visually before anything is fetched.
# Usage: scout.ps1 -Kind material -Sheet out.png -Queries "marble","terrazzo" [-Sources polyhaven,ambientcg] [-Limit 4]
param([string]$Kind = "material", [string]$Sheet, [string[]]$Queries, [string[]]$Sources = @("polyhaven", "ambientcg"), [int]$Limit = 4)
$uvx = "$env:LOCALAPPDATA\Microsoft\WinGet\Packages\astral-sh.uv_Microsoft.Winget.Source_8wekyb3d8bbwe\uvx.exe"
Add-Type -AssemblyName System.Drawing
$tmp = Join-Path $env:TEMP "claude\mus_thumbs"; New-Item -ItemType Directory -Force $tmp | Out-Null
$hits = @(); $seen = @{}
foreach ($q in $Queries) {
    foreach ($s in $Sources) {
        $raw = & $uvx --from git+https://github.com/kanaworksai-hue/sozai-search-mcp sozai search $q --kind $Kind --source $s --limit $Limit 2>$null | Out-String
        try { $j = $raw | ConvertFrom-Json } catch { continue }
        foreach ($r in $j.results) {
            if ($seen[$r.id]) { continue }; $seen[$r.id] = 1
            $size = if ($r.size_m) { ($r.size_m | % { "{0:0.##}" -f $_ }) -join "x" } else { "?" }
            "{0} | {1} | {2}m | poly {3}" -f $r.id, $r.title, $size, $r.polycount
            $hits += $r
        }
    }
}
if (-not $Sheet) { return }
$cell = 168; $cols = 8; $rows = [Math]::Ceiling($hits.Count / $cols)
$bmp = New-Object System.Drawing.Bitmap ($cols * $cell), ([Math]::Max(1, $rows) * ($cell + 28))
$g = [System.Drawing.Graphics]::FromImage($bmp); $g.Clear([System.Drawing.Color]::FromArgb(30, 30, 30))
$font = New-Object System.Drawing.Font "Arial", 8
$i = 0
foreach ($r in $hits) {
    $x = ($i % $cols) * $cell; $y = [Math]::Floor($i / $cols) * ($cell + 28)
    if ($r.thumbnail_url) {
        $f = Join-Path $tmp (($r.id -replace '[^A-Za-z0-9_]', '_') + ".img")
        if (-not (Test-Path $f)) { try { Invoke-WebRequest ($r.thumbnail_url -replace 'format=webp', 'format=png') -OutFile $f -UseBasicParsing } catch {} }
        try { $img = [System.Drawing.Image]::FromFile($f); $g.DrawImage($img, $x + 2, $y + 2, $cell - 4, $cell - 4); $img.Dispose() } catch {}
    }
    $g.DrawString(($r.id -replace '^[a-z]+:', ''), $font, [System.Drawing.Brushes]::White, $x + 2, $y + $cell)
    $i++
}
$bmp.Save($Sheet, [System.Drawing.Imaging.ImageFormat]::Png); $g.Dispose(); $bmp.Dispose()
"sheet: $Sheet ($($hits.Count) items)"
