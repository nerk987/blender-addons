import bpy


def create_widget(name):
    """Create an empty widget object and return the object"""
    prefs = bpy.context.preferences.addons["add_camera_rigs"].preferences
    widget_prefix = prefs.widget_prefix
    obj_name = widget_prefix + name
    scene = bpy.context.scene

    obj = bpy.data.objects.get(obj_name)

    if obj is None:
        mesh = bpy.data.meshes.new(obj_name)
        obj = bpy.data.objects.new(obj_name, mesh)

        # Create a new collection for the widgets
        collection_name = prefs.camera_widget_collection_name
        coll = bpy.data.collections.get(collection_name)
        if coll is None:
            coll = bpy.data.collections.new(collection_name)
            scene.collection.children.link(coll)
            coll.hide_viewport = True
            coll.hide_render = True

        # Link the collection
        coll.objects.link(obj)

    return obj


def create_root_widget(name):
    """Create a compass-shaped widget"""
    obj = create_widget(name)
    if not obj.data.vertices:
        verts = [(0.6307649612426758, 0.6271349787712097, 0.0),
                 (0.3413670063018799, 0.8205029964447021, 0.0),
                 (0.0, 0.8884050250053406, 0.0),
                 (-0.3413670063018799, 0.8205029964447021, 0.0),
                 (-0.6307649612426758, 0.6271349787712097, 0.0),
                 (-0.8241360187530518, 0.3377370238304138, 0.0),
                 (-0.8920379877090454, -0.003631560131907463, 0.0),
                 (0.8920379877090454, -0.003631379920989275, 0.0),
                 (0.824133038520813, 0.3377370238304138, 0.0),
                 (0.21458700299263, 1.5175920724868774, 0.0),
                 (-0.21458669006824493, 1.5175920724868774, 0.0),
                 (-0.21458700299263, 1.1372729539871216, 0.0),
                 (0.21458700299263, 1.1372729539871216, 0.0),
                 (-0.3977609872817993, 1.5175920724868774, 0.0),
                 (0.3977609872817993, 1.5175920724868774, 0.0),
                 (0.0, 2.002802848815918, 0.0),
                 (-0.8241360187530518, -0.3449999988079071, 0.0),
                 (0.8241360187530518, -0.3449999988079071, 0.0),
                 (0.6307649612426758, -0.6343979835510254, 0.0),
                 (0.3413670063018799, -0.8277660012245178, 0.0),
                 (0.0, -0.8956680297851562, 0.0),
                 (-0.3413670063018799, -0.8277660012245178, 0.0),
                 (-0.6307649612426758, -0.6343979835510254, 0.0),
                 (-2.0064330101013184, -0.003630870021879673, 0.0),
                 (-1.5212249755859375, 0.39413100481033325, 0.0),
                 (-1.5212249755859375, -0.4013940095901489, 0.0),
                 (-1.1409029960632324, 0.21095609664916992, 0.0),
                 (-1.1409029960632324, -0.2182179093360901, 0.0),
                 (-1.5212249755859375, -0.2182179093360901, 0.0),
                 (-1.5212249755859375, 0.21095609664916992, 0.0),
                 (1.5212249755859375, -0.2182179093360901, 0.0),
                 (1.5212249755859375, 0.21095609664916992, 0.0),
                 (1.1409029960632324, 0.21095609664916992, 0.0),
                 (1.1409029960632324, -0.2182179093360901, 0.0),
                 (1.5212249755859375, 0.39413100481033325, 0.0),
                 (1.5212249755859375, -0.4013940095901489, 0.0),
                 (2.0064330101013184, -0.0036309000570327044, 0.0),
                 (0.0, -2.0100629329681396, 0.0),
                 (-0.3977609872817993, -1.5248548984527588, 0.0),
                 (0.3977609872817993, -1.5248548984527588, 0.0),
                 (-0.21458669006824493, -1.144536018371582, 0.0),
                 (0.21458730101585388, -1.144536018371582, 0.0),
                 (0.21458730101585388, -1.5248548984527588, 0.0),
                 (-0.21458669006824493, -1.5248548984527588, 0.0)]

        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (7, 8), (0, 8),
                 (10, 11), (9, 12), (11, 12), (10, 13), (9, 14), (13, 15), (14, 15),
                 (16, 22), (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (7, 17),
                 (6, 16), (23, 24), (23, 25), (24, 29), (25, 28), (26, 27), (26, 29),
                 (27, 28), (31, 32), (30, 33), (32, 33), (31, 34), (30, 35), (34, 36),
                 (35, 36), (37, 38), (37, 39), (38, 43), (39, 42), (40, 41), (40, 43),
                 (41, 42)]

        mesh = obj.data
        mesh.from_pydata(verts, edges, [])
        mesh.update()
    return obj


