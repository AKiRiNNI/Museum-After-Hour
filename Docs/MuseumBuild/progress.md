# Museum build: progress and handover

Map: **`/Game/AfterHours/Maps/L_Museum_Main`** (UE 5.8). It is a separate level. `Lvl_FirstPerson`, the GameMode, the character, the input and the project's default maps were not touched.
Status (2026-11-18): **all 19 required zones are built, dressed, lit, marked up and saved.** It is environment only; no gameplay logic was added.

See also: `layout.md` (room rectangles, door table, stage plan), `build_manifest.json` (counts from the final audit), `asset_licenses.md`.

## What is in the level

- **Shell:** 29 spaces (19 zones plus connectors, stair shafts and basement corridor legs), 500 floor, wall and ceiling pieces, 39 framed doorways and two real 24-step stairs to the basement (StairA from Restoration/Archives, StairB from the Service Spine).
- **Materials:** a world-aligned triplanar master (`M_MUS_Tex`) with 19 textured instances (marble, terrazzo, checker marble, parquet, granite, plaster in cream, honey, burgundy, sage, service green, white, concrete and charcoal), a flat master with 16 instances plus 6 emissive instances, and glass. Every zone has its own floor and wall combination.
- **Exhibits and props:** 51 CC0 Poly Haven models (busts, horse, Gothic statue, bronze whale, frames, vases, weapons, cabinets, racks, tools, carts and more), plus 10 posed mannequin "statues" in marble, bronze or plaster (stand-ins).
- **Hero rooms:**
  - Hall of Figures: symmetric figure and bust rows on checker marble, warm spot pools, one bust turned toward the entrance, one bronze among the marble, and a lone far figure backlit at the end of the axis.
  - Atrium: inlaid floor, horse centrepiece, pilasters, clerestory windows, benches and way-signs.
  - White Cube: clinical cool light, huge negative space and an empty plinth with a full label.
  - Vault: a sealed glass case round the Gothic statue, deposit-drawer walls, one drawer ajar, a heavy door and status lights.
  - Natural History: a mounted skeleton stand-in, a bronze whale and dioramas.
- **Lighting (three layers):**
  - Functional: 144 ceiling downlights with fixtures, plus stair lights and staff fills.
  - Exhibition: about 115 aimed spots, warm in the classical rooms, neutral or cool in the contemporary and staff areas.
  - Uncanny: a bright note in an empty antiquities case, the backlit far figure, the clinical White Cube, cold service lighting, and 6 lights named `ENV_Light_FlickerReady_*`.
  - Post process: unbound volume `MUS_PostProcess_Night` with fixed exposure (min = max = 4.2), white balance 4000 K, vignette 0.5 and bloom 0.4.
- **Integration hooks (TargetPoints and TriggerBoxes, no logic):**
  - Task candidates: `ENV_TaskCandidate_{Inspect|Clean|Maintenance|Disturbance}_<Zone>_NN`, with 91 Inspect, 49 Clean, 30 Maintenance and 31 Disturbance. Each is tagged with its zone ID and `StageN`. By stage: 37 / 73 / 49 / 20 / 22.
  - 127 `ENV_PatrolWaypoint_*`, tagged with the zone and `Adj_<Room>` for every adjacent room.
  - 29 `ENV_ZoneBoundary_*` trigger boxes.
  - 13 `ENV_ProgressionGate_StageN_*`, at every door between different stages, plus 26 `ENV_DoorAnchor_*`. Both are tagged with clear width (`W…`) and height (`H…`).
  - 1 `ENV_SpawnCandidate_Security`.
  - 63 actors tagged `ENV_StatuePivot`: the statues and objects a teammate can later rotate or move for "disturbance" moments.
- **World:** `MUS_PlayerStart_Lobby` and `MUS_NavMeshBounds` (one volume over the whole museum, both floors). A RecastNavMesh actor exists.
- **Outliner:** everything is under `Museum/<ZoneID>_<Room>/{Shell, Lights, Exhibits, Dressing, Stairs}`, `Museum/Doors/...`, `Museum/_Markers/...` and `Museum/_World`.

