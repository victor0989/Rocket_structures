import trimesh
import numpy as np


def create_engine_nozzle():
    # Nozzle profile (simplificado)
    height = 10.0
    radius_top = 1.0
    radius_bottom = 3.0
    sections = 64

    # Crea un cono truncado para el nozzle
    nozzle = trimesh.creation.cone(radius=radius_bottom, height=height, sections=sections)
    nozzle.apply_translation([0, 0, height / 2])

    return nozzle


def create_turbopump():
    # Cilindro representando turbopump
    height = 3.0
    radius = 1.0
    pump = trimesh.creation.cylinder(radius=radius, height=height, sections=64)
    pump.apply_translation([0, 0, 11.5])  # sobre el nozzle

    return pump


def create_chamber():
    # Cámara de combustión tipo campana
    height = 5.0
    radius_top = 0.8
    radius_bottom = 1.2
    chamber = trimesh.creation.cone(radius=radius_bottom, height=height, sections=64)
    chamber.apply_translation([0, 0, 8.0])  # entre nozzle y turbopump

    return chamber


def combine_parts():
    parts = [
        create_engine_nozzle(),
        create_chamber(),
        create_turbopump()
    ]
    engine = trimesh.util.concatenate(parts)
    return engine


# Generar motor
engine_model = combine_parts()

# Exportar a STL
engine_model.export('merlin_style_engine.stl')
print("✅ Archivo STL generado como 'merlin_style_engine.stl'")
