##################################
##### Distributed Ray Tracer #####
##### 2020 @ Mercy Bhakta    #####
##################################

#supporting classes and libs
import math
from vector import Vector
from ray import Ray
from camera import Camera
from material import Material
from sphere import Sphere
from object import Object, Plane
from light import Light
#supporting libraries
import png
import unittest
import pdb
#image setup
image = [] #array for storing color value per pixel
imageWidth = 256
imageHeight = 192
aspectRatio = imageWidth / imageHeight
imageName = '.\images\image7.png' ## change this to get a new image ##

origin = Vector(0, 0, 0)
cam = Camera(origin, imageWidth, imageHeight, 24)

objects = []
lights = []
#lights
#head on, slightly above and beyond camera
lights.append(Light(Vector(0, 2, 2), Vector(1.0, 1.0, 1.0), Vector(1.0, 1.0, 1.0)))
#materials
difMat = Material("Diffuse", Vector(0.0, 0.8, 0.3))
specMat = Material("Specular", Vector(0.9, 0.0, 0.3))
#objects
objects.append(Sphere(Vector(0.0, -1.04, -4.0), 0.9, difMat))
objects.append(Sphere(Vector(0.0, 0.0, -4.0), 0.2, specMat))


inf = math.inf #or float("inf")

#utility class for png creation
def createPNG(image):
    global imageName
    with open(imageName, 'wb') as f:
        w = png.Writer(imageWidth, imageHeight, greyscale=False)
        w.write(f, image)

#main func
def renderScene():
    global imageWidth
    global imageHeight
    global image
    global objects
    global lights

    ambient_color = (10, 10, 10)

    for j in range(0, imageHeight):
        row = ()
        for i in range(0, imageWidth):
            #send a ray from the cam into the world
            primaryRay = cam.send_ray(i,j)
            t_min = inf
            objHit = None
            #check each object-ray intersection
            for obj in objects:
                t = obj.checkIntersect(primaryRay) #returns t or inf
                #check if the intersection is the closest (so far)
                if t_min > t and t > 0:
                    t_min = t
                    objHit = obj
            if objHit is not None:

                hitPoint = primaryRay.pointAtDistance(t_min)
                occluded = False
                light = lights[0]

                color = objHit.mat.reflect(obj, hitPoint, light, primaryRay)
                if i == (imageHeight - 1) and j == (imageHeight - 1):

                    print("testing obj", obj)
                    print("testing light", light)
                    print("testing primaryRay", primaryRay)

                    print("testing color", color)
                #this doesn't quite work for multiple light sources
                '''
                for light in lights:
                    l = (light.loc() - hitPoint).normalize()
                    epsilon = Vector(0.01, 0.01, 0.01)
                    shadowRay = Ray((hitPoint + epsilon), l)
                    for obj in objects:
                        d = obj.checkIntersect(shadowRay)
                        #if d < inf:
                        #if d <= 1 and d > 0:
                        if d > 0 and d < l.magnitude():
                            occluded = True
                if not occluded:
                    #calculate shading at the intersection point
                    color = objHit.mat.reflect(obj, hitPoint, light, primaryRay)
                else:
                    color = ambient_color
                '''
            else:
                color = (10, 10, 10)
            row = row + color
        image.append(row)
    createPNG(image)


renderScene()

if len(image) == imageHeight:
    #check to see the outputed image has enough rows
    print("")
    print("........................................")
    print(imageName[9:], "created successfully")
else:
    print("")
    print("........................................")
    print("Error Occured!")