def create_camera_widget(name):
    """Create a camera control widget"""
    obj = create_widget(name)
    if not obj.data.vertices:
        verts = [(0.27513638138771057, 0.0, -0.27513638138771057),
                 (0.359483003616333, 0.0, -0.14890272915363312),
                 (0.38910162448883057, 0.0, 0.0),
                 (0.359483003616333, 0.0, 0.1489027738571167),
                 (0.27513638138771057, 0.0, 0.27513638138771057),
                 (0.1489027589559555, 0.0, 0.359483003616333),
                 (-1.9481809943044937e-07, 0.0, 0.38910162448883057),
                 (-1.175054293867106e-07, 0.0, -0.38910162448883057),
                 (0.148903027176857, 0.0, -0.35948291420936584),
                 (0.6635494828224182, 0.0, -0.09360162913799286),
                 (0.6635494828224182, 0.0, 0.09360162913799286),
                 (0.49765610694885254, 0.0, 0.09360162913799286),
                 (0.49765610694885254, 0.0, -0.09360168874263763),
                 (0.6635494828224182, 0.0, 0.17350149154663086),
                 (0.6635494828224182, 0.0, -0.17350149154663086),
                 (0.8751950263977051, 0.0, 0.0),
                 (-0.14890296757221222, 0.0, 0.35948291420936584),
                 (-0.14890283346176147, 0.0, -0.359483003616333),
                 (-0.27513641119003296, 0.0, -0.2751363217830658),
                 (-0.359483003616333, 0.0, -0.14890272915363312),
                 (-0.38910162448883057, 0.0, 0.0),
                 (-0.359483003616333, 0.0, 0.1489028036594391),
                 (-0.2751363217830658, 0.0, 0.27513641119003296),
                 (1.0342557033027333e-07, 0.0, 0.8751950263977051),
                 (0.17350155115127563, 0.0, 0.6635494828224182),
                 (-0.17350146174430847, 0.0, 0.6635494828224182),
                 (0.09360174089670181, 0.0, 0.49765610694885254),
                 (-0.09360159188508987, 0.0, 0.49765610694885254),
                 (-0.09360159188508987, 0.0, 0.6635494828224182),
                 (0.09360168874263763, 0.0, 0.6635494828224182),
                 (-0.0936015248298645, 0.0, -0.6635494828224182),
                 (0.09360174834728241, 0.0, -0.6635494828224182),
                 (0.09360172599554062, 0.0, -0.49765610694885254),
                 (-0.09360159933567047, 0.0, -0.49765610694885254),
                 (0.1735016107559204, 0.0, -0.6635494828224182),
                 (-0.1735014021396637, 0.0, -0.6635494828224182),
                 (9.422691960025986e-08, 0.0, -0.8751950263977051),
                 (-0.8751950263977051, 0.0, 0.0),
                 (-0.6635494828224182, 0.0, 0.17350131273269653),
                 (-0.6635494828224182, 0.0, -0.17350167036056519),
                 (-0.49765610694885254, 0.0, 0.0936015397310257),
                 (-0.49765610694885254, 0.0, -0.0936017706990242),
                 (-0.6635494828224182, 0.0, -0.09360179305076599),
                 (-0.6635494828224182, 0.0, 0.09360147267580032),
                 (-0.16527177393436432, 0.0, 0.1652718484401703),
                 (-0.21593798696994781, 0.0, 0.08944448828697205),
                 (-0.23372963070869446, 0.0, 0.0),
                 (-0.21593798696994781, 0.0, -0.08944445103406906),
                 (-0.1652718484401703, 0.0, -0.16527177393436432),
                 (-0.08944450318813324, 0.0, -0.21593798696994781),
                 (-0.0894445851445198, 0.0, 0.21593795716762543),
                 (0.0894446149468422, 0.0, -0.21593795716762543),
                 (-7.058439166485186e-08, 0.0, -0.23372963070869446),
                 (-1.1702535118729429e-07, 0.0, 0.23372963070869446),
                 (0.08944445848464966, 0.0, 0.21593798696994781),
                 (0.1652718037366867, 0.0, 0.1652718037366867),
                 (0.21593798696994781, 0.0, 0.08944446593523026),
                 (0.23372963070869446, 0.0, 0.0),
                 (0.21593798696994781, 0.0, -0.08944445848464966),
                 (0.1652718037366867, 0.0, -0.1652718037366867)]

        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (7, 8), (0, 8),
                 (10, 11), (9, 12), (11, 12), (10, 13), (9, 14), (13, 15), (14, 15),
                 (16, 22), (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (7, 17),
                 (6, 16), (23, 24), (23, 25), (24, 29), (25, 28), (26, 29), (27, 28),
                 (31, 32), (30, 33), (32, 33), (31, 34), (30, 35), (34, 36), (35, 36),
                 (37, 38), (37, 39), (38, 43), (39, 42), (40, 41), (40, 43), (41, 42),
                 (50, 53), (49, 52), (44, 45), (45, 46), (46, 47), (47, 48), (48, 49),
                 (44, 50), (51, 59), (51, 52), (53, 54), (54, 55), (55, 56), (56, 57),
                 (57, 58), (58, 59), (27, 26)]

        mesh = obj.data
        mesh.from_pydata(verts, edges, [])
        mesh.update()
    return obj


