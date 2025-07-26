import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Función para combinar mallas
def combine_meshes(meshes):
    return trimesh.util.concatenate(meshes)

# --------- Definición de la torre estilo Prometheus / Tycho Base ---------

def create_launch_tower(base_height=15.0, tower_radius=3.5, platform_height=2.0, num_platforms=4):
    components = []

    # Torre cilíndrica principal
    tower = trimesh.creation.cylinder(radius=tower_radius, height=base_height)
    tower.visual.vertex_colors = [169, 169, 169, 200]  # Gris medio translúcido
    components.append(tower)

    # Plataformas escalonadas a diferentes alturas
    for i in range(num_platforms):
        h = (i + 1) * (base_height / (num_platforms + 1))
        platform = trimesh.creation.box(extents=[tower_radius * 2.5, tower_radius * 2.5, platform_height])
        platform.apply_translation([0, 0, h])
        platform.visual.vertex_colors = [112, 128, 144, 255]  # Gris acero
        components.append(platform)

        # Barreras perimetrales (simples cajas delgadas)
        barrier = trimesh.creation.box(extents=[tower_radius * 2.5, 0.1, 0.3])
        barrier.visual.vertex_colors = [80, 80, 80, 255]
        # Colocarlas en los 4 lados
        offsets = [
            (0, (tower_radius * 2.5)/2, h + 0.15),
            (0, -(tower_radius * 2.5)/2, h + 0.15),
            ((tower_radius * 2.5)/2, 0, h + 0.15),
            (-(tower_radius * 2.5)/2, 0, h + 0.15),
        ]
        for off in offsets:
            bar = barrier.copy()
            bar.apply_translation(off)
            components.append(bar)

    # Columnas verticales exteriores para soporte (4)
    col_radius = 0.15
    col_height = base_height + 3
    col_positions = [
        (tower_radius, tower_radius, col_height/2),
        (-tower_radius, tower_radius, col_height/2),
        (tower_radius, -tower_radius, col_height/2),
        (-tower_radius, -tower_radius, col_height/2),
    ]
    for pos in col_positions:
        column = trimesh.creation.cylinder(radius=col_radius, height=col_height)
        column.apply_translation(pos)
        column.visual.vertex_colors = [105, 105, 105, 255]
        components.append(column)

    # Antenas y sensores en la cima
    antenna_height = 3.5
    for angle in np.linspace(0, 2 * np.pi, 6, endpoint=False):
        x = np.cos(angle) * (tower_radius * 0.8)
        y = np.sin(angle) * (tower_radius * 0.8)
        antenna = trimesh.creation.cylinder(radius=0.05, height=antenna_height)
        antenna.apply_translation([x, y, base_height + antenna_height / 2])
        antenna.visual.vertex_colors = [200, 200, 255, 230]
        components.append(antenna)

        tip = trimesh.creation.icosphere(radius=0.07)
        tip.apply_translation([x, y, base_height + antenna_height])
        tip.visual.vertex_colors = [200, 200, 255, 230]
        components.append(tip)

    # Plataforma superior para la nave
    platform_top = trimesh.creation.box(extents=[tower_radius*1.8, tower_radius*1.8, 0.5])
    platform_top.apply_translation([0, 0, base_height + 0.25])
    platform_top.visual.vertex_colors = [169, 169, 169, 230]
    components.append(platform_top)

    return combine_meshes(components)

# --------- Función principal para integrar nave + torre ---------

def create_station_with_falcon_and_tower():
    # Crear la nave (Falcon Parker)
    from your_falcon_module import create_falcon_parker_module  # Si lo tienes en otro archivo, o copiar el código de la nave arriba

    # Para el ejemplo, uso tu función definida antes directamente (copiarías tu create_falcon_parker_module aquí)
    falcon = create_falcon_parker_module(offset=(0, 0, 15.5))  # Nave posicionada sobre la torre

    # Crear la torre
    tower = create_launch_tower(base_height=15.0, tower_radius=3.5)

    # Combinar ambas
    station = combine_meshes([tower, falcon])

    return station

# --------- Renderizar la escena ---------

def plot_mesh(mesh, filename="station_with_falcon_and_tower.png"):
    fig = plt.figure(figsize=(14, 14))
    ax = fig.add_subplot(111, projection='3d')

    faces = mesh.faces
    vertices = mesh.vertices

    face_colors = mesh.visual.face_colors / 255.0 if hasattr(mesh.visual, 'face_colors') else (0.5, 0.5, 0.5, 1)

    collection = Poly3DCollection(vertices[faces], alpha=0.9, linewidths=0.7, edgecolors=(0.1, 0.1, 0.1, 0.8))
    collection.set_facecolor(face_colors)
    ax.add_collection3d(collection)

    bounds = mesh.bounds
    margin = 5
    ax.set_xlim(bounds[0][0] - margin, bounds[1][0] + margin)
    ax.set_ylim(bounds[0][1] - margin, bounds[1][1] + margin)
    ax.set_zlim(bounds[0][2] - margin, bounds[1][2] + margin)

    ax.set_axis_off()
    ax.view_init(elev=30, azim=45)

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()
    print(f"Renderizado guardado en {filename}")

# --------- Main ---------

if __name__ == "__main__":
    station = create_station_with_falcon_and_tower()
    plot_mesh(station)
    station.export("station_with_falcon_and_tower.stl")
    print("Modelo exportado como station_with_falcon_and_tower.stl")
