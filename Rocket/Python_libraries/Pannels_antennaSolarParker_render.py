import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from trimesh.creation import torus


FUSELAGE_LENGTH = 20.0
FUSELAGE_RADIUS = 1.35

#def create_fuselage():
 #   fuselage = trimesh.creation.cylinder(radius=FUSELAGE_RADIUS, height=FUSELAGE_LENGTH)
  #  fuselage.apply_translation([0, 0, FUSELAGE_LENGTH / 2])
   # fuselage.visual.vertex_colors = [70, 130, 180, 255]  # Azul acero sólido
    #return fuselage
def create_advanced_fuselage():
    components = []

    # Cuerpo principal más grueso y compacto
    main_body = trimesh.creation.cylinder(radius=FUSELAGE_RADIUS + 0.3, height=FUSELAGE_LENGTH)
    main_body.apply_translation([0, 0, FUSELAGE_LENGTH / 2])
    main_body.visual.vertex_colors = [65, 105, 225, 255]  # Azul real
    components.append(main_body)

    # Anillos estructurales tipo refuerzo
    for z in np.linspace(2, FUSELAGE_LENGTH - 2, 5):
        ring = trimesh.creation.torus(FUSELAGE_RADIUS + 0.32, 0.05)
        ring.apply_translation([0, 0, z])
        ring.visual.vertex_colors = [105, 105, 105, 255]  # Gris oscuro
        components.append(ring)

    # Compartimentos cilíndricos externos
    for z in [5.0, 10.0, 15.0]:
        compartment = trimesh.creation.cylinder(radius=0.4, height=1.5)
        compartment.apply_translation([FUSELAGE_RADIUS + 0.6, 0, z])
        compartment.visual.vertex_colors = [139, 69, 19, 255]  # Marrón metálico
        components.append(compartment)

    # Revestimiento tipo kevlar o resina
    kevlar_layer = trimesh.creation.cylinder(radius=FUSELAGE_RADIUS + 0.4, height=FUSELAGE_LENGTH)
    kevlar_layer.apply_translation([0, 0, FUSELAGE_LENGTH / 2])
    kevlar_layer.visual.vertex_colors = [184, 134, 11, 90]  # Dorado translúcido (kevlar)
    components.append(kevlar_layer)

    # Escudos pequeños (rejillas planas como aletas adicionales)
    for i in range(3):
        fin = trimesh.creation.box(extents=[0.05, 1.2, 0.8])
        angle = i * (2 * np.pi / 3)
        x = np.cos(angle) * (FUSELAGE_RADIUS + 0.5)
        y = np.sin(angle) * (FUSELAGE_RADIUS + 0.5)
        fin.apply_translation([x, y, FUSELAGE_LENGTH / 2])
        fin.visual.vertex_colors = [169, 169, 169, 200]  # Gris medio translúcido
        components.append(fin)

    # Sensores adicionales
    for z in [4.0, 12.0]:
        sensor = trimesh.creation.icosphere(radius=0.2)
        sensor.apply_translation([0, -(FUSELAGE_RADIUS + 0.4), z])
        sensor.visual.vertex_colors = [255, 140, 0, 255]  # Naranja sólido
        components.append(sensor)

    return combine_meshes(components)


def create_nose_cone():
    cone = trimesh.creation.cone(radius=FUSELAGE_RADIUS * 0.9, height=3.2)
    cone.apply_translation([0, 0, FUSELAGE_LENGTH + 1.6])
    cone.visual.vertex_colors = [255, 215, 0, 255]  # Amarillo dorado sólido
    return cone

def create_escape_tower():
    tower = trimesh.creation.cylinder(radius=0.2, height=1.4)
    tower.apply_translation([0, 0, FUSELAGE_LENGTH + 3.2])
    tower.visual.vertex_colors = [192, 192, 192, 220]  # Plata translúcido
    return tower

def create_propulsion_base():
    base = trimesh.creation.cone(radius=1.4, height=1.2)
    base.apply_translation([0, 0, -0.6])
    base.visual.vertex_colors = [105, 105, 105, 255]  # Gris oscuro
    return base

