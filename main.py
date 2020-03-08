#supporting classes
import math
from vector import Vector
from ray import Ray
from material import Material
from sphere import Sphere
#supporting libraries
import png
#image setup
imageWidth = 300;
imageHeight = 200;
aspectRatio = imageWidth / imageHeight
imageName = 'spec9.png'
#scene, or "world" coordinates - adapted from Arun Ravindran's scene setup
xMin = -1.0
xMax = 1.0
xstep = (xMax - xMin) / (imageWidth - 1) #ratios for mapping

yMin = -1.0 / aspectRatio
yMax = 1.0 / aspectRatio
ystep = (yMax - yMin) / (imageHeight - 1) #ratios for mapping
image = []
objects = []
light = Vector(0, -10, -10)

#utility class for png creation
def createPNG(image):
    global imageName
    with open(imageName, 'wb') as f:
        w = png.Writer(imageWidth, imageHeight, greyscale=False)
        w.write(f, image)

def renderScene():
    global imageWidth
    global imageHeight
    global image
    global objects
    global light
    origin = Vector(0.0, 0.0, -1.0)
    shinyMat = Material("Specular", Vector(1.0, 0.0, 0.0))
    objects.append(Sphere(Vector(0.0, 0.0, 0.0), 0.5, shinyMat))


    for j in range(0, imageHeight):
        row = ()
        y = yMin + j * ystep
        for i in range(0, imageWidth):
            x = xMin + i * xstep
            #map image plane to pixels
            primaryRay = Ray(origin, Vector(x, y, 0.0) - origin)
            t_min=0
            objHit = None

            for obj in objects: #check each object-ray intersection

                t = obj.checkIntersect(primaryRay)
                #if the ray intersects obj and t is the minimum
                #then that obj is the closest
                if t is not None and (objHit is None or t < t_min):
                    t_min = t
                    objHit = obj
                    hitPoint = primaryRay.pointAtDistance(t)
                    normal = (hitPoint - obj.c).normalize()
                    #calculate shading at the intersection point
                    color = (obj.mat.reflect(hitPoint, normal, primaryRay, light)).componenets()
                    #print("color ", color)
                else:
                    #if there's no intersection, then there is no light
                    #and we leave the background color as black
                    color = (0,0,0)
            row = row + color
        image.append(row)
    createPNG(image)
#main func
renderScene()
print(imageName, " created successfully")
