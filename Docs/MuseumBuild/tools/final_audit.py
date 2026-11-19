import json
ST = 'editor_toolset.toolsets.scene.SceneTools.'
OT = 'editor_toolset.toolsets.object.ObjectTools.'
AT = 'editor_toolset.toolsets.asset.AssetTools.'
AC = 'editor_toolset.toolsets.actor.ActorTools.'
L = '/Game/AfterHours/Maps/L_Museum_Main'
EXTRA = [('Security', 'Z03', 1500, -650), ('Security', 'Z03', 1900, -1050), ('StaffOffice', 'Z03b', -1500, -650), ('StaffOffice', 'Z03b', -1900, -1050)]


def call(n, a):
    return execute_tool(n, json.dumps(a))['returnValue']


def find(name='', tag='', cls=None):
    a = {'name': name, 'tag': tag, 'collision_channels': []}
    if cls:
        a['actor_type'] = {'refPath': cls}
    return call(ST + 'find_actors', a)


def run():
    # Fill lights for the two small staff rooms (idempotent: skipped if they already exist).
    for i, (room, zid, x, y) in enumerate(EXTRA):
        nm = 'MUS_Light_%s_Fill%d' % (room, i % 2)
        if find(nm):
            continue
        a = call(ST + 'add_to_scene_from_class', {'actor_type': {'refPath': '/Script/Engine.SpotLight'}, 'name': nm,
              'xform': {'location': {'x': x, 'y': y, 'z': 324}, 'rotation': {'pitch': -90, 'yaw': 0, 'roll': 0}, 'scale': {'x': 1, 'y': 1, 'z': 1}}})
        call(OT + 'set_properties', {'instance': {'refPath': a['refPath'] + '.LightComponent0'}, 'values': json.dumps(
            {'IntensityUnits': 'Candelas', 'Intensity': 450, 'bUseTemperature': True, 'Temperature': 4000, 'AttenuationRadius': 600,
             'InnerConeAngle': 30, 'OuterConeAngle': 60, 'CastShadows': False, 'IndirectLightingIntensity': 2.5})})
        call(ST + 'set_actor_folder', {'actor': a, 'folder_path': 'Museum/%s_%s/Lights' % (zid, room)})
    call(AT + 'save_assets', {'asset_paths': [L]})

    out = {'level': call(ST + 'get_current_level', {}), 'dirty_after_save': call(AT + 'is_dirty', {'asset_path': L}),
           'actors_total': len(find())}
    for t in ('MUS', 'MUS_Shell', 'MUS_Door', 'MUS_Stair', 'MUS_Glass', 'MUS_StandIn', 'MUS_Hero', 'ENV_StatuePivot', 'ENV_FlickerReady',
              'ENV_PatrolWaypoint', 'ENV_ZoneBoundary', 'ENV_ProgressionGate', 'ENV_DoorAnchor', 'ENV_SpawnCandidate',
              'ENV_Task_Inspect', 'ENV_Task_Clean', 'ENV_Task_Maintenance', 'ENV_Task_Disturbance'):
        out['tag_' + t] = len(find(tag=t))
    for c in ('SpotLight', 'PointLight', 'StaticMeshActor', 'SkeletalMeshActor', 'TargetPoint', 'TriggerBox', 'PlayerStart',
              'NavMeshBoundsVolume', 'PostProcessVolume'):
        out['cls_' + c] = len(find(cls='/Script/' + ('NavigationSystem.' if c == 'NavMeshBoundsVolume' else 'Engine.') + c))
    # Tasks available per stage (each task marker carries a StageN tag).
    out['tasks_by_stage'] = {s: len([a for a in find(tag='ENV_Task') if 'Stage%d' % s in call(AC + 'get_tags', {'actor': a})]) for s in range(1, 6)}
    # Instanced arrays: count and any instance left at the origin (the PerInstanceSMData growth trap).
    bad = []
    n_inst = 0
    for a in find(cls='/Script/Engine.Actor'):
        for comp in call(AC + 'get_components', {'actor': a, 'component_type': {'refPath': '/Script/Engine.InstancedStaticMeshComponent'}}):
            d = json.loads(call(OT + 'get_properties', {'instance': comp, 'properties': ['PerInstanceSMData']}))['PerInstanceSMData']
            n_inst += len(d)
            bad += [comp['refPath'].split('.')[-1] for e in d if abs(e['transform']['wPlane']['x']) < 1 and abs(e['transform']['wPlane']['y']) < 1]
    out['instances_total'] = n_inst
    out['instances_at_origin'] = bad
    out['recast'] = len(find('RecastNavMesh'))
    return out