def create_thermal_shield():
    shield = trimesh.creation.cylinder(radius=2.6, height=0.6)
    shield.apply_translation([0, 0, FUSELAGE_LENGTH + 0.3])
    shield.visual.vertex_colors = [255, 69, 0, 150]  # Rojo anaranjado translúcido
    return shield

def create_reinforced_heat_shield_layers():
    layers = []
    radii = [2.7, 2.9, 3.1]
    heights = [0.15, 0.15, 0.15]
    colors = [[255, 140, 0, 120], [255, 69, 0, 100], [178, 34, 34, 80]]  # Naranjas y rojos translúcidos
    z_pos = FUSELAGE_LENGTH + 0.6
    for r, h, c in zip(radii, heights, colors):
        layer = trimesh.creation.cylinder(radius=r, height=h)
        layer.apply_translation([0, 0, z_pos])
        layer.visual.vertex_colors = c
        layers.append(layer)
        z_pos += h
    return layers

def create_detailed_merlin_engine(position):
    chamber = trimesh.creation.cylinder(radius=0.15, height=0.4)
    chamber.apply_translation([0, 0, 0.2])
    chamber.visual.vertex_colors = [220, 220, 220, 255]  # Gris claro

    nozzle = trimesh.creation.cone(radius=0.25, height=0.6)
    nozzle.apply_translation([0, 0, -0.3])
    nozzle.visual.vertex_colors = [169, 169, 169, 255]  # Gris medio

    engine = combine_meshes([chamber, nozzle])
    engine.apply_translation(position)
    return engine

def create_merlin_engine_array():
    engines = []
    pattern = [(np.cos(a) * 0.75, np.sin(a) * 0.75) for a in np.linspace(0, 2*np.pi, 8, endpoint=False)]
    pattern.append((0, 0))  # motor central
    for x, y in pattern:
        engines.append(create_detailed_merlin_engine([x, y, -1.5]))
    return engines

def create_solar_panels():
    panels = []
    width, height, depth = 5.0, 1.5, 0.1
    panel1 = trimesh.creation.box(extents=[width, depth, height])
    panel1.apply_translation([-3.2, 0, FUSELAGE_LENGTH * 0.4])
    panel1.visual.vertex_colors = [30, 144, 255, 180]  # Azul dodger, translúcido
    panel2 = panel1.copy()
    panel2.apply_translation([6.4, 0, 0])  # mover a la derecha
    panels.extend([panel1, panel2])
    return panels

def create_solar_panel_frames():
    frames = []
    width, height, depth = 5.1, 0.12, 1.6
    frame1 = trimesh.creation.box(extents=[width, height, depth])
    frame1.apply_translation([-3.2, 0, FUSELAGE_LENGTH * 0.4])
    frame1.visual.vertex_colors = [169, 169, 169, 255]  # Gris oscuro marco

    frame2 = frame1.copy()
    frame2.apply_translation([6.4, 0, 0])
    frames.extend([frame1, frame2])
    return frames

def create_radiator_panels():
    radiators = []
    width, height, depth = 3.0, 0.05, 1.0
    positions = [[2.5, 0, FUSELAGE_LENGTH * 0.7], [-2.5, 0, FUSELAGE_LENGTH * 0.7]]
    for pos in positions:
        panel = trimesh.creation.box(extents=[width, height, depth])
        panel.apply_translation(pos)
        panel.visual.vertex_colors = [70, 70, 70, 180]  # Gris oscuro translúcido
        radiators.append(panel)
    return radiators

def create_sensors():
    sensors = []
    # Dos sensores tipo esfera pequeños a ambos lados del fuselaje cerca de la parte superior
    positions = [[1.1, 0, FUSELAGE_LENGTH - 2], [-1.1, 0, FUSELAGE_LENGTH - 2]]
    for pos in positions:
        sensor = trimesh.creation.icosphere(radius=0.15)
        sensor.apply_translation(pos)
        sensor.visual.vertex_colors = [255, 140, 0, 200]  # Naranja translúcido
        sensors.append(sensor)
    return sensors

