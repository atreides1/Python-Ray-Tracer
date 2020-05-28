class Object:
    def __init__(self, material):
        self.material = material
        self.type = None

    def __str__(self):
        return self.type

    def hit(self, ray):
        return

class Plane(Object):
    def __init__(self, p0, p1, normal, material):
        Object.__init__(self, material)
        self.type = "plane"
        self.p0 = p0
        self.p1 = p1
        self.n = normal

    def hit(self, ray):
        pass
