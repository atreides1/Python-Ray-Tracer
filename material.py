import copy
class Material:
    def __init__(self, type, color, ka=1, kd=0, ks=0):
        self.type = type
        self.color = color
        #ambient, diffuse, and specular coefficients
        self.ka = ka
        self.kd = kd
        self.ks = ks

    def __str__(self):
        return self.type

    def reflect(self, hitPoint, normal, eyeRay, lightSource):
        shadowRay = (hitPoint, lightSource - hitPoint) #ray to light
        color = copy.deepcopy(self.color) #color of material at each point
        lightVec = -1 * (lightSource - hitPoint).normalize() #light vec
        viewing = (eyeRay.o - hitPoint).normalize() #viewer vec

        if self.type == "Diffuse":
            self.kd = 1
            #lambertian
            rounded_dot = lightVec.dot(normal)
            shade = kd * max(rounded_dot, 0) * color
            return (shade.round()).map()
        if self.type == "Specular":
            #phong
            k = 0.2
            self.kd = 0.2
            self.ks = 0.8
            r = (lightVec) + 2*(lightVec.dot(normal) * normal)
            reflection = (r - hitPoint).normalize()
            nDot_l = min(1, lightVec.dot(normal))

            shade = (self.kd * max(lightVec.dot(normal), 0) + self.ks * (reflection.dot(viewing)**2)) * color
            return shade.colormap()
            #blinn-phong
            #take the dot product of n and halfway vector, raise it to p
            #halfway = (viewing + lightVec) / (viewing.magnitude() + lightVec.magnitude())
            #p = 2
            #shade = (self.kd * max(lightVec.dot(normal), 0) + self.ks * ((halfway.dot(normal)) ** p)) * color
            #return (shade.round()).map()

    def refract(self):
        pass
