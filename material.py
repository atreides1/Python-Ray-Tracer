import copy
from vector import Vector
class Material:
    def __init__(self, type, color, ka=0.0075, kd=0, ks=0, kr=0):
        self.type = type
        self.color = color
        #ambient, diffuse, and specular coefficients
        self.ka = ka
        self.kd = 0.7
        self.ks = 0.3#Vector(1.0, 1.0, 1.0)
        self.kr = 0.1 #reflectivity

        self.ambient_intensity = Vector(0.3, 0.3, 0.3) #for everything in scene
        self.ambient = Vector(0.01, 0.01, 0.01)

    def __str__(self):
        return self.type

    def baseColor(self):
        color = copy.deepcopy(self.color)
        return color

    def reflect(self, obj, hitPoint, light, primaryRay, occluded):
        if occluded:
            return self.ambient

        color = copy.deepcopy(self.color) #color of material at each point

        l = (light.loc() - hitPoint).normalize() #light vec (hp to light)
        v = -1 * ((primaryRay.getDirection()).normalize()) #viewer vec (hp to viewer)
        n = obj.normal(hitPoint)
        i_a = copy.deepcopy(self.ambient_intensity)

        if self.type == "Diffuse":
            #lambertian
            l_dot_n = l.dot(n)
            shade = (self.ka * i_a) + (self.kd * max(l_dot_n, 0) * self.color)
            return shade

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
            shade = (self.ka * i_a) + (self.kd * max(l_dot_n, 0) * self.color) + (self.ks * light.specular_intensity() * (h.dot(n)**shininess))
            return shade
        else:
            print("invalid material type.")
            return -1

    def refract(self):
        pass
