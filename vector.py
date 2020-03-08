#vector.py - used for vectors and colors
from math import sqrt

class Vector:
    #### Vector() -> creates a vector object in the scene ###
    #### params: x, y, z coordinates                      ###
    #### can also be used for RGB values                  ###
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        #length
        self.mag = sqrt(self.dot(self))
    def componenets(self):
        return (self.x, self.y, self.z)

    def __str__(self):
        return "(%f, %f, %f)" % (self.x, self.y, self.z)
    def __add__(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def __sub__(self, vec):
        return Vector(self.x - vec.x, self.y - vec.y, self.z - vec.z)

    def __mul__(self, s):
        if isinstance(s, Vector):
            print("Can't * multiply by vector, try cross or dot.")
            return self
        self.x = self.x * s
        self.y = self.y * s
        self.z = self.z * s
        return self

    def __rmul__(self, s):
        if isinstance(s, Vector):
            print("Can't * multiply by vector, try cross or dot.")
            return self
        #print("sdfs", self.x)
        self.x = self.x * s
        #print("Heyyyy! ", self.x)
        self.y = self.y * s
        self.z = self.z * s
        return self

    def __truediv__(self, s):
        self.x = self.x / s
        self.y = self.y / s
        self.z = self.z / s
        return self
    def greaterThanZero(self):
        if self.x > 0 or self.y > 0 or self.z > 0:
            return True
        return False
    def dot(self, vec):
        return self.x * vec.x + self.y * vec.y + self.z * vec.z

    def cross(self, vec):
        x = self.y * vec.z - self.z * vec.y
        y = self.z * vec.x - self.x * vec.z
        z = self.x * vec.y - self.y * vec.x
        return Vector(x,y,z)

    def magnitude(self):
        self.mag = sqrt(self.dot(self))
        return self.mag

    def normalize(self):
        magnitude = self.mag
        if magnitude > 0:
            self.x = self.x / magnitude
            self.y = self.y / magnitude
            self.z = self.z / magnitude
            self.magnitude()
            return self
    def round(self):
        self.x = int(self.x)
        self.y = int(self.y)
        self.z = int(self.z)
        return self
    def map(self):
        if self.x > 255:
            self.x = 255
        if self.x < 0:
            self.x = 0

        if self.y > 255:
            self.y = 255
        if self.y < 0:
            self.y = 0

        if self.z > 255:
            self.z = 255
        if self.z < 0:
            self.z = 0
        return self

    def colormap(self):
        self.x = int(self.x * 255)
        self.y = int(self.y * 255)
        self.z = int(self.z * 255)

        if self.x > 255:
            self.x = 255
        if self.x < 0:
            self.x = 0

        if self.y > 255:
            self.y = 255
        if self.y < 0:
            self.y = 0

        if self.z > 255:
            self.z = 255
        if self.z < 0:
            self.z = 0
        return self
