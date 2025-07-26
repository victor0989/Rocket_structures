import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Parámetros globales para la estación
STATION_MODULE_LENGTH = 30.0
STATION_MODULE_RADIUS = 3.0

def create_station_module(length=STATION_MODULE_LENGTH, radius=STATION_MODULE_RADIUS, color=[100, 149, 237, 180]):
    """Crea un módulo cilíndrico básico para la estación"""
    module = trimesh.creation.cylinder(radius=radius, height=length)
    module.apply_translation([0, 0, length / 2])
    module.visual.vertex_colors = color
    return module

def create_connection_tunnel(length=8.0, radius=0.6, color=[169, 169, 169, 200]):
    """Crea un cilindro pequeño que hace de túnel o conector entre módulos"""
    tunnel = trimesh.creation.cylinder(radius=radius, height=length)
    tunnel.visual.vertex_colors = color
    tunnel.apply_translation([0, 0, length / 2])
    return tunnel

def create_solar_array(position, panel_count=4, panel_size=(8, 0.1, 2), spacing=2.5):
    """Crea una fila de paneles solares planos en línea"""
    panels = []
    width, depth, height = panel_size
    for i in range(panel_count):
        panel = trimesh.creation.box(extents=panel_size)
        x_pos = i * (width + spacing)
        panel.apply_translation([position[0] + x_pos, position[1], position[2]])
        panel.visual.vertex_colors = [30, 144, 255, 200]  # Azul translúcido
        panels.append(panel)
    return panels

def create_antenna_cluster(position, count=6):
    """Crea un grupo de antenas cilíndricas pequeñas con puntas esféricas"""
    antennas = []
    radius = 0.05
    height = 1.2
    for i in range(count):
        angle = 2 * np.pi * i / count
        x = position[0] + np.cos(angle) * 1.5
        y = position[1] + np.sin(angle) * 1.5
        z = position[2]
        mast = trimesh.creation.cylinder(radius=radius, height=height)
        mast.apply_translation([x, y, z + height / 2])
        mast.visual.vertex_colors = [220, 220, 220, 210]
        tip = trimesh.creation.icosphere(radius=0.07)
        tip.apply_translation([x, y, z + height])
        tip.visual.vertex_colors = [200, 200, 255, 230]
        antennas.extend([mast, tip])
    return antennas

def create_structural_arm(length=6, thickness=0.2, angle=np.pi / 4, base_position=(0,0,0)):
    """Crea un brazo estructural con rotación"""
    arm = trimesh.creation.box(extents=[thickness, thickness, length])
    arm.apply_translation([0, 0, length / 2])
    rot = trimesh.transformations.rotation_matrix(angle, [0, 1, 0], point=[0,0,0])
    arm.apply_transform(rot)
    arm.apply_translation(base_position)
    arm.visual.vertex_colors = [128, 128, 128, 255]
    return arm

def create_station():
    modules = []
    tunnels = []
    antennas = []
    solar_panels = []

    # Módulos principales en línea
    positions = [
        [0, 0, 0],
        [0, 0, STATION_MODULE_LENGTH + 10],
        [0, 0, 2 * (STATION_MODULE_LENGTH + 10)],
        [STATION_MODULE_RADIUS * 3, 0, STATION_MODULE_LENGTH / 2],  # módulo lateral grande
    ]

    colors = [
        [100, 149, 237, 180],  # azul acero translúcido
        [70, 130, 180, 200],   # azul acero sólido
        [65, 105, 225, 220],   # azul real
        [72, 61, 139, 180],    # azul medianoche translúcido
    ]

    for pos, col in zip(positions, colors):
        mod = create_station_module(length=STATION_MODULE_LENGTH, radius=STATION_MODULE_RADIUS, color=col)
        mod.apply_translation(pos)
        modules.append(mod)

    # Conectores entre módulos lineales
    for i in range(len(positions)-1):
        p1 = positions[i]
        p2 = positions[i+1]
        # calcular vector entre módulos
        vec = np.array(p2) - np.array(p1)
        dist = np.linalg.norm(vec)
        direction = vec / dist
        tunnel = create_connection_tunnel(length=dist- (STATION_MODULE_RADIUS * 2))
        # rotar para alinear con dirección
        axis = np.cross([0, 0, 1], direction)
        angle = np.arccos(np.dot([0, 0, 1], direction))
        if np.linalg.norm(axis) > 1e-6:
            axis = axis / np.linalg.norm(axis)
            rot = trimesh.transformations.rotation_matrix(angle, axis)
            tunnel.apply_transform(rot)
        # trasladar al punto medio entre módulos
        midpoint = (np.array(p1) + np.array(p2)) / 2
        tunnel.apply_translation(midpoint)
        tunnels.append(tunnel)

    # Añadir paneles solares al módulo lateral grande
    solar_panels.extend(create_solar_array(position=[positions[-1][0]-10, positions[-1][1], positions[-1][2]+STATION_MODULE_LENGTH/2]))

    # Añadir antenas en módulo frontal
    antennas.extend(create_antenna_cluster(position=[positions[0][0], positions[0][1], positions[0][2]+STATION_MODULE_LENGTH]))

    # Añadir brazos estructurales cruzados entre el módulo lateral y el central frontal
    arms_positions = [
        ([STATION_MODULE_RADIUS * 1.5, 0, STATION_MODULE_LENGTH / 2], np.pi/3),
        ([STATION_MODULE_RADIUS * 1.5, 0, STATION_MODULE_LENGTH], np.pi/6),
        ([STATION_MODULE_RADIUS * 2.5, 0, STATION_MODULE_LENGTH * 1.5], -np.pi/4),
    ]
    arms = [create_structural_arm(base_position=pos, angle=angle) for pos, angle in arms_positions]

    # Combinar todo
    all_parts = modules + tunnels + solar_panels + antennas + arms
    station = trimesh.util.concatenate(all_parts)
    return station

def plot_mesh(mesh, filename="space_station_1.png"):
    fig = plt.figure(figsize=(16, 16))
    ax = fig.add_subplot(111, projection='3d')

    faces = mesh.faces
    vertices = mesh.vertices
    face_colors = mesh.visual.face_colors / 255.0 if hasattr(mesh.visual, 'face_colors') else (0.2, 0.4, 0.6, 0.9)

    collection = Poly3DCollection(vertices[faces], alpha=0.9, linewidths=0.5, edgecolors=(0.1, 0.1, 0.1, 0.6))
    collection.set_facecolor(face_colors)
    ax.add_collection3d(collection)

    bounds = mesh.bounds
    margin = 10
    ax.set_xlim(bounds[0][0] - margin, bounds[1][0] + margin)
    ax.set_ylim(bounds[0][1] - margin, bounds[1][1] + margin)
    ax.set_zlim(bounds[0][2] - margin, bounds[1][2] + margin)

    ax.set_axis_off()
    ax.view_init(elev=25, azim=30)

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"Estación espacial renderizada en {filename}")

if __name__ == "__main__":
    station_mesh = create_station()
    plot_mesh(station_mesh)
    station_mesh.export("space_station.stl")
    print("Archivo STL de la estación espacial creado.")
