import json
EA = 'EditorToolset.EditorAppToolset.'
AT = 'editor_toolset.toolsets.asset.AssetTools.'
OUT = 'C:/Users/block/OneDrive/Documents/Unreal Projects/Museum-After-Hour/Museum_After_Hours/Saved/MuseumShots/r8/'
# name, x, y, z, yaw, pitch  (eye height 170 cm above each floor)
V = [('01_security', 1300, -850, 170, 20, 0), ('02_restoration', -1350, 8350, 170, 100, 0), ('03_archives', 975, 8350, 170, 90, 0),
     ('04_spine', -2300, 9950, 170, 0, 0), ('05_storage', -450, 9550, -280, 200, 0), ('06_bsmtcorr', -850, 6975, -280, 0, 0),
     ('07_vault', -1750, 7600, -280, -90, 0), ('08_staffoffice', -1300, -850, 170, 180, 0), ('09_stairB', 2100, 9650, 170, -90, -22)]
REP = 6
ANN = {'gridSpacing': 0, 'gridExtent': 0, 'gridHeight': 0, 'maxLabelDistance': 0, 'classFilter': {'refPath': '/Script/Engine.Actor'}, 'maxLabels': 0}


def call(n, a):
    return execute_tool(n, json.dumps(a))['returnValue']


def run():
    for nm, x, y, z, yaw, p in V:
        t = {'location': {'x': x, 'y': y, 'z': z}, 'rotation': {'pitch': p, 'yaw': yaw, 'roll': 0}, 'scale': {'x': 1, 'y': 1, 'z': 1}}
        for i in range(REP):  # repeated captures let Lumen and exposure settle
            r = call(EA + 'CaptureViewport', {'captureTransform': t, 'annotations': ANN, 'bShowUI': False})
        call(AT + 'write_file', {'content': r['image']['data'], 'file_path': OUT + nm + '.txt'})
    return {'ok': len(V)}