def create_antenna_array():
    antennas = []
    for pos in [[0.4, 0.4, FUSELAGE_LENGTH - 0.8], [-0.4, -0.4, FUSELAGE_LENGTH - 0.8]]:
        mast = trimesh.creation.cylinder(radius=0.05, height=1.3)
        mast.apply_translation([pos[0], pos[1], pos[2] + 0.65])
        mast.visual.vertex_colors = [255, 255, 224, 255]  # Amarillo pálido
        antennas.append(mast)
    return antennas

def create_scientific_module():
    module = trimesh.creation.cylinder(radius=1.0, height=0.4)
    module.apply_translation([0, 0, FUSELAGE_LENGTH * 0.2])
    module.visual.vertex_colors = [0, 191, 255, 255]  # Azul profundo
    return module

def create_payload_module():
    box = trimesh.creation.box(extents=[2.5, 2.5, 1.2])
    box.apply_translation([0, 0, FUSELAGE_LENGTH * 0.3])
    box.visual.vertex_colors = [160, 82, 45, 255]  # Marrón oscuro
    return box

def create_landing_legs():
    legs = []
    angles = [np.pi / 4, 3 * np.pi / 4, -np.pi / 4, -3 * np.pi / 4]
    for angle in angles:
        x = np.cos(angle) * 1.8
        y = np.sin(angle) * 1.8
        leg = trimesh.creation.box(extents=[0.1, 0.1, 2.0])
        leg.apply_translation([x, y, -1.0])
        tilt = trimesh.transformations.rotation_matrix(np.radians(35), [1, 0, 0], point=[x, y, -1.0])
        leg.apply_transform(tilt)
        leg.visual.vertex_colors = [128, 128, 128, 255]  # Gris medio
        legs.append(leg)
    return legs

def create_robotic_arm():
    arm_base = trimesh.creation.cylinder(radius=0.1, height=0.4)
    arm_base.visual.vertex_colors = [139, 69, 19, 255]  # Marrón oscuro
    arm = trimesh.creation.box(extents=[0.1, 1.2, 0.1])
    arm.apply_translation([0, 0.6, 0])
    arm.visual.vertex_colors = [160, 82, 45, 255]  # Marrón claro
    robotic = combine_meshes([arm_base, arm])
    robotic.apply_translation([1.6, 0, FUSELAGE_LENGTH * 0.7])
    return robotic

def create_spine_structure():
    spine = trimesh.creation.cylinder(radius=0.08, height=FUSELAGE_LENGTH * 0.8)
    spine.apply_translation([0, 0, FUSELAGE_LENGTH * 0.4])
    spine.visual.vertex_colors = [105, 105, 105, 255]  # Gris oscuro
    return spine

def create_dome():
    dome = trimesh.creation.icosphere(subdivisions=3, radius=1.2)
    dome.apply_scale([1.1, 1.1, 0.5])
    dome.apply_translation([0, 0, FUSELAGE_LENGTH + 2.6])
    dome.visual.vertex_colors = [135, 206, 250, 180]  # Azul cielo translúcido
    return dome

def combine_meshes(meshes):
    return trimesh.util.concatenate(meshes)

# Blindaje hexagonal
def create_hex_panel(radius=0.5, thickness=0.1):
    angle = np.pi / 3
    points = np.array([[np.cos(i*angle), np.sin(i*angle), 0] for i in range(6)])
    vertices = np.vstack([points, points + [0, 0, thickness]])

    faces = []

    # Caras laterales (cuadriláteros divididos en 2 triángulos)
    for i in range(6):
        next_i = (i + 1) % 6
        # Triángulos para cara lateral
        faces.append([i, next_i, next_i + 6])
        faces.append([i, next_i + 6, i + 6])

    # Tapas superior e inferior trianguladas
    # Base inferior triangulada en triángulos fan
    for i in range(1, 5):
        faces.append([0, i, i + 1])
    # Último triángulo para cerrar tapa inferior
    faces.append([0, 5, 1])

    # Tapa superior triangulada (vertices 6 a 11)
    for i in range(7, 11):
        faces.append([6, i, i + 1])
    faces.append([6, 11, 7])

    hex_mesh = trimesh.Trimesh(vertices=vertices, faces=faces, process=False)
    return hex_mesh


