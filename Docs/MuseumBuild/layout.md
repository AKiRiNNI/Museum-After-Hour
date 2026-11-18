# Museum layout contract (L_Museum_Main)

Map: `/Game/AfterHours/Maps/L_Museum_Main`. Units: cm (1 uu = 1 cm). **X = east, Y = north, Z = up.** Origin = south edge of the atrium, on its centre line.
Envelope: main floor x -50.25 m..50.25 m, y -24.25 m..101.75 m (about 100 x 126 m). Basement about 55 x 35 m at z = -450.

Construction rule: every room is its own shell (floor, ceiling, four 25 cm wall skins). Adjacent rooms sit exactly 50 cm apart, so shared walls are two skins back to back and each room keeps its own wall material. Floors and ceilings extend 25 cm under their own walls, so doorways have continuous floor. Doors are cut through both skins and get a 3-piece frame.

## Rooms (interior bounds in cm)

| ID | Name | x0..x1 | y0..y1 | floor z | height | size (m) | stage |
|---|---|---|---|---|---|---|---|
| Z01 | Vestibule | -600..600 | -2400..-1700 | 0 | 450 | 12 x 7 | 1 |
| Z02 | Lobby | -1200..1200 | -1650..-50 | 0 | 550 | 24 x 16 | 1 |
| Z03 | Security | 1250..2150 | -1250..-450 | 0 | 340 | 9 x 8 | 1 |
| Z03b | StaffOffice | -2150..-1250 | -1250..-450 | 0 | 340 | 9 x 8 | 1 |
| Z04 | Atrium | -1400..1400 | 0..3000 | 0 | 1000 | 28 x 30 | 1 |
| C01 | WestArcade | -4200..-1450 | 1250..1750 | 0 | 500 | 27.5 x 5 | 1 |
| C02 | EastArcade | 1450..4200 | 1250..1750 | 0 | 500 | 27.5 x 5 | 2 |
| Z05 | Sculpture (Hall of Figures) | -4700..-2700 | 1800..4800 | 0 | 700 | 20 x 30 | 1 |
| Z06 | Antiquities | -5000..-2400 | 4850..7050 | 0 | 550 | 26 x 22 | 2 |
| Z07 | CastCourt | -5000..-2400 | 7100..9700 | 0 | 900 | 26 x 26 | 2 |
| Z08 | Portraits | 2600..4800 | 1800..4200 | 0 | 500 | 22 x 24 | 2 |
| Z09 | WhiteCube | 2400..5000 | 4250..6850 | 0 | 600 | 26 x 26 | 3 |
| Z10 | Reflection | 2400..5000 | 6900..9700 | 0 | 550 | 26 x 28 | 3 |
| Z11a | Promenade | -300..300 | 3050..5150 | 0 | 600 | 6 x 21 | 1 |
| Z11b | CrossGallery | -2350..2350 | 7650..8250 | 0 | 550 | 47 x 6 | 2 |
| Z12 | NaturalHistory | -1300..1300 | 5200..7600 | 0 | 800 | 26 x 24 | 3 |
| Z13 | Specimen | 350..1750 | 3550..5150 | 0 | 450 | 14 x 16 | 3 |
| C03 | WestLink | -2650..-350 | 3800..4150 | 0 | 360 | 23 x 3.5 | 1 |
| C04 | EastLink | 1800..2350 | 4400..4750 | 0 | 360 | 5.5 x 3.5 | 3 |
| Z14 | Restoration | -2350..-350 | 8300..9700 | 0 | 400 | 20 x 14 | 4 |
| Z15 | Archives | 50..1900 | 8300..9700 | 0 | 380 | 18.5 x 14 | 4 |
| Z16 | ServiceSpine | -2350..5000 | 9750..10150 | 0 | 340 | 73.5 x 4 | 4 |
| S_A | StairA (shaft, z -450..400) | -300..0 | 8300..9700 | -450 | 850 | 3 x 14 | 4 |
| S_B | StairB (shaft, z -450..340) | 1950..2250 | 8400..9700 | -450 | 790 | 3 x 13 | 5 |
| Z17 | Storage (basement) | -3150..-350 | 7700..9700 | -450 | 380 | 28 x 20 | 5 |
| Z18 | Vault (basement) | -2550..-950 | 6250..7650 | -450 | 390 | 16 x 14 | 5 |
| Z19a | BsmtCorrS | -900..1900 | 6800..7150 | -450 | 320 | 28 x 3.5 | 5 |
| Z19b | BsmtCorrN | -300..1900 | 7750..8100 | -450 | 320 | 22 x 3.5 | 5 |
| Z19c | BsmtCorrNS | 1950..2250 | 6800..8350 | -450 | 320 | 3 x 15.5 | 5 |

The 19 required zones map to Z01..Z19 (Z11 = Promenade + CrossGallery, Z19 = the three basement corridor legs + StairB). C01..C04, Z03b and the two stair shafts are connectors.

Stairs: 24 solid steps, 18 cm rise, 32 to 34 cm run, 3 m wide. StairA top landing y 8300..8550 (z 0), bottom landing y 9400..9700 (z -450). StairB top landing y 9450..9700 (z 0), bottom landing y 8400..8650 (z -450).

## Doors (A side B, centre along the wall, clear width x height in cm)

