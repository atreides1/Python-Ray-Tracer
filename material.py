import copy
from vector import Vector
class Material:
    def __init__(self, type, color, ka=0.075, kd=0, ks=0):
        self.type = type
        self.color = color
        #ambient, diffuse, and specular coefficients
        self.ka = ka
        self.kd = color
        self.ks = Vector(1.0, 1.0, 1.0)

        self.ambient_intensity = Vector(1.0, 1.0, 1.0) #for everything in scene

    def __str__(self):
        return self.type

    def baseColor(self):
        color = copy.deepcopy(self.color)
        return color.colormap()

    def reflect(self, obj, hitPoint, light, primaryRay):
        color = copy.deepcopy(self.color) #color of material at each point

        l = (light.loc() - hitPoint).normalize() #light vec (hp to light)
        v = -1 * ((primaryRay.getDirection()).normalize()) #viewer vec (hp to viewer)
        n = obj.normal(hitPoint)
        i_a = copy.deepcopy(self.ambient_intensity)

        if self.type == "Diffuse":
            #lambertian
            l_dot_n = l.dot(n)
            shade = (self.ka * i_a) + (self.kd * max(l_dot_n, 0))
            return shade.colormap()

        if self.type == "Specular":
            #phong
            '''
            shininess = 20
            self.ks = 0.7
            l_dot_n = max(0, l.dot(n))
            r = -l + (2 * l_dot_n * n)
            shade = (self.ka * i_a) + (self.kd * l_dot_n) + (self.ks * light.specular_intensity() * (r.dot(v)**shininess))
            return shade.colormap()
            '''
            #blinn-phong
            h = (l + v).normalize() #halfway vector
            shininess = 200 #phong exponent
            self.ks = 0.8
            l_dot_n = max(0, l.dot(n))
            shade = (self.ka * i_a) + (self.kd * l_dot_n) + (self.ks * light.specular_intensity() * (h.dot(n)**shininess))
            return shade.colormap()

    def refract(self):
        pass
