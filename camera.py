from vector import Vector
from ray import Ray
from math import pi, tan
'''
class Camera:
    def __init__(self, origin, imageWidth, imageHeight, xMin, xMax, yMin, yMax):
        self.origin = origin
        self.xMin = xMin
        self.yMin = yMin
        self.worldWidth = xMax - self.xMin
        self.worldHeight = yMax - self.yMin
        self.xMap = self.worldWidth / imageWidth  #self.worldWidth / (imageWidth - 1)
        self.yMap = self.worldHeight / imageHeight
        self.aspectRatio = imageWidth / imageHeight
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight

    def send_ray(self, i, j):
        #f = open("results.txt", "a")

        x = ((i * self.xMap + self.xMin)) #* 0.2) + (1 / self.aspectRatio)
        y = ((j * self.yMap + self.yMin)) #* 0.2) + (1 / self.aspectRatio) #this could be stored and reused...
        pixel = Vector(x, y, 0)
        #f.write(pixel.__str__())
        #f.close()
        direction = pixel - self.origin
        #print(direction.magnitude())
        return Ray(pixel, direction) #starting at image plane, instead of camera

class TestCam:
    def __init__(self, origin, look, up, fov, aspectRatio):
        self.origin = origin
        self.fov = fov * pi / 180 #converting fov from degrees to radians
        #half the width and height of image plane - based off the field of view
        self.halfHeight = tan(self.fov / 2)
        self.halfWidth = self.halfHeight * aspectRatio
        #basis vectors for the camera coordinates
        self.w = ((origin - look).normalize())
        self.u = (up.cross(self.w)).normalize()
        self.v = self.w.cross(self.u)
        #print("w", self.w)
        #print("u", self.u)
        #print("v", self.v)
        #mapping to the image plane
        self.lowerLeft = self.origin - (self.halfWidth * self.u) - (self.halfHeight * self.v) - self.w
        self.horizontal = 2 * self.halfWidth * self.u
        self.vertical = 2 * self.halfHeight * self.v
        #print("horizontal", self.horizontal)
        #print("vertical", self.vertical)

    def send_ray(self, i, j):
        h = self.horizontal
        v = self.vertical
        #print(i)
        # print(h)
        # print(i * self.horizontal)
        # print(j)
        # print(v)
        # print(j * self.vertical)
        p = self.lowerLeft + (i * self.horizontal) + (j * self.vertical) - self.origin
        d = p - self.origin
        return Ray(self.origin, d)
'''
class Camera:
    def __init__(self, origin, imageWidth, imageHeight, fov):

        self.origin = origin
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.aspectRatio = self.imageWidth / self.imageHeight
        self.fov = fov * pi / 180 #converting fov from degrees to radians

    def send_ray(self, i, j):
        #mapping to [0, 1]
        x = (i + 0.5) / self.imageWidth
        y = (j + 0.5) / self.imageHeight
        #mapping to range [-1, 1]
        pix_x = 2 * x - 1
        pix_y = 1 - 2 * y
        #scaling by aspectRatio and field of view (fov)
        scaled_x = pix_x * self.aspectRatio * (tan(self.fov/2))
        scaled_y = pix_y * (tan(self.fov/2))

        p = Vector(scaled_x, scaled_y, -1/tan(self.fov))
        d = p - self.origin
        d.normalize()
        return Ray(self.origin, d)
