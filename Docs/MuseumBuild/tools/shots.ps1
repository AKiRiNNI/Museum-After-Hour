# Decodes viewport captures (*.b64 written by the editor via AssetTools.write_file) to PNG
# and builds one labelled contact sheet for review.
# Usage: shots.ps1 -Dir <folder with .b64> -Out sheet.png [-Cols 3] [-CellW 640]
param([string]$Dir, [string]$Out, [int]$Cols = 3, [int]$CellW = 640)
Add-Type -AssemblyName System.Drawing
$imgs = @()
Get-ChildItem $Dir -Filter *.txt | Sort-Object Name | ForEach-Object {
    $png = [IO.Path]::ChangeExtension($_.FullName, ".png")
    [IO.File]::WriteAllBytes($png, [Convert]::FromBase64String((Get-Content $_.FullName -Raw)))
    Remove-Item $_.FullName
    $imgs += $png
}
if (-not $imgs) { $imgs = (Get-ChildItem $Dir -Filter *.png | Sort-Object Name).FullName }
$first = [System.Drawing.Image]::FromFile($imgs[0]); $cellH = [int]($CellW * $first.Height / $first.Width); "source size: $($first.Width)x$($first.Height)"; $first.Dispose()
$rows = [Math]::Ceiling($imgs.Count / $Cols)
$bmp = New-Object System.Drawing.Bitmap ($Cols * $CellW), ($rows * ($cellH + 18))
$g = [System.Drawing.Graphics]::FromImage($bmp); $g.Clear([System.Drawing.Color]::Black)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$font = New-Object System.Drawing.Font "Arial", 9
$i = 0
foreach ($p in $imgs) {
    $x = ($i % $Cols) * $CellW; $y = [Math]::Floor($i / $Cols) * ($cellH + 18)
    $im = [System.Drawing.Image]::FromFile($p); $g.DrawImage($im, $x, $y, $CellW, $cellH); $im.Dispose()
    $g.DrawString([IO.Path]::GetFileNameWithoutExtension($p), $font, [System.Drawing.Brushes]::Yellow, $x + 3, $y + $cellH + 1)
    $i++
}
$bmp.Save($Out, [System.Drawing.Imaging.ImageFormat]::Png); $g.Dispose(); $bmp.Dispose()
"sheet: $Out ($($imgs.Count) views)"
