import trimesh
import numpy as np

FUSELAGE_LENGTH = 20.0
FUSELAGE_RADIUS = 1.35

def create_ring(radius=1.7, tube_radius=0.05, segments=32):
    # Construye un anillo tipo toro usando cilindros pequeños unidos en círculo
    parts = []
    for i in range(segments):
        angle = 2 * np.pi * i / segments
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        cyl = trimesh.creation.cylinder(radius=tube_radius, height=0.15)
        cyl.apply_translation([0, 0, -0.075])  # centrar eje z
        # rotar el cilindro para que quede tangente al anillo
        rot = trimesh.transformations.rotation_matrix(angle, [0, 0, 1])
        cyl.apply_transform(rot)
        # trasladar a la posición sobre el anillo
        cyl.apply_translation([x, y, 0])
        parts.append(cyl)
    return trimesh.util.concatenate(parts)

def create_advanced_fuselage():
    components = []

    # Cuerpo principal grueso y compacto
    main_body = trimesh.creation.cylinder(radius=FUSELAGE_RADIUS + 0.3, height=FUSELAGE_LENGTH)
    main_body.apply_translation([0, 0, FUSELAGE_LENGTH / 2])
    main_body.visual.vertex_colors = [65, 105, 225, 255]
    components.append(main_body)

    # Anillos estructurales (reemplazo de torus)
    for z in np.linspace(2, FUSELAGE_LENGTH - 2, 5):
        ring = create_ring(radius=FUSELAGE_RADIUS + 0.32, tube_radius=0.05)
        ring.apply_translation([0, 0, z])
        ring.visual.vertex_colors = [105, 105, 105, 255]
        components.append(ring)

    # Compartimentos cilíndricos externos
    for z in [5.0, 10.0, 15.0]:
        compartment = trimesh.creation.cylinder(radius=0.4, height=1.5)
        compartment.apply_translation([FUSELAGE_RADIUS + 0.6, 0, z])
        compartment.visual.vertex_colors = [139, 69, 19, 255]
        components.append(compartment)

    # Revestimiento kevlar
    kevlar_layer = trimesh.creation.cylinder(radius=FUSELAGE_RADIUS + 0.4, height=FUSELAGE_LENGTH)
    kevlar_layer.apply_translation([0, 0, FUSELAGE_LENGTH / 2])
    kevlar_layer.visual.vertex_colors = [184, 134, 11, 90]
    components.append(kevlar_layer)

    # Escudos pequeños (aletas)
    for i in range(3):
        fin = trimesh.creation.box(extents=[0.05, 1.2, 0.8])
        angle = i * (2 * np.pi / 3)
        x = np.cos(angle) * (FUSELAGE_RADIUS + 0.5)
        y = np.sin(angle) * (FUSELAGE_RADIUS + 0.5)
        fin.apply_translation([x, y, FUSELAGE_LENGTH / 2])
        fin.visual.vertex_colors = [169, 169, 169, 200]
        components.append(fin)

    # Sensores adicionales
    for z in [4.0, 12.0]:
        sensor = trimesh.creation.icosphere(radius=0.2)
        sensor.apply_translation([0, -(FUSELAGE_RADIUS + 0.4), z])
        sensor.visual.vertex_colors = [255, 140, 0, 255]
        components.append(sensor)

    return trimesh.util.concatenate(components)

def create_warp_nacelle_curve(length=8.0, radius=0.5, curve_radius=5.0):
    # Crea una nacelle curvada tipo warp con cilindro y deformación curva simple
    nacelle = trimesh.creation.cylinder(radius=radius, height=length, sections=48)
    # Para curvar: dividimos la malla en segmentos y rotamos progresivamente
    vertices = nacelle.vertices.copy()
    for i, v in enumerate(vertices):
        # calcular ángulo de curvatura según altura z
        z = v[2]
        angle = (z / length) * np.pi / 4  # curvatura hasta 45 grados
        # rotar puntos en x,y alrededor eje y para curvar
        c, s = np.cos(angle), np.sin(angle)
        x_new = c * v[0] + s * (curve_radius - v[1])
        y_new = -s * v[0] + c * (curve_radius - v[1])
        vertices[i] = [x_new, y_new, z]
    nacelle.vertices = vertices
    return nacelle

def create_nacelles():
    nacelle_left = create_warp_nacelle_curve()
    nacelle_right = create_warp_nacelle_curve()

    # posicionar a los lados del fuselaje
    nacelle_left.apply_translation([-FUSELAGE_RADIUS - 1.5, 0, FUSELAGE_LENGTH / 3])
    nacelle_right.apply_translation([FUSELAGE_RADIUS + 1.5, 0, FUSELAGE_LENGTH / 3])

    # Colores metalizados azul oscuro
    nacelle_left.visual.vertex_colors = [30, 60, 120, 255]
    nacelle_right.visual.vertex_colors = [30, 60, 120, 255]
    return [nacelle_left, nacelle_right]

def create_rear_parabolic_antenna():
    cone = trimesh.creation.cone(radius=1.2, height=0.6)
    cone.apply_translation([0, 0, FUSELAGE_LENGTH + 0.9])
    cone.visual.vertex_colors = [211, 211, 211, 220]

    mast = trimesh.creation.cylinder(radius=0.07, height=0.8)
    mast.visual.vertex_colors = [169, 169, 169, 255]
    mast.apply_translation([0, 0, FUSELAGE_LENGTH + 0.1])
    return [cone, mast]

def main():
    components = [
        create_advanced_fuselage(),
        create_nacelles(),
        *create_rear_parabolic_antenna(),
        # Aquí puedes añadir el resto de partes que ya tienes definidas
    ]
    model = trimesh.util.concatenate(components)
    model.export('falcon_parker_warp_model_1.stl')
    print("Modelo con nacelles y antenas exportado a falcon_parker_warp_model.stl")

if __name__ == "__main__":
    main()
