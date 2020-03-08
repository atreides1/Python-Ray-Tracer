from math import sqrt
class Sphere:
    #### Sphere() -> creates a sphere object in the scene ###
    #### params: center point, radius, material type ###
    def __init__ (self, center, radius, Material):
        self.c = center
        self.r = radius
        self.mat = Material

    def checkIntersect(self, Ray):
        v = Ray.o - self.c #vector from center of sphere to origin
        r = self.r
        # a = Ray.d.dot(d) = 1
        b = 2.0 * Ray.d.dot(v)
        c = (v.dot(v))- (r*r)
        discriminant = b*b - 4*c

        if discriminant >= 0:
            t = (-b - sqrt(discriminant)) / 2
            if t > 0:
                return t
            return None
