import trimesh
import numpy as np
from trimesh.creation import cone, cylinder
from trimesh.transformations import rotation_matrix

def combine_meshes(meshes):
    return trimesh.util.concatenate(meshes)

def create_merlin_nozzle():
    outer_nozzle = cone(radius=0.65, height=1.2, sections=64)
    inner_cut = cylinder(radius=0.15, height=1.2, sections=64)
    inner_cut.apply_translation([0, 0, 0.6])
    nozzle = outer_nozzle.difference(inner_cut)
    nozzle.visual.vertex_colors = [200, 200, 200, 255]
    return nozzle

def create_combustion_chamber():
    chamber = cylinder(radius=0.22, height=0.5)
    chamber.apply_translation([0, 0, 1.2])
    chamber.visual.vertex_colors = [150, 150, 150, 255]
    return chamber

def create_turbopump():
    turbo = cylinder(radius=0.28, height=0.4)
    turbo.apply_translation([0, 0, 1.7])
    turbo.visual.vertex_colors = [80, 80, 80, 255]
    return turbo

def create_feed_lines():
    pipes = []
    for angle in [0, np.pi / 2, np.pi, 3*np.pi/2]:
        pipe = cylinder(radius=0.02, height=0.3, sections=24)
        rot = rotation_matrix(angle, [0, 0, 1])
        pipe.apply_transform(rot)
        pipe.apply_translation([0.3 * np.cos(angle), 0.3 * np.sin(angle), 1.5])
        pipes.append(pipe)
    return pipes

def create_detailed_merlin_engine(position=[0, 0, 0]):
    nozzle = create_merlin_nozzle()
    chamber = create_combustion_chamber()
    turbo = create_turbopump()
    pipes = create_feed_lines()
    engine = combine_meshes([nozzle, chamber, turbo] + pipes)
    engine.apply_translation(position)
    return engine

engine = create_detailed_merlin_engine()
engine.export('/mnt/c/Users/PC/PycharmProjects/pythonProject1/merlin_engine_detailed_fixed.stl')


