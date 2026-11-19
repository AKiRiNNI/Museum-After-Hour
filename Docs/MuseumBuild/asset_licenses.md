# Third-party assets used in L_Museum_Main

Every third-party asset in the museum is **CC0** (public domain), so no attribution is legally required. Credits are kept anyway, and Poly Haven asks API users to say "Powered by Poly Haven".
Source files were downloaded to `Docs/MuseumBuild/staging/`, which is git-ignored and can be re-fetched with `tools/fetch_ph_models.ps1` and `sozai fetch`. Unreal assets were imported under `/Game/AfterHours/Environment/Museum/`.

## Surface textures (2K): `/Game/AfterHours/Environment/Museum/Materials/Textures/`

| Unreal set | Source | Licence |
|---|---|---|
| T_MUS_MarbleCream_* | Marble 01, https://polyhaven.com/a/marble_01 | CC0, Powered by Poly Haven |
| T_MUS_MarbleWhite_* | Marble 012, https://ambientcg.com/a/Marble012 | CC0, ambientCG |
| T_MUS_Terrazzo_* | Terrazzo 004, https://ambientcg.com/a/Terrazzo004 | CC0, ambientCG |
| T_MUS_Plaster_* | Beige Wall 001, https://polyhaven.com/a/beige_wall_001 | CC0, Powered by Poly Haven |
| T_MUS_Parquet_* | Herringbone Parquet, https://polyhaven.com/a/herringbone_parquet | CC0, Powered by Poly Haven |
| T_MUS_DarkWood_* | Dark Wood, https://polyhaven.com/a/dark_wood | CC0, Powered by Poly Haven |
| T_MUS_Checker_* | Tiles 074, https://ambientcg.com/a/Tiles074 | CC0, ambientCG |
| T_MUS_Granite_* | Granite Tile, https://polyhaven.com/a/granite_tile | CC0, Powered by Poly Haven |

## Models (FBX from the Poly Haven API, 1K textures; statues 2K): `/Game/AfterHours/Environment/Museum/Props/<id>/SM_MUS_<id>`

All 51 are CC0 and Powered by Poly Haven. Source page: `https://polyhaven.com/a/<id>`.

antique_ceramic_vase_01, antique_estoc, antique_katana_01, ArmChair_01, brass_vase_03, bronze_whale_statue, Camera_01, cardboard_box_01, carved_wooden_elephant, ceramic_vase_01, ceramic_vase_02, concrete_cat_statue, desk_lamp_arm_01, drawer_cabinet, fancy_picture_frame_01, fancy_picture_frame_02, GothicCabinet_01, gothic_statue (2K), GreenChair_01, hand_truck, hanging_picture_frame_02, horse_head, horse_statue_01 (2K), jug_01, korean_fire_extinguisher_01, lambis_shell, Lantern_01, lion_head, marble_bust_01 (2K), metal_office_desk, metal_tool_chest, mid_century_lounge_chair, modular_industrial_pipes_01, ornate_mirror_01, painted_wooden_bench, potted_plant_01, rollershutter_door, round_wooden_table_01, SchoolChair_01, security_camera_01, Shelf_01, standing_picture_frame_02, Television_01, tool_cart, utility_box_02, vintage_cabinet_01, vintage_grandfather_clock_01, vintage_microscope, wooden_crate_01, wooden_ladder_02, worn_metal_rack.

Imported but not yet placed in the map: GreenChair_01, painted_wooden_bench, modular_industrial_pipes_01.

## Project content reused (no new licence)

- `/Game/Characters/Mannequins/Meshes/SKM_Manny_Simple`, `SKM_Quinn_Simple` posed with the template animations: **stand-in statues** (tag `MUS_StandIn`), in marble, bronze or plaster materials. Replace them with real scanned statues later; see "Swap list" in `progress.md`.
- `/Engine/BasicShapes/*`: architecture, plinths, cases, signage and other modular blockout pieces.

## Not used

- No Megascans or Fab content (that needs an Epic account claim, so it was left to the team).
- No Smithsonian or Met Open Access scans. Those are good candidates for the stand-in swap.