def create_hex_shield_layer(z_height, radius=3.3, panel_spacing=0.05):
    panels = []
    # Distribuir hexágonos en una rejilla circular sobre el plano XY
    step = 2 * radius / 7
    x_vals = np.arange(-radius, radius + step, step)
    y_vals = np.arange(-radius, radius + step, step * np.sqrt(3)/2)

    for i, y in enumerate(y_vals):
        offset = 0 if i % 2 == 0 else step / 2
        for x in x_vals:
            pos_x = x + offset
            if pos_x**2 + y**2 <= radius**2:
                panel = create_hex_panel()
                panel.apply_translation([pos_x, y, z_height])
                panel.visual.vertex_colors = [255, 140, 0, 160]  # naranja translúcido
                panels.append(panel)
    return panels

def create_ion_propulsion_system():
    parts = []

    # Base cónica ya creada (la puedes llamar desde create_propulsion_base)

    # Añadimos un anillo anular alrededor de la base
    ring_outer = trimesh.creation.cylinder(radius=1.5, height=0.2)
    ring_outer.apply_translation([0, 0, -0.7])
    ring_outer.visual.vertex_colors = [80, 80, 90, 255]  # Gris azulado

    ring_inner = trimesh.creation.cylinder(radius=1.2, height=0.2)
    ring_inner.apply_translation([0, 0, -0.7])
    ring_inner.visual.vertex_colors = [0, 0, 0, 0]  # Hacemos "hueco" (transparente)

    # Para “restar” el interior, haría falta boolean, pero para simplicidad:
    # Solo pondremos dos cilindros superpuestos, visualmente parecido.

    parts.append(ring_outer)
    parts.append(ring_inner)

    # Añadimos varios pequeños motores iónicos (conos pequeños) alrededor
    num_thrusters = 6
    radius_thruster_circle = 1.3
    for i in range(num_thrusters):
        angle = 2 * np.pi * i / num_thrusters
        x = np.cos(angle) * radius_thruster_circle
        y = np.sin(angle) * radius_thruster_circle
        thruster = trimesh.creation.cone(radius=0.1, height=0.3)
        thruster.apply_translation([x, y, -1.2])
        thruster.visual.vertex_colors = [100, 149, 237, 255]  # Azul acero claro
        parts.append(thruster)

    return combine_meshes(parts)

# Antena parabólica simple
def create_parabolic_antenna():
    # Parámetros
    radius = 1.2
    height = 0.6
    # Crear paraboloide simple con mesh de revolución (usamos cono a modo aproximado)
    cone = trimesh.creation.cone(radius=radius, height=height)
    cone.visual.vertex_colors = [211, 211, 211, 220]  # gris claro translúcido
    cone.apply_translation([0, 0, FUSELAGE_LENGTH * 0.9])
    # Añadir mástil de soporte
    mast = trimesh.creation.cylinder(radius=0.07, height=0.8)
    mast.visual.vertex_colors = [169, 169, 169, 255]  # gris medio
    mast.apply_translation([0, 0, FUSELAGE_LENGTH * 0.9 - 0.8])
    return [cone, mast]

def create_side_module(position, size=(1.2, 2.5, 1.0), color=[100, 100, 140, 255]):
    module = trimesh.creation.box(extents=size)
    module.apply_translation(position)
    module.visual.vertex_colors = color
    return module
side_modules = [
    create_side_module([FUSELAGE_RADIUS + 1.5, 0, 6]),
    create_side_module([-FUSELAGE_RADIUS - 1.5, 0, 8]),
    create_side_module([0, FUSELAGE_RADIUS + 1.2, 12], size=(1.5, 1.5, 0.8), color=[80, 80, 120, 255])
]


