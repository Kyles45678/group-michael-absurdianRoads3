# ---------------------------------------------------------
# Data class for the city (only city number)
# ---------------------------------------------------------
class City:
    def __init__(self, city_num):
        self.num = city_num
        self.connectedCities = []
        self.numConnected = 0;
        self.visited = False;

    def toString(self):
        ending = ""
        for c in self.connectedCities:
            ending += str(c.num) + ","
        ending = ending.rstrip(",");
        return "City: " + str(self.num) + \
            " | Num Connections: " + str(self.numConnected) + \
            " | Connections: [" + ending + "]"

    def removeFirstConnectionIfExists(self, city):
        indexToRemove = None;
        for i in range(len(self.connectedCities)):
            if city.num == self.connectedCities[i].num:
                indexToRemove = i
                break
        if indexToRemove is not None:
            del self.connectedCities[indexToRemove]


def get_city(cities, city_num):
    if cities.get(city_num):
        return cities.get(city_num)
    else:
        c = City(city_num)
        cities[city_num] = c
        return c


def print_and_remove_leaves(citiesDic):
    stack = [];

    for k, city in citiesDic.items():
        if city.numConnected == 1:
            stack.append(k)

    while len(stack) > 0:
        curr = stack[-1]
        stack.pop()

        for adjacentCity in citiesDic[curr].connectedCities:
            adjacentCity.numConnected -= 1
            if adjacentCity.numConnected == 1:
                stack.append(adjacentCity)
            print(citiesDic[curr].num, adjacentCity.num)

        for city in citiesDic.values():
            city.removeFirstConnectionIfExists(citiesDic[curr])

        citiesDic.pop(curr)


def print_and_remove_loops(citiesDic, startCityKey):
    stack = []
    stack.append(startCityKey);

    while len(stack) > 0:
        curKey = stack[-1]
        stack.pop()

        for i in range(len(citiesDic[curKey].connectedCities)):
            adC = citiesDic[curKey].connectedCities[i]
            if adC.visited is not True:
                stack.append(adC.num)
                adC.visited = True
                print(citiesDic[curKey].num, adC.num)
                break;

    #TODO minimum spanning tree

    for i in range(len(citiesDic[startCityKey].connectedCities)):
        adC = citiesDic[curKey].connectedCities[i]
        if adC.visited is not True:
            print(adC.num, citiesDic[startCityKey].num)
            break

    #currCity = citiesDic.get(cityKey)
    #if currCity is None: return
    #print(currCity.connectedCities)
    #if len(currCity.connectedCities) <= 0: return
    #firstAdjacentCity = currCity.connectedCities[0]

    #print(currCity.num, firstAdjacentCity.num)

    #for city in citiesDic.values():
    #    city.removeFirstConnectionIfExists(citiesDic[cityKey])

    #citiesDic.pop(cityKey)



def main():
    citiesDic = {}

    num_cities = int(input())

    # Gathering input and creating each edge
    for i in range(num_cities):
        connection_line = input().split(" ")
        a = int(connection_line[0])
        b = int(connection_line[1])
        city_a = get_city(citiesDic, a)
        city_b = get_city(citiesDic, b)

        city_a.connectedCities.append(city_b)
        city_b.connectedCities.append(city_a)

        city_a.numConnected+=1
        city_b.numConnected+=1

    print_and_remove_leaves(citiesDic)

    #cityKeysAsArray = []
    #for k in citiesDic.keys():
    #    cityKeysAsArray.append(k)

    #for i in citiesDic:
    #    print(citiesDic[i].toString())

    #for ki in cityKeysAsArray:
    #    print_and_remove_loops(citiesDic, ki)
        #for i in citiesDic:
        #    print(citiesDic[i].toString())


main()
