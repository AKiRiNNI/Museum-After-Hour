import json
ST = 'editor_toolset.toolsets.scene.SceneTools.'
OT = 'editor_toolset.toolsets.object.ObjectTools.'
AT = 'editor_toolset.toolsets.asset.AssetTools.'
# room -> (intensity multiplier, minimum outer cone in degrees): flatter, wider "fluorescent" coverage in staff/basement zones
ROOMS = {'Security': (2.5, 55), 'StaffOffice': (2.5, 55), 'Restoration': (2.2, 55), 'Archives': (2.8, 50),
         'ServiceSpine': (3.0, 55), 'Storage': (3.0, 55), 'Vault': (2.0, 45), 'BsmtCorrS': (3.0, 55),
         'BsmtCorrN': (3.0, 55), 'BsmtCorrNS': (3.0, 55), 'Specimen': (1.6, 45), 'WestLink': (1.8, 40), 'EastLink': (1.8, 40)}


def call(n, a):
    return execute_tool(n, json.dumps(a))['returnValue']


def run():
    out = {}
    for room, (k, cone) in ROOMS.items():
        acts = call(ST + 'find_actors', {'name': 'MUS_Light_%s_F' % room, 'tag': '', 'collision_channels': []})
        acts += call(ST + 'find_actors', {'name': 'ENV_Light_FlickerReady_%s_' % room, 'tag': '', 'collision_channels': []})
        for a in acts:
            lc = {'refPath': a['refPath'] + '.LightComponent0'}
            p = json.loads(call(OT + 'get_properties', {'instance': lc, 'properties': ['Intensity', 'OuterConeAngle']}))
            oc = max(p['OuterConeAngle'], cone)
            call(OT + 'set_properties', {'instance': lc, 'values': json.dumps({'Intensity': p['Intensity'] * k, 'OuterConeAngle': oc, 'InnerConeAngle': oc * 0.5})})
        out[room] = len(acts)
    out['saved'] = call(AT + 'save_assets', {'asset_paths': ['/Game/AfterHours/Maps/L_Museum_Main']})
    return out
