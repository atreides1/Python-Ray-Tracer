class Ray:
    #### Ray() -> creates a ray object in the scene ###
    #### params: origin point, direction vector ###
    def __init__(self, origin, direction):
        self.o = origin
        self.d = direction.normalize()
        self.tmin = 100
    # t is the distance
    def pointAtDistance(self, t):
        return self.o + self.d * t