| # | From | Side | To | Centre | W x H | Note |
|---|---|---|---|---|---|---|
| 1 | Vestibule | N | Lobby | x 0 | 400 x 320 | entrance |
| 2 | Lobby | N | Atrium | x 0 | 500 x 400 | |
| 3 | Lobby | E | Security | y -850 | 160 x 240 | staff |
| 4 | StaffOffice | E | Lobby | y -850 | 160 x 240 | staff |
| 5 | WestArcade | E | Atrium | y 1500 | 440 x 420 | |
| 6 | Atrium | E | EastArcade | y 1500 | 440 x 420 | gate: stage 2 |
| 7 | Atrium | N | Promenade | x 0 | 500 x 500 | |
| 8 | WestArcade | N | Sculpture | x -3700 | 300 x 400 | |
| 9 | EastArcade | N | Portraits | x 3700 | 300 x 360 | |
| 10 | Sculpture | N | Antiquities | x -3700 | 300 x 400 | gate: stage 2 |
| 11 | Antiquities | N | CastCourt | x -3700 | 360 x 400 | |
| 12 | CastCourt | E | CrossGallery | y 7950 | 500 x 450 | |
| 13 | Sculpture | E | WestLink | y 3975 | 300 x 300 | |
| 14 | WestLink | E | Promenade | y 3975 | 300 x 300 | |
| 15 | Promenade | N | NaturalHistory | x 0 | 500 x 450 | gate: stage 3 |
| 16 | Promenade | E | Specimen | y 4350 | 240 x 300 | gate: stage 3 |
| 17 | Specimen | N | NaturalHistory | x 900 | 240 x 300 | |
| 18 | Specimen | E | EastLink | y 4575 | 300 x 300 | |
| 19 | EastLink | E | WhiteCube | y 4575 | 300 x 300 | |
| 20 | Portraits | N | WhiteCube | x 3700 | 300 x 360 | gate: stage 3 |
| 21 | WhiteCube | N | Reflection | x 3700 | 300 x 400 | |
| 22 | CrossGallery | E | Reflection | y 7950 | 500 x 450 | gate: stage 3 |
| 23 | NaturalHistory | N | CrossGallery | x 0 | 500 x 450 | gate: stage 3 |
| 24 | CrossGallery | N | Restoration | x -1350 | 200 x 260 | staff, gate: stage 4 |
| 25 | CrossGallery | N | Archives | x 975 | 200 x 260 | staff, gate: stage 4 |
| 26 | CastCourt | E | Restoration | y 9000 | 160 x 240 | staff, gate: stage 4 |
| 27 | Restoration | N | ServiceSpine | x -1350 | 200 x 260 | staff |
| 28 | Archives | N | ServiceSpine | x 975 | 200 x 260 | staff |
| 29 | Reflection | N | ServiceSpine | x 3700 | 200 x 260 | staff, gate: stage 4 |
| 30 | Restoration | E | StairA | y 8425 | 160 x 240 | top landing |
| 31 | StairA | E | Archives | y 8425 | 160 x 240 | top landing |
| 32 | StairB | N | ServiceSpine | x 2100 | 200 x 240 | top landing, gate: stage 5 |
| 33 | Storage | E | StairA | y 9550 | 160 x 240 | bottom landing, gate: stage 5 |
| 34 | Vault | N | Storage | x -1750 | 240 x 280 | vault main door |
| 35 | Vault | E | BsmtCorrS | y 6975 | 160 x 240 | vault rear door |
| 36 | Storage | E | BsmtCorrN | y 7925 | 240 x 260 | |
| 37 | BsmtCorrS | E | BsmtCorrNS | y 6975 | 300 x 280 | |
| 38 | BsmtCorrN | E | BsmtCorrNS | y 7925 | 300 x 280 | |
| 39 | BsmtCorrNS | N | StairB | x 2100 | 240 x 260 | bottom landing |

Frames narrow each opening by 10 cm per side and 10 cm at the head.

## Graph checks (computed by the build script from the door list)

- Reachability: all 29 spaces are reachable from the Vestibule (breadth-first search over the door list: 0 unreached).
- Stage 1 loop (no later gate needed): Atrium - WestArcade - Sculpture - WestLink - Promenade - Atrium.
- West public loop: Atrium - WestArcade - Sculpture - Antiquities - CastCourt - CrossGallery - NaturalHistory - Promenade - Atrium.
- East public loop: Atrium - EastArcade - Portraits - WhiteCube - Reflection - CrossGallery - NaturalHistory - Promenade - Atrium, with a short cut WhiteCube - EastLink - Specimen - Promenade.
- Staff loop: CrossGallery - Restoration - ServiceSpine - Archives - CrossGallery, plus ServiceSpine - Reflection.
- Basement: two independent connections to the main floor (StairA from Restoration/Archives, StairB from ServiceSpine), and an internal loop Storage - Vault - BsmtCorrS - BsmtCorrNS - BsmtCorrN - Storage.

## Stage plan (proposed; no gating logic is implemented)

| Stage | Opens |
|---|---|
| 1 | Vestibule, Lobby, Security, StaffOffice, Atrium, WestArcade, Sculpture, WestLink, Promenade |
| 2 | EastArcade, Portraits, Antiquities, CastCourt, CrossGallery |
| 3 | WhiteCube, Reflection, NaturalHistory, Specimen, EastLink |
| 4 | Restoration, Archives, ServiceSpine, StairA |
| 5 | StairB, Storage, Vault, basement corridors |

Change from the prompt's suggestion: Promenade and WestLink are stage 1 so the first night already has a real loop for evading the anomaly.
