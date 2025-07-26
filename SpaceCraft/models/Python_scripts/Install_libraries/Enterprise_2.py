import trimesh
import numpy as np

def create_segmented_torus(radius_major, radius_minor, segments_major=12, segments_minor=6):
    """Simula un toroide con cilindros segmentados."""
    components = []
    angle_step = 2 * np.pi / segments_major
    for i in range(segments_major):
        angle = i * angle_step
        # Posición del cilindro en el círculo mayor
        center_x = radius_major * np.cos(angle)
        center_y = radius_major * np.sin(angle)
        # Orientación del cilindro, tangente al círculo mayor
        rotation_angle = angle + np.pi / 2

        cyl = trimesh.creation.cylinder(
            radius=radius_minor,
            height=radius_major * angle_step,
            sections=16
        )
        # Centrar el cilindro para que esté alineado en eje Y
        cyl.apply_translation([0, cyl.bounds[1][1]/2, 0])
        # Rotar para ser tangente al toro
        cyl.apply_transform(trimesh.transformations.rotation_matrix(
            rotation_angle, [0,0,1]
        ))
        # Mover al centro del segmento
        cyl.apply_translation([center_x, center_y, 0])
        components.append(cyl)
    return trimesh.util.concatenate(components)

def create_warp_nacelle(length=10, radius=1.5, curve_radius=6, segments=24):
    """Crea un nacelle curvado tipo warp como unión de cilindros ligeramente rotados."""
    components = []
    angle_step = np.pi / (2 * segments)  # curvatura de 90 grados en quarter circle
    for i in range(segments):
        angle = i * angle_step
        # Posición curva del cilindro
        center_x = curve_radius * np.sin(angle)
        center_y = curve_radius * (1 - np.cos(angle))
        cyl = trimesh.creation.cylinder(radius=radius, height=length/segments, sections=12)
        # Centrar el cilindro en altura
        cyl.apply_translation([0, cyl.bounds[1][1]/2, 0])
        # Rotar cilindro para alinear con la curva
        rot = trimesh.transformations.rotation_matrix(angle, [0, 0, 1])
        cyl.apply_transform(rot)
        # Trasladar cilindro a su posición curva
        cyl.apply_translation([center_x, center_y, 0])
        components.append(cyl)
    return trimesh.util.concatenate(components)

def create_parabolic_antenna(radius=1.0, depth=0.5, segments=16):
    """Crea una antena parabólica simple tipo Enterprise."""
    # Paraboloide aproximado con latitudinal segmentos
    phi = np.linspace(0, np.pi/2, segments)
    theta = np.linspace(0, 2*np.pi, segments)
    phi, theta = np.meshgrid(phi, theta)
    r = radius * (phi / (np.pi/2))**2  # parábola
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = depth * (1 - phi / (np.pi/2))
    # Crear malla de triángulos
    vertices = np.column_stack((x.flatten(), y.flatten(), z.flatten()))
    faces = []
    for i in range(segments-1):
        for j in range(segments-1):
            idx = i * segments + j
            faces.append([idx, idx+1, idx+segments])
            faces.append([idx+1, idx+segments+1, idx+segments])
    antenna_mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
    return antenna_mesh

def build_falcon_parker():
    components = []

    # Cuerpo principal
    fuselage = trimesh.creation.box(extents=[6, 20, 6])  # más grueso
    components.append(fuselage)

    # Motores traseros (cilindros)
    thruster1 = trimesh.creation.cylinder(radius=2.5, height=5, sections=16)
    thruster1.apply_translation([3, -12.5, 0])
    components.append(thruster1)

    thruster2 = thruster1.copy()
    thruster2.apply_translation([-6, 0, 0])
    components.append(thruster2)

    # Anillos torus reemplazados por segmentación con cilindros
    torus1 = create_segmented_torus(radius_major=4, radius_minor=0.5, segments_major=16, segments_minor=8)
    torus1.apply_translation([0, 2, 0])
    components.append(torus1)

    # Nacelles warp a los lados (curvados)
    nacelle_left = create_warp_nacelle(length=12, radius=1.2, curve_radius=6, segments=18)
    nacelle_left.apply_translation([-7, 0, 0])
    components.append(nacelle_left)

    nacelle_right = nacelle_left.copy()
    nacelle_right.apply_scale([-1,1,1])  # espejo en X
    components.append(nacelle_right)

    # Antenas parabólicas traseras (tipo Enterprise)
    antenna1 = create_parabolic_antenna(radius=1.8, depth=0.6, segments=24)
    antenna1.apply_translation([0, -10, 3])
    components.append(antenna1)

    antenna2 = antenna1.copy()
    antenna2.apply_translation([0, 0, -6])
    components.append(antenna2)

    # Combina todas las piezas
    model = trimesh.util.concatenate(components)
    model.export('falcon_parker_warp_model_3.stl')
    print("Modelo con nacelles y antenas exportado a falcon_parker_warp_model_3.stl")

if __name__ == "__main__":
    build_falcon_parker()
