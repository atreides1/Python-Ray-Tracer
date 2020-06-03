class Light:
    def __init__(self, location, i_d, i_s, type="point", color=(1,1,1)):
        self.location = location
        #diffuse and specular intensity (colors)
        self.i_d = 0.7
        self.i_s = i_s
        #etc
        self.type = type
        self.color = color

    def loc(self):
        return self.location

    def diffuse_intensity(self):
        return self.i_d

    def specular_intensity(self):
        return self.i_s
