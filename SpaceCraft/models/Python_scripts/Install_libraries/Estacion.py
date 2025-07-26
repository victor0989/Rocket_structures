import trimesh
import numpy as np

FUSELAGE_RADIUS = 2.0
FUSELAGE_LENGTH = 18.0

def combine_meshes(mesh_list):
    combined = trimesh.util.concatenate(mesh_list)
    return combined

# --- Función doblado suave ---
def bend_mesh_smooth(mesh, bend_angle=np.pi/6, bend_height=FUSELAGE_LENGTH/2):
    vertices = mesh.vertices.copy()
    for i, v in enumerate(vertices):
        if v[2] > bend_height:
            dz = v[2] - bend_height
            bend_fraction = dz / (FUSELAGE_LENGTH - bend_height)
            incremental_angle = bend_angle * bend_fraction
            x_new = v[0] * np.cos(incremental_angle) + v[2] * np.sin(incremental_angle)
            z_new = -v[0] * np.sin(incremental_angle) + v[2] * np.cos(incremental_angle)
            vertices[i] = [x_new, v[1], z_new]
    bent_mesh = trimesh.Trimesh(vertices=vertices, faces=mesh.faces, process=False)
    return bent_mesh

# --- Fuselaje avanzado sin colores ---
def create_advanced_fuselage_v2():
    components = []

    main_body = trimesh.creation.cylinder(radius=FUSELAGE_RADIUS + 0.3, height=FUSELAGE_LENGTH)
    main_body.apply_translation([0, 0, FUSELAGE_LENGTH / 2])
    components.append(main_body)

    for z in np.linspace(2, FUSELAGE_LENGTH - 2, 5):
        ring = trimesh.creation.torus(FUSELAGE_RADIUS + 0.32, 0.05)
        ring.apply_translation([0, 0, z])
        components.append(ring)

    for z in [5.0, 10.0, 15.0]:
        compartment = trimesh.creation.cylinder(radius=0.4, height=1.5)
        compartment.apply_translation([FUSELAGE_RADIUS + 0.6, 0, z])
        components.append(compartment)

    kevlar_layer = trimesh.creation.cylinder(radius=FUSELAGE_RADIUS + 0.4, height=FUSELAGE_LENGTH)
    kevlar_layer.apply_translation([0, 0, FUSELAGE_LENGTH / 2])
    components.append(kevlar_layer)

    for i in range(3):
        fin = trimesh.creation.box(extents=[0.05, 1.2, 0.8])
        angle = i * (2 * np.pi / 3)
        x = np.cos(angle) * (FUSELAGE_RADIUS + 0.5)
        y = np.sin(angle) * (FUSELAGE_RADIUS + 0.5)
        fin.apply_translation([x, y, FUSELAGE_LENGTH / 2])
        components.append(fin)

    for z in [4.0, 12.0]:
        sensor = trimesh.creation.icosphere(radius=0.2)
        sensor.apply_translation([0, -(FUSELAGE_RADIUS + 0.4), z])
        components.append(sensor)

    return combine_meshes(components)

# --- Componentes adicionales v2 (sin colores) ---

def create_nose_cone_v2():
    cone = trimesh.creation.cone(radius=FUSELAGE_RADIUS * 0.9, height=3.2)
    cone.apply_translation([0, 0, FUSELAGE_LENGTH + 1.6])
    return cone

def create_escape_tower_v2():
    tower = trimesh.creation.cylinder(radius=0.2, height=1.4)
    tower.apply_translation([0, 0, FUSELAGE_LENGTH + 3.2])
    return tower

def create_propulsion_base_v2():
    base = trimesh.creation.cone(radius=1.4, height=1.2)
    base.apply_translation([0, 0, -0.6])
    return base

def create_thermal_shield_v2():
    shield = trimesh.creation.cylinder(radius=2.6, height=0.6)
    shield.apply_translation([0, 0, FUSELAGE_LENGTH + 0.3])
    return shield

def create_reinforced_heat_shield_layers_v2():
    layers = []
    radii = [2.7, 2.9, 3.1]
    heights = [0.15, 0.15, 0.15]
    z_pos = FUSELAGE_LENGTH + 0.6
    for r, h in zip(radii, heights):
        layer = trimesh.creation.cylinder(radius=r, height=h)
        layer.apply_translation([0, 0, z_pos])
        layers.append(layer)
        z_pos += h
    return layers

