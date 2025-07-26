import trimesh
import numpy as np
from trimesh.creation import cylinder, box, capsule
from trimesh.scene import Scene

def rotation_matrix_z(angle_deg):
    angle_rad = np.deg2rad(angle_deg)
    return trimesh.transformations.rotation_matrix(angle_rad, [0, 0, 1])

scene = Scene()

# --- Cuerpo principal ---
main_body = cylinder(radius=1.5, height=6, sections=40)
main_body.apply_translation([0, 0, 3])
scene.add_geometry(main_body)

# --- Compartimento de carga ---
cargo = box(extents=[2, 2, 2])
cargo.apply_translation([0, 0, 7])
scene.add_geometry(cargo)

# --- Módulos científicos modulares ---
for i in range(3):
    module = box(extents=[1, 1, 0.5])
    module.apply_translation([2.5, -1 + i*1.2, 3])
    scene.add_geometry(module)

# --- Cámaras/sensores ópticos sobre brazo extensible ---
arm = cylinder(radius=0.1, height=2)
arm.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2, [0,1,0]))
arm.apply_translation([-2, 0, 5])
camera = capsule(radius=0.2, height=0.5)
camera.apply_translation([-3, 0, 5])
scene.add_geometry(arm)
scene.add_geometry(camera)

# --- Antenas modulares FPGA ---
for angle in range(0, 360, 90):
    antenna = box(extents=[0.1, 1.5, 0.2])
    antenna.apply_transform(rotation_matrix_z(angle))
    antenna.apply_translation([1.7 * np.cos(np.radians(angle)), 1.7 * np.sin(np.radians(angle)), 6])
    scene.add_geometry(antenna)

# --- Cápsulas CubeSat ---
for i in range(2):
    cubesat = box(extents=[0.5, 0.5, 0.5])
    cubesat.apply_translation([-0.8 + i * 1.6, 0.8, 7.8])
    scene.add_geometry(cubesat)

# --- Propulsores ---
# Hidrazina - Cilíndricos
for i in [-1, 1]:
    thruster_h = cylinder(radius=0.2, height=0.6)
    thruster_h.apply_translation([i * 1.5, -1.2, 1])
    scene.add_geometry(thruster_h)

# Iónicos - Cúbicos
for i in [-1, 1]:
    thruster_i = box(extents=[0.4, 0.4, 0.4])
    thruster_i.apply_translation([i * 1.5, 1.2, 1])
    scene.add_geometry(thruster_i)

# --- Combina todas las geometrías y exporta a STL ---
combined_mesh = trimesh.util.concatenate([g for g in scene.geometry.values()])
combined_mesh.export('modelo_espacial.stl')

print("Archivo STL 'modelo_espacial.stl' generado correctamente.")
