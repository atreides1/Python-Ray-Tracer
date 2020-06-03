###############################
####### scene.py ##############
###############################
from vector import Vector
from camera import Camera
from sphere import Sphere
from light import Light
from material import Material

class Scene:
    def __init__(self, camera, objects, lights):
        self.camera = camera
        self.objects = objects
        self.lights = lights
imageWidth = 256
imageHeight = 192
origin = Vector(0, 0, 0)
cam = Camera(origin, imageWidth, imageHeight, 24)

objects = []
lights = []
#lights
#head on, slightly above and behind camera
lights.append(Light(Vector(0, 2, 2), Vector(0.5, 0.5, 0.5), Vector(1.0, 1.0, 1.0)))
#lights.append(Light(Vector(2, 2, 2), Vector(0.5, 0.5, 0.5), Vector(0.5, 0.5, 0.5)))
#materials
difMat = Material("Diffuse", Vector(0.0, 0.8, 0.3))
specMat = Material("Specular", Vector(0.9, 0.0, 0.3))
specMat2 = Material("Specular", Vector(0.9, 0.7, 0.0))
#objects
objects.append(Sphere(Vector(0.0, -1.04, -4.0), 0.9, difMat))
#objects.append(Sphere(Vector(0.0, 0.0, -4.0), 0.2, specMat))
objects.append(Sphere(Vector(0.0, 0.1, -3.0), 0.15, specMat2))
objects.append(Sphere(Vector(0.3, 0.2, -3.0), 0.1, specMat))
world = Scene(cam, objects, lights)