def create_merlin_engine_array_v2():
    engines = []
    positions = [(np.cos(a)*0.75, np.sin(a)*0.75) for a in np.linspace(0, 2*np.pi, 8, endpoint=False)]
    positions.append((0,0))
    for x, y in positions:
        chamber = trimesh.creation.cylinder(radius=0.15, height=0.4)
        chamber.apply_translation([0, 0, 0.2])
        nozzle = trimesh.creation.cone(radius=0.25, height=0.6)
        nozzle.apply_translation([0, 0, -0.3])
        engine = combine_meshes([chamber, nozzle])
        engine.apply_translation([x, y, -1.5])
        engines.append(engine)
    return engines

def create_solar_panels_v2():
    panels = []
    width, height, depth = 5.0, 1.5, 0.1
    panel1 = trimesh.creation.box(extents=[width, depth, height])
    panel1.apply_translation([-3.2, 0, FUSELAGE_LENGTH * 0.4])
    panel2 = panel1.copy()
    panel2.apply_translation([6.4, 0, 0])
    panels.extend([panel1, panel2])
    return panels

def create_solar_panel_frames_v2():
    frames = []
    width, height, depth = 5.1, 0.12, 1.6
    frame1 = trimesh.creation.box(extents=[width, height, depth])
    frame1.apply_translation([-3.2, 0, FUSELAGE_LENGTH * 0.4])
    frame2 = frame1.copy()
    frame2.apply_translation([6.4, 0, 0])
    frames.extend([frame1, frame2])
    return frames

# Para estas funciones, si no tienes versión _v2 específicas, debes hacerlas igual sin asignar colores.

# Placeholder para otras funciones sin colores
def create_spine_structure():
    # Aquí código sin colores (si tienes versión _v2, usa esa)
    return trimesh.creation.cylinder(radius=0.1, height=FUSELAGE_LENGTH)

def create_scientific_module():
    return trimesh.creation.box(extents=[2.0, 2.0, 2.0])

def create_radiator_panels():
    # Lista vacía si no está definida
    return []

def create_landing_legs():
    return []

def create_sensors():
    return []

def create_antenna_array():
    return []

def create_robotic_arm():
    return trimesh.creation.box(extents=[0.3, 0.3, 1.5])

def create_dome():
    dome = trimesh.creation.icosphere(radius=1.0)
    dome.apply_translation([0, 0, FUSELAGE_LENGTH * 0.5])
    return dome

def create_payload_module():
    return trimesh.creation.box(extents=[1.0, 1.0, 1.0])

def create_hex_shield_layer(z_pos, radius):
    # Por simplicidad, creamos un cilindro delgado como shield
    layer = trimesh.creation.cylinder(radius=radius, height=0.1)
    layer.apply_translation([0, 0, z_pos])
    return [layer]

def create_ion_propulsion_system():
    return trimesh.creation.cylinder(radius=0.4, height=1.0)

def create_parabolic_antenna():
    # Retornamos lista vacía si no implementado
    return []

side_modules = []  # Sin módulos laterales definidos
def create_extra_antennas():
    return []

def create_warp_propulsor_complex(pos):
    base = trimesh.creation.cylinder(radius=0.4, height=1.2)
    base.apply_translation(pos)
    return base

def create_surface_panels():
    return []

# --- Módulo Falcon Parker v2 ---
def create_falcon_parker_module_v2(offset=(0,0,0)):
    components = [
        create_advanced_fuselage_v2(),
        create_nose_cone_v2(),
        create_escape_tower_v2(),
        create_propulsion_base_v2(),
        create_thermal_shield_v2(),
        *create_reinforced_heat_shield_layers_v2(),
        create_spine_structure(),
        create_scientific_module(),
        *create_merlin_engine_array_v2(),
        *create_solar_panels_v2(),
        *create_solar_panel_frames_v2(),
        *create_radiator_panels(),
        *create_landing_legs(),
        *create_sensors(),
        *create_antenna_array(),
        create_robotic_arm(),
        create_dome(),
        create_payload_module(),
        *create_hex_shield_layer(FUSELAGE_LENGTH + 1.2, radius=3.3),
        *create_hex_shield_layer(FUSELAGE_LENGTH + 1.35, radius=3.3),
        create_ion_propulsion_system(),
        *create_parabolic_antenna(),
        *side_modules,
        *create_extra_antennas(),
        create_warp_propulsor_complex([FUSELAGE_RADIUS + 2.5, 0, 6]),
        create_warp_propulsor_complex([-FUSELAGE_RADIUS - 2.5, 0, 6]),
        *create_surface_panels(),
    ]
    module = combine_meshes(components)
    module.apply_translation(offset)
    return module