def create_aim_widget(name):
    """Create a camera aim widget"""
    obj = create_widget(name)
    if not obj.data.vertices:
        verts = [(0.31008288264274597, 0.0, 0.31008288264274597),
                 (0.40514281392097473, 0.0, 0.1678156554698944),
                 (0.43852344155311584, 0.0, 0.0),
                 (0.40514281392097473, 0.0, -0.1678156852722168),
                 (0.31008288264274597, 0.0, -0.31008288264274597),
                 (0.1678156703710556, 0.0, -0.40514281392097473),
                 (-2.1956294915526087e-07, 0.0, -0.43852344155311584),
                 (-1.3243040086763358e-07, 0.0, 0.43852344155311584),
                 (0.16781596839427948, 0.0, 0.4051426947116852),
                 (0.7993937134742737, 0.0, 0.10549049079418182),
                 (0.7993937134742737, 0.0, -0.10549048334360123),
                 (0.9863580465316772, 0.0, -0.10549048334360123),
                 (0.9863580465316772, 0.0, 0.105490542948246),
                 (0.7993937134742737, 0.0, -0.19553886353969574),
                 (0.7993937134742737, 0.0, 0.19553886353969574),
                 (0.5608659386634827, 0.0, 0.0),
                 (-0.1678159236907959, 0.0, -0.4051426947116852),
                 (-0.16781575977802277, 0.0, 0.40514281392097473),
                 (-0.31008294224739075, 0.0, 0.3100828230381012),
                 (-0.40514281392097473, 0.0, 0.16781564056873322),
                 (-0.43852344155311584, 0.0, 0.0),
                 (-0.40514281392097473, 0.0, -0.16781572997570038),
                 (-0.3100828230381012, 0.0, -0.31008294224739075),
                 (5.8281088399780856e-08, 0.0, 0.5608659982681274),
                 (-0.19553889334201813, 0.0, 0.7993938326835632),
                 (0.1955389529466629, 0.0, 0.7993938326835632),
                 (-0.10549052804708481, 0.0, 0.9863581657409668),
                 (0.10549058020114899, 0.0, 0.9863581657409668),
                 (0.10549052804708481, 0.0, 0.7993938326835632),
                 (-0.10549046844244003, 0.0, 0.7993938326835632),
                 (0.10549034923315048, 0.0, -0.7993939518928528),
                 (-0.10549066960811615, 0.0, -0.7993939518928528),
                 (-0.10549074411392212, 0.0, -0.9863584041595459),
                 (0.10549039393663406, 0.0, -0.9863584041595459),
                 (-0.19553910195827484, 0.0, -0.7993938326835632),
                 (0.19553880393505096, 0.0, -0.7993940711021423),
                 (-1.4296951178494055e-07, 0.0, -0.5608659982681274),
                 (-0.5608660578727722, 0.0, 0.0),
                 (-0.7993939518928528, 0.0, -0.19553877413272858),
                 (-0.7993937134742737, 0.0, 0.19553901255130768),
                 (-0.9863580465316772, 0.0, -0.10549040883779526),
                 (-0.9863580465316772, 0.0, 0.10549063980579376),
                 (-0.7993938326835632, 0.0, 0.10549062490463257),
                 (-0.7993938326835632, 0.0, -0.10549038648605347),
                 (-0.12803608179092407, 0.0, -0.12803612649440765),
                 (-0.167287215590477, 0.0, -0.06929267197847366),
                 (-0.18107034265995026, 0.0, 0.0),
                 (-0.167287215590477, 0.0, 0.06929262727499008),
                 (-0.12803612649440765, 0.0, 0.12803608179092407),
                 (-0.06929267197847366, 0.0, 0.167287215590477),
                 (-0.06929274648427963, 0.0, -0.1672871708869934),
                 (0.06929276883602142, 0.0, 0.1672871708869934),
                 (-5.468173824851874e-08, 0.0, 0.18107034265995026),
                 (-9.065958295195742e-08, 0.0, -0.18107034265995026),
                 (0.06929264962673187, 0.0, -0.167287215590477),
                 (0.12803609669208527, 0.0, -0.12803609669208527),
                 (0.167287215590477, 0.0, -0.06929264962673187),
                 (0.18107034265995026, 0.0, 0.0),
                 (0.167287215590477, 0.0, 0.06929264217615128),
                 (0.12803609669208527, 0.0, 0.12803609669208527),
                 (-6.667435314966497e-08, 0.0, 0.060356780886650085),
                 (-7.866697160352487e-08, 0.0, -0.060356780886650085),
                 (-0.060356780886650085, 0.0, 0.0),
                 (0.060356780886650085, 0.0, 0.0)]

        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (7, 8), (0, 8),
                 (10, 11), (9, 12), (11, 12), (10, 13), (9, 14), (13, 15), (14, 15),
                 (16, 22), (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (7, 17),
                 (6, 16), (23, 24), (23, 25), (24, 29), (25, 28), (26, 29), (27, 28),
                 (31, 32), (30, 33), (32, 33), (31, 34), (30, 35), (34, 36), (35, 36),
                 (37, 38), (37, 39), (38, 43), (39, 42), (40, 41), (40, 43), (41, 42),
                 (50, 53), (49, 52), (44, 45), (45, 46), (46, 47), (47, 48), (48, 49),
                 (44, 50), (51, 59), (51, 52), (53, 54), (54, 55), (55, 56), (56, 57),
                 (57, 58), (58, 59), (27, 26), (60, 61), (62, 63)]

        mesh = obj.data
        mesh.from_pydata(verts, edges, [])
        mesh.update()
    return obj
