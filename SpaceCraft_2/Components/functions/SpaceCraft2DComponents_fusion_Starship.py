import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ------------------- PARÁMETROS -------------------
FUSELAGE_LENGTH = 24.0
FUSELAGE_RADIUS = 1.2
WING_SPAN = 5.0
WING_WIDTH = 0.3
NUM_FIGHTERS = 6
FIGHTER_SCALE = 0.35

# ------------------- FUNCIONES 3D -------------------

def create_fuselage():
    body = trimesh.creation.cylinder(radius=FUSELAGE_RADIUS, height=FUSELAGE_LENGTH, sections=64)
    body.apply_translation([0, 0, FUSELAGE_LENGTH / 2])
    return body

def create_nose_cone():
    nose = trimesh.creation.cone(radius=FUSELAGE_RADIUS * 0.9, height=3.0)
    nose.apply_translation([0, 0, FUSELAGE_LENGTH + 1.5])
    return nose

def create_escape_tower():
    tower = trimesh.creation.cylinder(radius=0.2, height=1.5)
    tower.apply_translation([0, 0, FUSELAGE_LENGTH + 3.5])
    return tower

def create_propulsion_base():
    base = trimesh.creation.cone(radius=1.5, height=1.5)
    base.apply_translation([0, 0, -0.75])
    return base

def create_merlin_cluster():
    engines = []
    positions = [(np.cos(a) * 0.7, np.sin(a) * 0.7) for a in np.linspace(0, 2*np.pi, 8, endpoint=False)]
    positions.append((0, 0))  # Central engine
    for x, y in positions:
        nozzle = trimesh.creation.cone(radius=0.2, height=0.7)
        nozzle.apply_translation([x, y, -1.4])
        engines.append(nozzle)
    return engines

def create_wings():
    wings = []
    for angle in [np.radians(25), -np.radians(25)]:
        wing = trimesh.creation.box(extents=[WING_WIDTH, WING_SPAN, 0.15])
        wing.apply_translation([0, WING_SPAN/2, FUSELAGE_LENGTH * 0.5])
        rot = trimesh.transformations.rotation_matrix(angle, [1, 0, 0], point=[0, 0, FUSELAGE_LENGTH * 0.5])
        wing.apply_transform(rot)
        wings.append(wing.copy())
        wing.apply_translation([0, -WING_SPAN, 0])
        wings.append(wing)
    return wings

def create_shield_alternative():
    shield = []
    for angle in np.linspace(0, 2 * np.pi, 32, endpoint=False):
        x = 2.2 * np.cos(angle)
        y = 2.2 * np.sin(angle)
        tube = trimesh.creation.cylinder(radius=0.07, height=0.15)
        tube.apply_translation([x, y, FUSELAGE_LENGTH * 0.3])
        shield.append(tube)
    return shield

def create_sensors():
    positions = [[1.0, 0, FUSELAGE_LENGTH - 2], [-1.0, 0, FUSELAGE_LENGTH - 2]]
    sensors = []
    for pos in positions:
        sensor = trimesh.creation.icosphere(radius=0.15)
        sensor.apply_translation(pos)
        sensors.append(sensor)
    return sensors

def create_antennas():
    antennas = []
    for pos in [[0.5, 0.5, FUSELAGE_LENGTH - 1], [-0.5, -0.5, FUSELAGE_LENGTH - 1]]:
        mast = trimesh.creation.cylinder(radius=0.05, height=1.5)
        mast.apply_translation([pos[0], pos[1], pos[2] + 0.75])
        antennas.append(mast)
    return antennas

def create_fighter(position):
    body = trimesh.creation.cone(radius=0.2, height=0.6)
    body.apply_scale(FIGHTER_SCALE)
    body.apply_translation(position)
    return body

def create_fighter_wing():
    fighters = []
    radius = 4.2
    z = FUSELAGE_LENGTH * 0.7
    for i in range(NUM_FIGHTERS):
        theta = (2 * np.pi / NUM_FIGHTERS) * i
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        fighters.append(create_fighter([x, y, z]))
    return fighters

def create_dome():
    dome = trimesh.creation.icosphere(subdivisions=3, radius=1.2)
    dome.apply_scale([1.2, 1.2, 0.5])
    dome.apply_translation([0, 0, FUSELAGE_LENGTH + 2.5])
    return dome

def create_cargo_module():
    box = trimesh.creation.box(extents=[2.5, 2.5, 1.2])
    box.apply_translation([0, 0, FUSELAGE_LENGTH * 0.3])
    return box

def combine_meshes(meshes):
    return trimesh.util.concatenate(meshes)

# ------------------- PLOT -------------------

def plot_mesh(mesh):
    fig = plt.figure(figsize=(14, 14))
    ax = fig.add_subplot(111, projection='3d')
    faces = mesh.faces
    vertices = mesh.vertices

    collection = Poly3DCollection(vertices[faces], alpha=0.95)
    collection.set_facecolor((0.25, 0.4, 0.65, 0.95))
    collection.set_edgecolor((0.05, 0.05, 0.05, 0.3))
    ax.add_collection3d(collection)

    bounds = mesh.bounds
    ax.set_xlim(bounds[0][0] - 1, bounds[1][0] + 1)
    ax.set_ylim(bounds[0][1] - 1, bounds[1][1] + 1)
    ax.set_zlim(bounds[0][2] - 1, bounds[1][2] + 1)
    ax.set_axis_off()
    ax.view_init(elev=30, azim=45)
    plt.tight_layout()
    plt.savefig("/mnt/data/Starship_Falcon9_Improved.png", dpi=300)
    plt.show()

# ------------------- MAIN -------------------

def main():
    parts = []
    parts.append(create_fuselage())
    parts.append(create_nose_cone())
    parts.append(create_escape_tower())
    parts.append(create_propulsion_base())
    parts.extend(create_merlin_cluster())
    parts.extend(create_wings())
    parts.extend(create_shield_alternative())
    parts.extend(create_sensors())
    parts.extend(create_antennas())
    parts.extend(create_fighter_wing())
    parts.append(create_dome())
    parts.append(create_cargo_module())

    full_model = combine_meshes(parts)
    plot_mesh(full_model)

main()
