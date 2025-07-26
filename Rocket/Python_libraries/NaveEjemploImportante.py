import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Parámetros base de la nave
FUS_RIB_A_BEV_SCALE_X = 1.5
REACTOR_THICK = 1.0
SENSOR_RAD = 0.25
SHIELD_MAJOR_RADIUS = 2.0
SHIELD_MINOR_RADIUS = 0.15

def create_fuselage():
    length = 8
    radius = 1.0 * FUS_RIB_A_BEV_SCALE_X
    cylinder = trimesh.creation.cylinder(radius=radius, height=length, sections=64)
    cylinder.apply_translation([0, 0, length/2])
    return cylinder

def create_reactor():
    reactor = trimesh.creation.cylinder(radius=0.8, height=2.0, sections=32)
    reactor.apply_translation([0, 0, 1.0])
    return reactor

def create_shield():
    torus = trimesh.creation.torus(SHIELD_MAJOR_RADIUS, SHIELD_MINOR_RADIUS)
    torus.apply_translation([0, 0, 4.0])
    return torus


def create_sensor(position):
    sphere = trimesh.creation.icosphere(subdivisions=3, radius=SENSOR_RAD)
    sphere.apply_translation(position)
    return sphere

def create_sensors():
    positions = [
        [1.5, 0, 6.5],
        [-1.5, 0, 6.5],
        [1.5, 0, 5.0],
        [-1.5, 0, 5.0],
    ]
    return [create_sensor(pos) for pos in positions]

def combine_meshes(mesh_list):
    return trimesh.util.concatenate(mesh_list)

def plot_mesh(mesh):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, projection='3d')

    faces = mesh.faces
    vertices = mesh.vertices

    mesh_collection = Poly3DCollection(vertices[faces], alpha=0.85)
    mesh_collection.set_facecolor((0.5, 0.6, 0.7))  # azul suave
    mesh_collection.set_edgecolor((0.1, 0.1, 0.1))  # bordes oscuros
    ax.add_collection3d(mesh_collection)

    # Escalado automático para ajustarse al tamaño de la nave
    scale = mesh.bounds
    x_min, y_min, z_min = scale[0]
    x_max, y_max, z_max = scale[1]
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_zlim(z_min, z_max)

    ax.set_axis_off()
    ax.view_init(elev=20, azim=45)

    plt.tight_layout()
    plt.savefig("nave_3d.png", dpi=300)
    plt.show()

def main():
    fuselage = create_fuselage()
    reactor = create_reactor()
    shield = create_shield()
    sensors = create_sensors()

    all_parts = [fuselage, reactor, shield] + sensors
    nave = combine_meshes(all_parts)

    plot_mesh(nave)

if __name__ == "__main__":
    main()


