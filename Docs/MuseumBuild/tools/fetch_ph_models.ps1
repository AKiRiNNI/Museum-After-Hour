# Downloads Poly Haven (CC0) models as FBX plus their textures into Docs/MuseumBuild/staging/models/<id>/.
# Unreal's StaticMeshTools.import_file only takes FBX/OBJ, so the FBX package is fetched from the
# official Poly Haven API instead of the glTF that Sozai's fetch returns.
# Usage: fetch_ph_models.ps1 -Res 1k -Ids a,b,c
param([string]$Res = "1k", [string[]]$Ids)
$dst = Join-Path $PSScriptRoot "..\staging\models"; New-Item -ItemType Directory -Force $dst | Out-Null
$ua = @{ "User-Agent" = "MuseumAfterHours-student-project/1.0" }
foreach ($id in $Ids) {
    try { $j = Invoke-RestMethod "https://api.polyhaven.com/files/$id" -Headers $ua } catch { "$id | API ERROR $($_.Exception.Message)"; continue }
    if (-not $j.fbx) { "$id | no fbx; keys: $(($j.PSObject.Properties.Name) -join ',')"; continue }
    $r = if ($j.fbx.$Res) { $Res } else { ($j.fbx.PSObject.Properties.Name | Select-Object -First 1) }
    $f = $j.fbx.$r.fbx
    $dir = Join-Path $dst $id; New-Item -ItemType Directory -Force $dir | Out-Null
    $fbx = Join-Path $dir ([IO.Path]::GetFileName($f.url))
    if (-not (Test-Path $fbx)) { Invoke-WebRequest $f.url -OutFile $fbx -Headers $ua -UseBasicParsing }
    $tex = @()
    foreach ($p in $f.include.PSObject.Properties) {
        $out = Join-Path $dir ($p.Name -replace '/', '\'); New-Item -ItemType Directory -Force (Split-Path $out) | Out-Null
        if (-not (Test-Path $out)) { Invoke-WebRequest $p.Value.url -OutFile $out -Headers $ua -UseBasicParsing }
        $tex += [IO.Path]::GetFileName($p.Name)
    }
    "{0} | {1} | fbx {2:N1} MB | {3}" -f $id, $r, ((Get-Item $fbx).Length / 1MB), ($tex -join ' ')
}
