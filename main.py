##################################
##### Distributed Ray Tracer #####
##### 2020 @ Mercy Bhakta    #####
##################################

#supporting classes
import math
from vector import Vector
from ray import Ray
from camera import Camera
from material import Material
from sphere import Sphere
from object import Object, Plane
from light import Light
from scene import world
#supporting libraries
import png
import unittest
import pdb

#image setup
image = [] #array for storing color value per pixel
imageWidth = 256 #also lives in scene.py...
imageHeight = 192
imageName = '.\images\image12.png' ## change this to get a new image ##

inf = math.inf #or float("inf")

#utility class for png creation
def createPNG(image):
    global imageName
    with open(imageName, 'wb') as f:
        w = png.Writer(imageWidth, imageHeight, greyscale=False)
        w.write(f, image)

def colorAt(ray, depth=2):
    ambient_color = Vector(0.0001, 0.0001, 0.0001)
    color = Vector(0,0,0)

    primaryRay = ray
    t_min = inf
    objHit = None
    #check each object-ray intersection
    for obj in world.objects:
        t = obj.checkIntersect(primaryRay) #returns t or inf
        #check if the intersection is the closest (so far)
        if t_min > t and t > 0:
            t_min = t
            objHit = obj

    if objHit is not None:
        hitPoint = primaryRay.pointAtDistance(t_min)
        occluded = False

        if depth > 0:
            v = -1 * ((primaryRay.getDirection()).normalize()) #viewer vec (hp to viewer)
            n = objHit.normal(hitPoint)
            r = 2 * ((n.dot(v)) * n) - v
            reflectRay = Ray(hitPoint, r)
            color = colorAt(reflectRay, depth-1) * objHit.reflectivity()

        for light in world.lights:

            l = (light.loc() - hitPoint).normalize()
            epsilon = Vector(0.01, 0.01, 0.01)
            shadowRay = Ray((hitPoint + epsilon), l)

            for obj in world.objects:
                d = obj.checkIntersect(shadowRay)

                if d > 0 and d < l.magnitude():
                    occluded = True
            #calculate shading at the intersection point
            color = (color + objHit.mat.reflect(objHit, hitPoint, light, primaryRay, occluded))
    else:
        color = ambient_color
    return color

#main func
def renderScene():
    global imageWidth
    global imageHeight
    global image

    samplesPerDirection = 3
    s = samplesPerDirection * samplesPerDirection #number of samples
    for j in range(0, imageHeight):
        row = ()
        for i in range(0, imageWidth):
            color = Vector(0,0,0)
            #send a ray from the cam into the world
            for x_samples in range(0, samplesPerDirection):
                for y_samples in range(0, samplesPerDirection):
                    primaryRay = world.camera.send_ray((i + x_samples / samplesPerDirection), (j + y_samples / samplesPerDirection))
                    color = color + colorAt(primaryRay)
            color = color / s
            row = row + color.colormap()
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
