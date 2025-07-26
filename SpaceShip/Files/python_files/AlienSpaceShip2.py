import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# la necesito menos alargada la nave mas ancha y menos alargada, mas grotesca y scify.
def combine_meshes(meshes):
    return trimesh.util.concatenate(meshes)

# Cuerpo principal, más grueso y de perfil bajo
def create_alien_fuselage():
    main_body = trimesh.creation.cylinder(radius=1.8, height=25)
    main_body.apply_translation([0, 0, 12.5])
    main_body.visual.vertex_colors = [50, 50, 50, 255]  # Gris oscuro mate
    return main_body

# Cápsulas laterales tipo bote de escape, grandes y robustas
def create_escape_capsules():
    capsules = []
    positions = [
        (2.6, 0, 7), (-2.6, 0, 7),
        (2.6, 0, 17), (-2.6, 0, 17)
    ]
    for pos in positions:
        capsule = trimesh.creation.cylinder(radius=0.6, height=4.5)
        capsule.apply_translation([pos[0], pos[1], pos[2]])
        capsule.visual.vertex_colors = [80, 80, 80, 255]  # Gris industrial
        capsules.append(capsule)
    return capsules

# Refuerzos tubulares cruzados al estilo industrial
def create_cross_tubes():
    tubes = []
    length = 26
    radius = 0.15
    for angle_deg in [0, 45, 90, 135]:
        tube = trimesh.creation.cylinder(radius=radius, height=length)
        tube.apply_translation([0, 0, length / 2])
        rot = trimesh.transformations.rotation_matrix(np.radians(angle_deg), [0, 0, 1])
        tube.apply_transform(rot)
        tube.visual.vertex_colors = [90, 90, 90, 255]  # Gris medio
        tubes.append(tube)
    return tubes

# Blindaje hexagonal translúcido naranja oscuro
def create_hex_shield_layer(z_height, radius=3.5):
    panels = []
    step = 2 * radius / 6
    x_vals = np.arange(-radius, radius + step, step)
    y_vals = np.arange(-radius, radius + step, step * np.sqrt(3)/2)

    for i, y in enumerate(y_vals):
        offset = 0 if i % 2 == 0 else step / 2
        for x in x_vals:
            pos_x = x + offset
            if pos_x**2 + y**2 <= radius**2:
                panel = create_hex_panel()
                panel.apply_translation([pos_x, y, z_height])
                panel.visual.vertex_colors = [255, 140, 0, 140]  # Naranja translúcido
                panels.append(panel)
    return panels

def create_hex_panel(radius=0.5, thickness=0.15):
    angle = np.pi / 3
    points = np.array([[np.cos(i*angle), np.sin(i*angle), 0] for i in range(6)]) * radius
    vertices = np.vstack([points, points + [0, 0, thickness]])
    faces = []
    for i in range(6):
        next_i = (i + 1) % 6
        faces.append([i, next_i, next_i + 6])
        faces.append([i, next_i + 6, i + 6])
    for i in range(1, 5):
        faces.append([0, i, i + 1])
    faces.append([0, 5, 1])
    for i in range(7, 11):
        faces.append([6, i, i + 1])
    faces.append([6, 11, 7])
    return trimesh.Trimesh(vertices=vertices, faces=faces, process=False)

# Cúpula tipo domo para la cabina, semi aplastada
def create_command_dome():
    dome = trimesh.creation.icosphere(subdivisions=3, radius=1.4)
    dome.apply_scale([1.2, 1.2, 0.6])
    dome.apply_translation([0, 0, 26])
    dome.visual.vertex_colors = [60, 60, 60, 200]  # Gris oscuro translúcido
    return dome

# Antenas robustas estilo industrial
def create_antennas():
    antennas = []
    base_z = 24
    for i in range(5):
        angle = 2 * np.pi * i / 5
        x = np.cos(angle) * 1.6
        y = np.sin(angle) * 1.6
        antenna = trimesh.creation.cylinder(radius=0.07, height=3)
        antenna.apply_translation([x, y, base_z + 1.5])
        antenna.visual.vertex_colors = [100, 100, 120, 230]
        antennas.append(antenna)
        tip = trimesh.creation.icosphere(radius=0.1)
        tip.apply_translation([x, y, base_z + 3])
        tip.visual.vertex_colors = [150, 150, 170, 200]
        antennas.append(tip)
    return antennas

# Paneles solares angulares, oscuros y pequeños
def create_solar_panels():
    panels = []
    panel_size = (3.5, 0.1, 1.2)
    positions = [(0, -2.4, 12), (0, 2.4, 12)]
    for pos in positions:
        panel = trimesh.creation.box(extents=panel_size)
        panel.apply_translation(pos)
        panel.visual.vertex_colors = [40, 40, 60, 170]
        panels.append(panel)
    return panels

