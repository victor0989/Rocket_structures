import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def combine_meshes(meshes):
    return trimesh.util.concatenate(meshes)

# Cuerpo principal, más ancho y menos alto (menos alargado)
def create_alien_fuselage():
    # Antes radius=1.8, height=25
    main_body = trimesh.creation.cylinder(radius=3.5, height=12)  # Más ancho, menos alto
    main_body.apply_translation([0, 0, 6])  # Ajustar la altura para centrarlo
    main_body.visual.vertex_colors = [50, 50, 50, 255]
    return main_body

def create_escape_capsules():
    capsules = []
    # Ajustamos la posición y tamaño para que queden más integradas
    positions = [
        (3.6, 0, 4), (-3.6, 0, 4),
        (3.6, 0, 9), (-3.6, 0, 9)
    ]
    for pos in positions:
        capsule = trimesh.creation.cylinder(radius=0.9, height=3)  # Más gruesas y menos altas
        capsule.apply_translation([pos[0], pos[1], pos[2]])
        capsule.visual.vertex_colors = [80, 80, 80, 255]
        capsules.append(capsule)
    return capsules

def create_cross_tubes():
    tubes = []
    length = 14  # Reducimos la longitud proporcionalmente
    radius = 0.25  # Tubos más gruesos para dar aspecto grotesco
    for angle_deg in [0, 45, 90, 135]:
        tube = trimesh.creation.cylinder(radius=radius, height=length)
        tube.apply_translation([0, 0, length / 2])
        rot = trimesh.transformations.rotation_matrix(np.radians(angle_deg), [0, 0, 1])
        tube.apply_transform(rot)
        tube.visual.vertex_colors = [90, 90, 90, 255]
        tubes.append(tube)
    return tubes

def create_hex_shield_layer(z_height, radius=6.0):  # Aumentamos radio para cubrir nave más ancha
    panels = []
    step = 2 * radius / 6
    x_vals = np.arange(-radius, radius + step, step)
    y_vals = np.arange(-radius, radius + step, step * np.sqrt(3)/2)
    for i, y in enumerate(y_vals):
        offset = 0 if i % 2 == 0 else step / 2
        for x in x_vals:
            pos_x = x + offset
            if pos_x**2 + y**2 <= radius**2:
                panel = create_hex_panel(radius=0.7)  # Paneles más grandes
                panel.apply_translation([pos_x, y, z_height])
                panel.visual.vertex_colors = [255, 140, 0, 140]
                panels.append(panel)
    return panels

def create_hex_panel(radius=0.7, thickness=0.2):  # Más gruesos
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

def create_command_dome():
    dome = trimesh.creation.icosphere(subdivisions=3, radius=2.0)  # Más grande
    dome.apply_scale([1.4, 1.4, 0.8])
    dome.apply_translation([0, 0, 13])
    dome.visual.vertex_colors = [60, 60, 60, 200]
    return dome

def create_antennas():
    antennas = []
    base_z = 12
    for i in range(6):  # Más antenas para aspecto sci-fi
        angle = 2 * np.pi * i / 6
        x = np.cos(angle) * 2.5
        y = np.sin(angle) * 2.5
        antenna = trimesh.creation.cylinder(radius=0.1, height=3.5)
        antenna.apply_translation([x, y, base_z + 1.75])
        antenna.visual.vertex_colors = [100, 100, 120, 230]
        antennas.append(antenna)
        tip = trimesh.creation.icosphere(radius=0.15)
        tip.apply_translation([x, y, base_z + 3.5])
        tip.visual.vertex_colors = [150, 150, 170, 200]
        antennas.append(tip)
    return antennas

def create_solar_panels():
    panels = []
    panel_size = (5.0, 0.1, 1.5)  # Más grandes
    positions = [(0, -3.5, 7), (0, 3.5, 7)]
    for pos in positions:
        panel = trimesh.creation.box(extents=panel_size)
        panel.apply_translation(pos)
        panel.visual.vertex_colors = [40, 40, 60, 170]
        panels.append(panel)
    return panels