def create_extra_antennas():
    antennas = []
    antenna_positions = [
        [1.0, 1.0, FUSELAGE_LENGTH - 1.5],
        [-1.2, 1.5, FUSELAGE_LENGTH - 1.7],
        [1.5, -1.3, FUSELAGE_LENGTH - 2.2],
        [-1.4, -1.6, FUSELAGE_LENGTH - 2.5],
        [0, 0, FUSELAGE_LENGTH - 0.5]
    ]
    for pos in antenna_positions:
        mast = trimesh.creation.cylinder(radius=0.03, height=1.0)
        mast.apply_translation([pos[0], pos[1], pos[2] + 0.5])
        mast.visual.vertex_colors = [220, 220, 220, 200]
        antennas.append(mast)

        tip = trimesh.creation.icosphere(radius=0.06)
        tip.apply_translation(pos)
        tip.visual.vertex_colors = [200, 200, 255, 230]
        antennas.append(tip)
    return antennas
def create_warp_propulsor_complex(position, main_radius=0.8, length=3.5):
    components = []
    # Capa exterior
    outer_cyl = trimesh.creation.cylinder(radius=main_radius + 0.15, height=length)
    outer_cyl.apply_translation([0, 0, length/2])
    outer_cyl.visual.vertex_colors = [50, 50, 80, 180]

    # Capa interior
    inner_cyl = trimesh.creation.cylinder(radius=main_radius, height=length * 0.95)
    inner_cyl.apply_translation([0, 0, length/2 + 0.1])
    inner_cyl.visual.vertex_colors = [80, 80, 140, 220]

    # Estructura tubular radial (8 tubos)
    for i in range(8):
        angle = 2 * np.pi * i / 8
        tube = trimesh.creation.cylinder(radius=0.05, height=length)
        # Posicionar tubo en círculo alrededor del eje Z
        x = np.cos(angle) * (main_radius + 0.2)
        y = np.sin(angle) * (main_radius + 0.2)
        tube.apply_translation([x, y, length/2])
        tube.visual.vertex_colors = [150, 150, 200, 200]
        components.append(tube)

    components.extend([outer_cyl, inner_cyl])
    warp_assembly = combine_meshes(components)
    warp_assembly.apply_translation(position)
    return warp_assembly

def create_surface_panel(position, size=(1.0, 0.05, 0.7), color=[100, 100, 150, 200]):
    panel = trimesh.creation.box(extents=size)
    panel.apply_translation(position)
    panel.visual.vertex_colors = color
    return panel
surface_panels = []
for z in np.linspace(3, FUSELAGE_LENGTH - 3, 6):
    surface_panels.append(create_surface_panel([0, FUSELAGE_RADIUS + 0.25, z]))
    surface_panels.append(create_surface_panel([0, -FUSELAGE_RADIUS - 0.25, z]))

def create_docking_node():
    node = trimesh.creation.icosphere(radius=0.8)
    node.visual.vertex_colors = [200, 200, 220, 255]
    node.apply_translation([0, 0, FUSELAGE_LENGTH * 0.6])

    # Seis puertos tipo túnel
    tunnels = []
    directions = [
        [1.8, 0, 0], [-1.8, 0, 0], [0, 1.8, 0], [0, -1.8, 0],
        [0, 0, 1.8], [0, 0, -1.8]
    ]
    for d in directions:
        tunnel = trimesh.creation.cylinder(radius=0.35, height=1.8)
        tunnel.visual.vertex_colors = [169, 169, 169, 255]
        tunnel.apply_translation([d[0] / 2, d[1] / 2, d[2] / 2])
        if d[0]:
            tunnel.apply_transform(trimesh.transformations.rotation_matrix(np.pi / 2, [0, 1, 0]))
        elif d[1]:
            tunnel.apply_transform(trimesh.transformations.rotation_matrix(np.pi / 2, [1, 0, 0]))
        tunnels.append(tunnel)

    return combine_meshes([node] + tunnels)

def create_lab_module(position, color=[0, 128, 255, 255]):
    lab = trimesh.creation.box(extents=[2.4, 2.4, 3.5])
    lab.apply_translation(position)
    lab.visual.vertex_colors = color
    return lab

