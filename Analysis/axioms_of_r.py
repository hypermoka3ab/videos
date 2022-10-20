from axioms import Axioms
from completude import Completude
from real_numbers import Intro
from multiprocessing import Pool
from manim import SceneFileWriter
SceneFileWriter.force_output_as_scene_name = True
with Pool(3) as pool:
    for scene in Intro, Axioms, Completude:
        scene().render()