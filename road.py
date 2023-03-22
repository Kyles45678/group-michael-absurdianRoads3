
class Road:
    def __init(self, cityA, cityB):
        self.cityA = cityA
        self.cityB = cityB
        self.builtCity = None

    def setBuiltCity(self, city):
        self.builtCity = city

    def getBuiltCity(self):
        return self.builtCity

    def hasBuiltCity(self):
        return self.builtCity is not None
