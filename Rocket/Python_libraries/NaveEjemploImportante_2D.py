import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

#--------------------
# Base ship parameters
FUS_RIB_A_BEV_SCALE_X = 1.5
REACTOR_THICK = 1.0
SENSOR_RAD = 0.25
SHIELD_MAJOR_RADIUS = 2.0
SHIELD_MINOR_RADIUS = 0.15

#--------------------
# PART CREATION FUNCTIONS

def create_fuselage():
    """
    Fuselage: Long cylinder
    Suggested material:
    - Aluminum 7075-T6 or Titanium 6Al-4V (lightness + strength)
    """
    length = 8
    radius = 1.0 * FUS_RIB_A_BEV_SCALE_X
    cylinder = trimesh.creation.cylinder(radius=radius, height=length, sections=64)
    cylinder.apply_translation([0, 0, length/2])
    return cylinder

def create_reactor():
    """
    Reactor: Smaller cylinder at the rear
    Suggested material:
    - Inconel 718 or ZrO2 ceramic (high thermal and chemical resistance)
    """
    reactor = trimesh.creation.cylinder(radius=0.8, height=2.0, sections=32)
    reactor.apply_translation([0, 0, 1.0])
    return reactor

def create_shield():
    """
    Heat and radiation shield: Torus
    Suggested material:
    - PICA-X (SpaceX) or advanced ceramic for heat dissipation
    - Anti-microwave coating: Pyrolytic carbon or tungsten
    - Radiation shielding: tantalum, hydrogen-enriched polyethylene
    """
    torus = trimesh.creation.torus(SHIELD_MAJOR_RADIUS, SHIELD_MINOR_RADIUS)
    torus.apply_translation([0, 0, 4.0])
    return torus

def create_sensor(position):
    """
    Sensors/LIDAR: Small spheres to represent cameras or sensors
    """
    sphere = trimesh.creation.icosphere(subdivisions=3, radius=SENSOR_RAD)
    sphere.apply_translation(position)
    return sphere

def create_sensors():
    """
    Position sensors in four strategic locations for navigation and monitoring
    """
    positions = [
        [1.5, 0, 6.5],
        [-1.5, 0, 6.5],
        [1.5, 0, 5.0],
        [-1.5, 0, 5.0],
    ]
    return [create_sensor(pos) for pos in positions]

def combine_meshes(mesh_list):
    return trimesh.util.concatenate(mesh_list)

# --------------------
# 3D GRAPH

def plot_mesh(mesh):
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(111, projection='3d')

    faces = mesh.faces
    vertices = mesh.vertices

    mesh_collection = Poly3DCollection(vertices[faces], alpha=0.9)
    mesh_collection.set_facecolor((0.4, 0.5, 0.65, 0.9)) # translucent grayish blue
    mesh_collection.set_edgecolor((0.1, 0.1, 0.15, 0.8)) # Dark borders with some transparency.
    ax.add_collection3d(mesh_collection)

    # Scaling and bounds enhancement
    bounds = mesh.bounds
    x_min, y_min, z_min = bounds[0]
    x_max, y_max, z_max = bounds[1]
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_zlim(z_min, z_max)

    ax.set_axis_off()
    ax.view_init(elev=30, azim=45) # Slightly higher angle for better perspective

    plt.tight_layout()
    plt.savefig("3d_enhanced_ship.png", dpi=300)
    plt.show()

#--------------------
# MAIN

def main():
    fuselage = create_fuselage()
    reactor = create_reactor()
    shield = create_shield()
    sensors = create_sensors()

    all_parts = [fuselage, reactor, shield] + sensors
    ship = combine_meshes(all_parts)

    plot_mesh(ship)

if __name__ == "__main__":
    main()

#--------------------
# ENGINEERING AND ASSEMBLY NOTES (for documentation)
"""
- Combustion chamber with ablative insulation (phenolic or ceramic).
- N2O tanks with certified high-pressure lines.
- Redundant solenoid valves and ignition system.
- Actuators for thrust vector control (industrial servos).
- Avionics: NVIDIA Jetson or STM32, MPU9250 IMU + dual GPS.
- PID algorithms and Kalman filters for orbital navigation.
- Cargo and internal cabin: modular racks, 3D printing for structures, thermal insulation with aerogel or foam Nomex.
- Power system: Tesla 21700 or LiFePO4 batteries, supercapacitors, DC-DC regulators.
- Thermal and aerodynamic shielding with PICA-X tiles, carbon plates, and ceramic ablators.
- Materials resistant to high temperatures, space radiation, and electromagnetic fields.
- Advanced structural components: metamaterials, graphene for thermal management, shape memory alloys, NEMS sensors.
- Axial and centrifugal compressors for propulsion systems.
"""