def create_cupola_module():
    base = trimesh.creation.cylinder(radius=0.8, height=0.2)
    dome = trimesh.creation.icosphere(subdivisions=2, radius=0.9)
    dome.apply_translation([0, 0, 0.5])
    dome.visual.vertex_colors = [135, 206, 250, 180]
    cupola = combine_meshes([base, dome])
    cupola.apply_translation([0, 0, FUSELAGE_LENGTH * 0.95])
    return cupola

def create_control_moment_gyros():
    gyros = []
    for angle in np.linspace(0, 2*np.pi, 3, endpoint=False):
        base = trimesh.creation.cylinder(radius=0.25, height=0.2)
        x = np.cos(angle) * 2.2
        y = np.sin(angle) * 2.2
        base.apply_translation([x, y, FUSELAGE_LENGTH * 0.6])
        base.visual.vertex_colors = [105, 105, 105, 255]
        gyros.append(base)
    return gyros

def create_escape_capsule(position):
    capsule = trimesh.creation.icosphere(subdivisions=3, radius=1.0)
    capsule.apply_scale([1.5, 1.5, 2.4])  # Esto lo estira como un elipsoide
    capsule.apply_translation(position)
    capsule.visual.vertex_colors = [139, 0, 0, 255]  # Rojo oscuro
    return capsule



# --- Función combine_meshes y plot_mesh ya definidas por ti ---
def plot_mesh(mesh, filename="Falcon_Parker_Advanced_Enhanced_2.png"):
    fig = plt.figure(figsize=(14, 14))
    ax = fig.add_subplot(111, projection='3d')

    faces = mesh.faces
    vertices = mesh.vertices

    # Normalizar colores de las caras si existen
    face_colors = mesh.visual.face_colors / 255.0 if hasattr(mesh.visual, 'face_colors') else (0.2, 0.4, 0.6, 0.9)

    collection = Poly3DCollection(vertices[faces], alpha=0.9, linewidths=0.7, edgecolors=(0.1, 0.1, 0.1, 0.8))
    collection.set_facecolor(face_colors)
    ax.add_collection3d(collection)

    bounds = mesh.bounds
    margin = 3
    ax.set_xlim(bounds[0][0] - margin, bounds[1][0] + margin)
    ax.set_ylim(bounds[0][1] - margin, bounds[1][1] + margin)
    ax.set_zlim(bounds[0][2] - margin, bounds[1][2] + margin)

    ax.set_axis_off()
    ax.view_init(elev=35, azim=40)

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"Imagen renderizada guardada como: {filename}")

def main():
    components = [
        create_advanced_fuselage(),
        create_nose_cone(),
        create_escape_tower(),
        create_propulsion_base(),
        create_thermal_shield(),
        *create_reinforced_heat_shield_layers(),
        create_spine_structure(),
        create_scientific_module(),
        *create_merlin_engine_array(),
        *create_solar_panels(),
        *create_solar_panel_frames(),
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

        # Nuevos compartimentos laterales
        *side_modules,

        # Antenas extra
        *create_extra_antennas(),

        # Warp propulsores dobles
        create_warp_propulsor_complex([FUSELAGE_RADIUS + 2.5, 0, 6]),
        create_warp_propulsor_complex([-FUSELAGE_RADIUS - 2.5, 0, 6]),

        # Paneles superficie
        *surface_panels,
        create_docking_node(),
        create_lab_module([3.5, 0, FUSELAGE_LENGTH * 0.6]),
        create_lab_module([-3.5, 0, FUSELAGE_LENGTH * 0.6], color=[0, 100, 180, 255]),
        create_cupola_module(),
        *create_control_moment_gyros(),
        create_escape_capsule([0, -3.0, 2]),
        create_escape_capsule([0, 3.0, 2])

    ]

    model = combine_meshes(components)
    plot_mesh(model, filename="falcon_parker_star_trek_loaded_v1.png")
    model.export('falcon_parker_star_trek_loaded_v1.stl')
    print("Modelo exportado a falcon_parker_star_trek_loaded_v1.stl, versión cargada Trek")

if __name__ == "__main__":
    main()
