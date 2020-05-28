class Ray:
    #### Ray() -> creates a ray object in the scene ###
    #### params: origin point, direction vector ###
    def __init__(self, origin, direction, spectrum=None):
        self.o = origin
        '''
        if direction.mag != 1.0:
            direction.normalize()
        '''
        self.d = direction
        #self.spectrum = spectrum

    def getDirection(self):
        return self.d

    def __str__(self):
        return "origin: " + self.o.__str__() + "  " + "direction: " + self.d.__str__()
    # t is the distance
    def pointAtDistance(self, t):
        return self.o + self.d * t
