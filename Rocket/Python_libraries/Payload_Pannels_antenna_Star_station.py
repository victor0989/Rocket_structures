import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Parámetros base de la nave
FUSELAGE_LENGTH = 12.0
FUSELAGE_RADIUS = 1.5
PAYLOAD_LENGTH = 3.5
PAYLOAD_RADIUS = 1.3
SHIELD_RADIUS = 2.6
SHIELD_THICKNESS = 0.25
ENGINE_RADIUS = 0.55
ENGINE_HEIGHT = 1.5
RADIATOR_WIDTH = 4.0
RADIATOR_HEIGHT = 0.15
RADIATOR_DEPTH = 1.2
SENSOR_RADIUS = 0.2

def create_fuselage():
    # Cilindro macizo que representa el cuerpo principal
    fuselage = trimesh.creation.cylinder(radius=FUSELAGE_RADIUS, height=FUSELAGE_LENGTH, sections=64)
    fuselage.apply_translation([0, 0, FUSELAGE_LENGTH/2])
    fuselage.visual.vertex_colors = [160, 160, 160, 255]  # Gris metálico
    return fuselage

def create_payload_module():
    # Cilindro de carga útil ligeramente más pequeño y más corto que el fuselaje
    payload = trimesh.creation.cylinder(radius=PAYLOAD_RADIUS, height=PAYLOAD_LENGTH, sections=48)
    payload.apply_translation([0, 0, FUSELAGE_LENGTH*0.5])
    payload.visual.vertex_colors = [90, 60, 30, 255]  # Marrón oscuro
    return payload

def create_thermal_shield():
    # Escudo térmico cilíndrico externo, con hueco para fuselaje
    outer = trimesh.creation.cylinder(radius=SHIELD_RADIUS, height=FUSELAGE_LENGTH * 0.75, sections=64)
    inner = trimesh.creation.cylinder(radius=SHIELD_RADIUS - SHIELD_THICKNESS, height=FUSELAGE_LENGTH * 0.75, sections=64)
    shield = outer.difference(inner)  # capa de grosor SHIELD_THICKNESS
    shield.apply_translation([0, 0, FUSELAGE_LENGTH*0.3])
    shield.visual.vertex_colors = [255, 69, 0, 150]  # Rojo anaranjado semitransparente
    return shield

def create_vasimr_engine():
    # Motor principal: cámara + boquilla
    chamber = trimesh.creation.cylinder(radius=ENGINE_RADIUS, height=ENGINE_HEIGHT * 0.7, sections=32)
    chamber.visual.vertex_colors = [80, 80, 160, 255]  # Azul oscuro metálico
    nozzle = trimesh.creation.cone(radius=ENGINE_RADIUS * 1.2, height=ENGINE_HEIGHT * 0.3, sections=32)
    nozzle.apply_translation([0, 0, -ENGINE_HEIGHT * 0.3])
    nozzle.visual.vertex_colors = [40, 40, 100, 255]  # Azul más oscuro
    engine = trimesh.util.concatenate([chamber, nozzle])
    engine.apply_translation([0, 0, -ENGINE_HEIGHT/2])
    return engine

def create_radiator_panels():
    # Dos paneles radiadores planos, simulan disipación térmica lateral
    radiators = []
    size = [RADIATOR_WIDTH, RADIATOR_DEPTH, RADIATOR_HEIGHT]
    positions = [[0, SHIELD_RADIUS + RADIATOR_DEPTH/2, FUSELAGE_LENGTH*0.65],
                 [0, -(SHIELD_RADIUS + RADIATOR_DEPTH/2), FUSELAGE_LENGTH*0.65]]
    for pos in positions:
        panel = trimesh.creation.box(extents=size)
        panel.apply_translation(pos)
        panel.visual.vertex_colors = [50, 50, 50, 160]  # Gris oscuro semitransparente
        radiators.append(panel)
    return radiators

def create_lidar_sensor(position):
    sensor = trimesh.creation.icosphere(subdivisions=3, radius=SENSOR_RADIUS)
    sensor.visual.vertex_colors = [255, 215, 0, 255]  # Amarillo dorado
    sensor.apply_translation(position)
    return sensor

def create_lidar_sensors():
    # Sensores distribuidos alrededor de fuselaje
    offsets = [
        [FUSELAGE_RADIUS * 0.8, 0, FUSELAGE_LENGTH * 0.9],
        [-FUSELAGE_RADIUS * 0.8, 0, FUSELAGE_LENGTH * 0.9],
        [0, FUSELAGE_RADIUS * 0.8, FUSELAGE_LENGTH * 0.85],
        [0, -FUSELAGE_RADIUS * 0.8, FUSELAGE_LENGTH * 0.85],
    ]
    return [create_lidar_sensor(pos) for pos in offsets]

def combine_meshes(mesh_list):
    return trimesh.util.concatenate(mesh_list)

def export_stl(mesh, filename="spacecraft_shipwright_full.stl"):
    mesh.export(filename)
    print(f"Modelo STL exportado a: {filename}")

def plot_mesh(mesh, filename="preview_spacecraft_full.png"):
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(111, projection='3d')
    faces = mesh.faces
    vertices = mesh.vertices
    collection = Poly3DCollection(vertices[faces], alpha=0.9, linewidths=0.3, edgecolors='k')
    collection.set_facecolor(mesh.visual.face_colors / 255)
    ax.add_collection3d(collection)
    bounds = mesh.bounds
    margin = 1
    ax.set_xlim(bounds[0][0]-margin, bounds[1][0]+margin)
    ax.set_ylim(bounds[0][1]-margin, bounds[1][1]+margin)
    ax.set_zlim(bounds[0][2]-margin, bounds[1][2]+margin)
    ax.set_axis_off()
    ax.view_init(elev=30, azim=45)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()
    print(f"Vista previa guardada en: {filename}")

def main():
    fuselage = create_fuselage()
    payload = create_payload_module()
    shield = create_thermal_shield()
    engine = create_vasimr_engine()
    radiators = create_radiator_panels()
    sensors = create_lidar_sensors()

    parts = [fuselage, payload, shield, engine] + radiators + sensors
    ship_mesh = combine_meshes(parts)

    export_stl(ship_mesh)
    plot_mesh(ship_mesh)

if __name__ == "__main__":
    main()