## Acceptance checks

| Check | Result | Evidence |
|---|---|---|
| Map exists, loads, original work intact | PASS | `load_level` reload: 1694 actors before and after. `Lvl_FirstPerson` and `/Game/FirstPerson` are unchanged (git shows no changes there). |
| All 19 zones physically built | PASS | 29 shells, 500 shell pieces (audit); screenshot rounds r5, r7 and r8 cover every wing. |
| Connected graph, loops, two basement links | PASS (graph) | A breadth-first search over the 39-door table reaches all 29 spaces from the Vestibule. StairA and StairB are real solid steps. Walk-through: NOT TESTED. |
| Widths | PASS (by construction) | Main corridors 4.0 to 6 m, links 3.5 m, gallery doors 3.0 to 5.0 m and staff doors 1.6 to 2.0 m clear (frames take 10 cm a side). Staff doors are below the 2.4 m gallery target on purpose. |
| Task candidate minimums (30 / 20 / 12 / 10) | PASS | 91 / 49 / 30 / 31. Every stage has its own candidates. |
| Instanced arrays sane | PASS | 1224 instances, 0 left at the origin. |
| Lighting readable with flashlight off | PASS (visual) | Final screenshots of public rooms, staff areas, basement and stairs; dark staff zones were re-lit in r8. |
| Persistence | PASS | Saved, not dirty after save, and the actor count is unchanged after reload. |
| NavMesh coverage | NOT TESTED | The bounds volume and a RecastNavMesh actor exist, but no MCP tool reports coverage. Press P in the viewport to check, especially the stairs. |
| PIE first-person traversal | NOT TESTED | Not run, to avoid touching the GameMode. Start PIE from `MUS_PlayerStart_Lobby` to try it. |
| Performance | NOT TESTED | About 270 dynamic lights with shadows on the exhibit spots; run `stat unit` and `stat gpu`. |

## Known gaps and next steps for the team

1. **Stand-in statues:** the 10 skeletal mannequins (tag `MUS_StandIn`) and the cylinder skeleton should be replaced with real scans, such as Smithsonian or Met Open Access CC0 sculptures or Fab/Megascans statues. Their positions and facings are the design: keep the transforms.
2. **Navmesh:** check coverage on the stairs and through the 1.6 m staff doors. Widen the doors if the anomaly capsule does not fit.
3. **Performance:** most exhibit spots cast shadows. If GPU-bound, turn off `CastShadows` on spots that light flat walls first.
4. **Doors:** openings are frame-only. Door leaves can go on the `ENV_DoorAnchor` / `ENV_ProgressionGate` markers.
5. **Unused imports:** GreenChair_01, painted_wooden_bench and modular_industrial_pipes_01 are imported but not placed.
6. **Flicker:** the 6 `ENV_Light_FlickerReady_*` lights are named and tagged; there is no flicker component yet.

## Tools (re-runnable)

`Docs/MuseumBuild/tools/`:
- `mcp_call.mjs`: run a batch script against the editor's MCP server, `node mcp_call.mjs script.py`.
- `capture.py` + `shots.ps1`: viewport screenshots to a contact sheet.
- `final_audit.py`: the audit above.
- `fix_service_lights.py`: the staff and basement relight.
- `fetch_ph_models.ps1`: re-download the CC0 source models.
- `scout.ps1`: Sozai search with thumbnail sheets.

Source downloads live in `Docs/MuseumBuild/staging/` (git-ignored, about 300 MB).

Traps hit during the build: never click modal menu items through SlateInspector, because it freezes the editor. `AssetTools.read_file` and `write_file` only work under Content/ or Saved/, with a 80 KB read limit and .txt/.json/.md/.csv/.py/.html only. `StaticMeshTools.import_file` takes FBX/OBJ, not glTF. Skeletal mannequins need `bUsedWithSkeletalMesh` on any material applied to them, and that is set on `M_MUS_Tex` and `M_MUS_Flat`.