def create_vasimir_engine(position=[0, 0, 1], scale=1.5):  # Más grande y más bajo
    parts = []
    combustion = trimesh.creation.cylinder(radius=1.0 * scale, height=1.0 * scale)
    combustion.apply_translation([position[0], position[1], position[2]])
    combustion.visual.vertex_colors = [255, 69, 0, 220]
    parts.append(combustion)
    nozzle = trimesh.creation.cone(radius=1.3 * scale, height=1.0 * scale)
    nozzle.apply_translation([position[0], position[1], position[2] - 1.0 * scale])
    nozzle.visual.vertex_colors = [30, 144, 255, 180]
    parts.append(nozzle)
    for angle_deg in [0, 90, 180, 270]:
        tube = trimesh.creation.cylinder(radius=0.15 * scale, height=1.2 * scale)
        tube.apply_translation([position[0], position[1], position[2] + 0.25 * scale])
        rot = trimesh.transformations.rotation_matrix(np.radians(angle_deg), [0, 0, 1])
        tube.apply_transform(rot)
        tube.visual.vertex_colors = [120, 120, 120, 200]
        parts.append(tube)
    return combine_meshes(parts)

def create_turbine_engine(position=[2.6, 0, 2], scale=1.2):  # Más grandes y desplazadas un poco más afuera
    parts = []
    body = trimesh.creation.cylinder(radius=0.7 * scale, height=3.0 * scale)
    body.apply_translation(position)
    body.visual.vertex_colors = [130, 130, 130, 255]
    parts.append(body)
    for i in range(3):
        blade = trimesh.creation.box(extents=[0.1 * scale, 1.5 * scale, 0.4 * scale])
        rot_z = trimesh.transformations.rotation_matrix(np.radians(i*120), [0, 0, 1])
        blade.apply_transform(rot_z)
        rot_x = trimesh.transformations.rotation_matrix(np.radians(90), [1, 0, 0])
        blade.apply_transform(rot_x)
        blade.apply_translation([position[0], position[1], position[2] + 1.5 * scale])
        blade.visual.vertex_colors = [70, 70, 70, 255]
        parts.append(blade)
    return combine_meshes(parts)

def create_alien_ship_with_engines():
    parts = []
    parts.append(create_alien_fuselage())
    parts.extend(create_escape_capsules())
    parts.extend(create_cross_tubes())
    parts.extend(create_hex_shield_layer(z_height=7))
    parts.append(create_command_dome())
    parts.extend(create_antennas())
    parts.extend(create_solar_panels())

    vasimir_center = create_vasimir_engine(position=[0, 0, 1], scale=1.5)
    turbine_right = create_turbine_engine(position=[3.2, -1.2, 2], scale=1.2)
    turbine_left = create_turbine_engine(position=[-3.2, -1.2, 2], scale=1.2)

    parts.append(vasimir_center)
    parts.append(turbine_right)
    parts.append(turbine_left)

    return combine_meshes(parts)

def plot_mesh(mesh, filename="alien_ship_wide_scifi.png"):
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='3d')
    faces = mesh.faces
    vertices = mesh.vertices
    face_colors = mesh.visual.face_colors / 255.0 if hasattr(mesh.visual, 'face_colors') else (0.5, 0.5, 0.5, 1)
    collection = Poly3DCollection(vertices[faces], alpha=0.95, linewidths=0.7, edgecolors=(0, 0, 0, 0.7))
    collection.set_facecolor(face_colors)
    ax.add_collection3d(collection)
    bounds = mesh.bounds
    margin = 7
    ax.set_xlim(bounds[0][0]-margin, bounds[1][0]+margin)
    ax.set_ylim(bounds[0][1]-margin, bounds[1][1]+margin)
    ax.set_zlim(bounds[0][2]-margin, bounds[1][2]+margin)
    ax.set_axis_off()
    ax.view_init(elev=35, azim=60)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()
    print(f"Render guardado: {filename}")

if __name__ == "__main__":
    ship = create_alien_ship_with_engines()
    plot_mesh(ship)
    ship.export("alien_style_wide_grotesque_ship.stl")
    print("Archivo STL exportado como alien_style_wide_grotesque_ship.stl")