# --- NUEVO: Sistema de propulsión trasero tipo VASIMR y turbinas ---

def create_vasimir_engine(position=[0,0,2], scale=1.0):
    parts = []

    # Cámara de combustión (cilindro rojo anaranjado)
    combustion = trimesh.creation.cylinder(radius=0.7 * scale, height=1.5 * scale)
    combustion.apply_translation([position[0], position[1], position[2]])
    combustion.visual.vertex_colors = [255, 69, 0, 220]  # Naranja intenso

    parts.append(combustion)

    # Tobera (cono invertido, azul metálico)
    nozzle = trimesh.creation.cone(radius=1.0 * scale, height=1.2 * scale)
    nozzle.apply_translation([position[0], position[1], position[2] - 1.2 * scale])
    nozzle.visual.vertex_colors = [30, 144, 255, 180]  # Azul intenso translúcido

    parts.append(nozzle)

    # Rejillas externas tubulares
    for angle_deg in [0, 90, 180, 270]:
        tube = trimesh.creation.cylinder(radius=0.1 * scale, height=1.7 * scale)
        tube.apply_translation([position[0], position[1], position[2] + 0.35 * scale])
        rot = trimesh.transformations.rotation_matrix(np.radians(angle_deg), [0, 0, 1])
        tube.apply_transform(rot)
        tube.visual.vertex_colors = [120, 120, 120, 200]
        parts.append(tube)

    return combine_meshes(parts)

def create_turbine_engine(position=[1.8,0,3], scale=1.0):
    parts = []

    # Cuerpo principal (cilindro gris metálico)
    body = trimesh.creation.cylinder(radius=0.5 * scale, height=3.5 * scale)
    body.apply_translation(position)
    body.visual.vertex_colors = [130, 130, 130, 255]

    parts.append(body)

    # Aspas (tres alas tipo hélice) - planos triangulares
    for i in range(3):
        blade = trimesh.creation.box(extents=[0.05 * scale, 1.2 * scale, 0.3 * scale])
        # rotar en el eje Z para distribuir en 120 grados
        rot_z = trimesh.transformations.rotation_matrix(np.radians(i*120), [0, 0, 1])
        blade.apply_transform(rot_z)
        # rotar para posicionar plano vertical
        rot_x = trimesh.transformations.rotation_matrix(np.radians(90), [1, 0, 0])
        blade.apply_transform(rot_x)
        # mover al centro del cuerpo de la turbina
        blade.apply_translation([position[0], position[1], position[2] + 1.75 * scale])
        blade.visual.vertex_colors = [70, 70, 70, 255]
        parts.append(blade)

    return combine_meshes(parts)

# --------- Función principal para crear nave con propulsión ----------

def create_alien_ship_with_engines():
    parts = []
    parts.append(create_alien_fuselage())
    parts.extend(create_escape_capsules())
    parts.extend(create_cross_tubes())
    parts.extend(create_hex_shield_layer(z_height=13))
    parts.append(create_command_dome())
    parts.extend(create_antennas())
    parts.extend(create_solar_panels())

    # Añadimos propulsores (2 VASIMR centrales y 2 turbinas laterales)
    vasimir_center = create_vasimir_engine(position=[0, 0, 1.5], scale=1.0)
    turbine_right = create_turbine_engine(position=[2.4, -1.0, 2.0], scale=0.8)
    turbine_left = create_turbine_engine(position=[-2.4, -1.0, 2.0], scale=0.8)

    parts.append(vasimir_center)
    parts.append(turbine_right)
    parts.append(turbine_left)

    return combine_meshes(parts)

def plot_mesh(mesh, filename="alien_ship_with_engines.png"):
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='3d')
    faces = mesh.faces
    vertices = mesh.vertices
    face_colors = mesh.visual.face_colors / 255.0 if hasattr(mesh.visual, 'face_colors') else (0.5, 0.5, 0.5, 1)
    collection = Poly3DCollection(vertices[faces], alpha=0.9, linewidths=0.5, edgecolors=(0, 0, 0, 0.5))
    collection.set_facecolor(face_colors)
    ax.add_collection3d(collection)
    bounds = mesh.bounds
    margin = 5
    ax.set_xlim(bounds[0][0]-margin, bounds[1][0]+margin)
    ax.set_ylim(bounds[0][1]-margin, bounds[1][1]+margin)
    ax.set_zlim(bounds[0][2]-margin, bounds[1][2]+margin)
    ax.set_axis_off()
    ax.view_init(elev=25, azim=45)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()
    print(f"Render guardado: {filename}")

if __name__ == "__main__":
    ship = create_alien_ship_with_engines()
    plot_mesh(ship)
    ship.export("alien_style_ship_with_engines.stl")
    print("Archivo STL exportado como alien_style_ship_with_engines.stl")
