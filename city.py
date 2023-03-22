
class City:
    def __init__(self, num):
        self.number = num
        self.roads = []

    def addRoad(self, goalCity):
        self.roads.append(goalCity);

    