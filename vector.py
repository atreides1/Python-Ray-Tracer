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
        self.mag = self.magnitude()#sqrt(self.dot(self)) #length

    def components(self):
        return (self.x, self.y, self.z)

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getZ(self):
        return self.z

    def __str__(self):
        return "(%f, %f, %f)" % (self.x, self.y, self.z)

    #### +,-,*,/ ops with two vectors produces a separate vector
    def __add__(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def __sub__(self, vec):
        return Vector(self.x - vec.x, self.y - vec.y, self.z - vec.z)

    def __mul__(self, s):
        if isinstance(s, Vector):
            print("Can't * multiply by vector, try cross or dot.")
            return self
        return Vector(self.x * s, self.y * s, self.z * s)

    def __rmul__(self, s):
        return self.__mul__(s)

    def __truediv__(self, s):
        return Vector(self.x / s, self.y / s, self.z / s)

    def __neg__(self):
        self.x = -1 * self.x
        self.y = -1 * self.y
        self.z = -1 * self.z
        return self

    ### +=, -=, *=, /= ops with a vector and scalar modify the original vector
    def __iadd__(self, s):
        self.x = self.x + s
        self.y = self.y + s
        self.z = self.z + s
        return self

    def __isub__(self, s):
        self.x = self.x - s
        self.y = self.y - s
        self.z = self.z - s
        return self

    def __imul__(self, s):
        self.x = self.x * s
        self.y = self.y * s
        self.z = self.z * s
        return self

    def __idiv__(self, s):
        self.x = self.x / s
        self.y = self.y / s
        self.z = self.z / s
        return self

    def dot(self, vec):
        return self.x * vec.x + self.y * vec.y + self.z * vec.z

    def cross(self, vec):
        x = self.y * vec.z - self.z * vec.y
        y = self.z * vec.x - self.x * vec.z
        z = self.x * vec.y - self.y * vec.x
        return Vector(x,y,z)

    def magnitude(self):
        mag = sqrt(self.dot(self))
        if round(mag) == 1:
            mag = 1.0
        self.mag = mag
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

    #clamp values to a low and high val
    def clamp(self, low, high):
        if self.x > high:
            self.x = high
        if self.x < low:
            self.x = low

        if self.y > high:
            self.y = high
        if self.y < low:
            self.y = low

        if self.z > high:
            self.z = high
        if self.z < low:
            self.z = low
        return self

    def colormap(self):
        #maps and returns components
        self.x = int(self.x * 255)
        self.y = int(self.y * 255)
        self.z = int(self.z * 255)
        #could just call clamp() after this
        self = self.clamp(0, 255)
        return self.components()

    def map(self, x, low, high):
        #x is in range [a, b] = low, high
        #we want y in  [c,d] = [0, 255]
        # y = (x-a) * ((d-c)/ (b-a)) + c
        y = (x - low) * (255/(high-low))

    def greaterThanZero(self):
        if self.x > 0 or self.y > 0 or self.z > 0:
            return True
        return False