# --- Funciones para estación ---
def create_passage_tunnel(length=20, radius=0.6, position=(0,0,0)):
    tunnel = trimesh.creation.cylinder(radius=radius, height=length)
    tunnel.apply_translation(position)
    return tunnel

def create_structural_wrap(length=10, radius=0.5, count=6, position=(0,0,0), direction='x'):
    wraps = []
    for i in range(count):
        angle = 2 * np.pi * i / count
        x = np.cos(angle) * radius
        y = np.sin(angle) * radius
        bar = trimesh.creation.cylinder(radius=0.05, height=length)
        if direction == 'x':
            bar.apply_translation([0, 0, length/2])
            bar.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2, [0,1,0]))
        bar.apply_translation([x, y, position[2]])
        wraps.append(bar)
    return combine_meshes(wraps)

def create_star_trek_station_v2():
    pos1 = (-FUSELAGE_LENGTH * 0.6, 0, 0)
    pos2 = (FUSELAGE_LENGTH * 0.6, 0, 0)

    module1 = create_falcon_parker_module_v2(pos1)
    module2 = create_falcon_parker_module_v2(pos2)

    passage = create_passage_tunnel(length=FUSELAGE_LENGTH * 1.2, radius=0.6, position=(0,0,FUSELAGE_LENGTH*0.15))
    wrap_low = create_structural_wrap(length=FUSELAGE_LENGTH * 1.2, radius=0.4, count=6, position=(0,0,3), direction='x')
    wrap_mid = create_structural_wrap(length=FUSELAGE_LENGTH * 1.2, radius=0.5, count=8, position=(0,0,8), direction='x')
    wrap_high = create_structural_wrap(length=FUSELAGE_LENGTH * 1.2, radius=0.3, count=6, position=(0,0,12), direction='x')

    solar_panel = trimesh.creation.box(extents=[8, 0.2, 3])
    solar_panel.apply_translation((0, -FUSELAGE_RADIUS*2, FUSELAGE_LENGTH*0.6))

    antennas = []
    for i in range(5):
        antenna = trimesh.creation.cylinder(radius=0.08, height=2.5)
        angle = 2 * np.pi * i / 5
        x = np.cos(angle) * 1.5
        y = np.sin(angle) * 1.5
        antenna.apply_translation([x, y, FUSELAGE_LENGTH * 0.8])
        antennas.append(antenna)

    parts = [module1, module2, passage, wrap_low, wrap_mid, wrap_high, solar_panel] + antennas
    station = combine_meshes(parts)
    return station

# --- Función para mostrar o guardar ---
def plot_mesh(mesh, filename=None):
    try:
        import pyrender
        import trimesh.viewer
    except ImportError:
        print("Para visualizar necesitas instalar pyrender y trimesh[viewer].")
        return
    scene = pyrender.Scene()
    mesh = pyrender.Mesh.from_trimesh(mesh, smooth=False)
    scene.add(mesh)
    viewer = pyrender.Viewer(scene, use_raymond_lighting=True, run_in_thread=True)
    if filename:
        mesh.export(filename)

# --- Flujo principal ---
def main():
    # Crear fuselaje avanzado v2 y doblarlo suavemente
    fuselage = create_advanced_fuselage_v2()
    fuselage_bent = bend_mesh_smooth(fuselage, bend_angle=np.pi/6, bend_height=FUSELAGE_LENGTH/2)

    # Guardar fuselaje doblado si quieres
    fuselage_bent.export("fuselage_bent_v2.stl")

    # Crear y exportar estación Star Trek v2
    station = create_star_trek_station_v2()
    station.export("star_trek_station_v2.stl")

    print("Modelos generados y exportados: fuselage_bent_v2.stl y star_trek_station_v2.stl")

if __name__ == "__main__":
    main()
