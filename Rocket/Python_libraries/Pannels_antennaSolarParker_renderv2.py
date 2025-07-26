import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from trimesh.creation import torus

FUSELAGE_LENGTH = 20.0
FUSELAGE_RADIUS = 1.35

def combine_meshes(meshes):
    # Combinar en grupos de 10 para evitar sobrecarga
    combined = []
    for i in range(0, len(meshes), 10):
        combined.append(trimesh.util.concatenate(meshes[i:i+10]))
    return trimesh.util.concatenate(combined)

def create_advanced_fuselage():
    components = []

    main_body = trimesh.creation.cylinder(radius=FUSELAGE_RADIUS + 0.3, height=FUSELAGE_LENGTH)
    main_body.apply_translation([0, 0, FUSELAGE_LENGTH / 2])
    main_body.visual.vertex_colors = [65, 105, 225, 255]
    components.append(main_body)

    # Reducir anillos estructurales a 2
    for z in np.linspace(4, FUSELAGE_LENGTH - 4, 2):
        ring = trimesh.creation.torus(FUSELAGE_RADIUS + 0.32, 0.05)
        ring.apply_translation([0, 0, z])
        ring.visual.vertex_colors = [105, 105, 105, 255]
        components.append(ring)

    # Compartimentos externos reducidos a 2
    for z in [5.0, 12.0]:
        compartment = trimesh.creation.cylinder(radius=0.4, height=1.5)
        compartment.apply_translation([FUSELAGE_RADIUS + 0.6, 0, z])
        compartment.visual.vertex_colors = [139, 69, 19, 255]
        components.append(compartment)

    kevlar_layer = trimesh.creation.cylinder(radius=FUSELAGE_RADIUS + 0.4, height=FUSELAGE_LENGTH)
    kevlar_layer.apply_translation([0, 0, FUSELAGE_LENGTH / 2])
    kevlar_layer.visual.vertex_colors = [184, 134, 11, 90]
    components.append(kevlar_layer)

    # Escudos pequeños reducidos a 2
    for i in range(2):
        angle = i * (2 * np.pi / 3)
        x = np.cos(angle) * (FUSELAGE_RADIUS + 0.5)
        y = np.sin(angle) * (FUSELAGE_RADIUS + 0.5)
        fin = trimesh.creation.box(extents=[0.05, 1.2, 0.8])
        fin.apply_translation([x, y, FUSELAGE_LENGTH / 2])
        fin.visual.vertex_colors = [169, 169, 169, 200]
        components.append(fin)

    # Sensores reducidos a 1 por posición
    for z in [4.0]:
        sensor = trimesh.creation.icosphere(radius=0.2)
        sensor.apply_translation([0, -(FUSELAGE_RADIUS + 0.4), z])
        sensor.visual.vertex_colors = [255, 140, 0, 255]
        components.append(sensor)

    return combine_meshes(components)

# Mantén el resto de funciones igual, pero con estas modificaciones para reducir carga:
# - reduce cantidad de elementos en loops (anillos, sensores, escudos)
# - usa combine_meshes en grupos para no saturar la memoria

def create_nose_cone():
    cone = trimesh.creation.cone(radius=FUSELAGE_RADIUS * 0.9, height=3.2)
    cone.apply_translation([0, 0, FUSELAGE_LENGTH + 1.6])
    cone.visual.vertex_colors = [255, 215, 0, 255]
    return cone

def create_escape_tower():
    tower = trimesh.creation.cylinder(radius=0.2, height=1.4)
    tower.apply_translation([0, 0, FUSELAGE_LENGTH + 3.2])
    tower.visual.vertex_colors = [192, 192, 192, 220]
    return tower

def create_propulsion_base():
    base = trimesh.creation.cone(radius=1.4, height=1.2)
    base.apply_translation([0, 0, -0.6])
    base.visual.vertex_colors = [105, 105, 105, 255]
    return base

def create_thermal_shield():
    shield = trimesh.creation.cylinder(radius=2.6, height=0.6)
    shield.apply_translation([0, 0, FUSELAGE_LENGTH + 0.3])
    shield.visual.vertex_colors = [255, 69, 0, 150]
    return shield

def create_reinforced_heat_shield_layers():
    layers = []
    radii = [2.7, 2.9]  # menos capas
    heights = [0.15, 0.15]
    colors = [[255, 140, 0, 120], [255, 69, 0, 100]]
    z_pos = FUSELAGE_LENGTH + 0.6
    for r, h, c in zip(radii, heights, colors):
        layer = trimesh.creation.cylinder(radius=r, height=h)
        layer.apply_translation([0, 0, z_pos])
        layer.visual.vertex_colors = c
        layers.append(layer)
        z_pos += h
    return layers

# Puedes continuar con las demás funciones sin cambios o con reducción similar (menos loops, menos instancias)

# La función main con pocos componentes para que corra rápido:

def main():
    components = [
        create_advanced_fuselage(),
        create_nose_cone(),
        create_escape_tower(),
        create_propulsion_base(),
        create_thermal_shield(),
        *create_reinforced_heat_shield_layers(),
        # Puedes añadir más con cuidado
    ]

    model = combine_meshes(components)
    plot_mesh(model, filename="falcon_light.png")
    model.export('falcon_light.stl')
    print("Modelo exportado y renderizado ligero.")

def plot_mesh(mesh, filename="output.png"):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, projection='3d')

    faces = mesh.faces
    vertices = mesh.vertices

    face_colors = mesh.visual.face_colors / 255.0 if hasattr(mesh.visual, 'face_colors') else (0.2, 0.4, 0.6, 0.9)

    collection = Poly3DCollection(vertices[faces], alpha=0.9, linewidths=0.7, edgecolors=(0.1,0.1,0.1,0.8))
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
    print(f"Imagen guardada como: {filename}")

if __name__ == "__main__":
    main()
