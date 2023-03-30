class City:
    def __init__(self, city_num):
        self.num = city_num
        self.conns = []
        self.uncheckedNeighbors = 0;
        self.visited = False;

    def __repr__(self):
        return "|" + str(self.num) + \
            ", " + str(self.conns) + \
            ", " + str(self.visited) + "|"

    def __str__(self):
        return "|" + str(self.num) + \
            ", " + str(self.conns) + \
            ", " + str(self.visited) + "|"


def print_and_mark_leaves(cities):
    leafCities = []

    # cities with a single connection are leaf graph nodes
    for c in cities:
        if c.uncheckedNeighbors == 1:
            leafCities.append(c)

    while len(leafCities) > 0:
        curCity = leafCities.pop()
        curCity.visited = True

        for neighborCityNum in curCity.conns:           # check the connected cities to our leaf city
            neighborCity = cities[neighborCityNum - 1]

            if not neighborCity.visited:

                # we haven't seen this leaf city yet, so use its connection up (print)
                print(curCity.num, neighborCity.num)

                # it could become a leaf node after this, so let's update it
                neighborCity.uncheckedNeighbors -= 1

                # after using up this connection, see if our neighbor city became a new leaf node. if so, check it
                if neighborCity.uncheckedNeighbors == 1:
                    leafCities.append(neighborCity)


def print_and_mark_loops(cities, start_city_index):
    loopCities = [start_city_index]
    lastCityIndex = None

    while len(loopCities) > 0:
        curCityIndex = loopCities.pop()
        curCity = cities[curCityIndex]

        # go through the neighbors of the city we're currently on
        for neighborCityNum in curCity.conns:
            neighborCity = cities[neighborCityNum - 1]

            # find the first neighbor city that wasn't visited yet, if any
            if not neighborCity.visited:
                curCity.visited = True  # use up the connection from our current to the neighbor
                print(curCity.num, neighborCity.num)
                loopCities.append(neighborCityNum - 1)  # continue the loop by adding the neighbor
                break  # now go check the neighbor's connections

        lastCityIndex = curCityIndex

    # we now need to finish the loop from our last city's neighbors to our starting city we need to check our start
    # and end index aren't the same city (happens when our start city has all neighbors visited already)
    if not cities[lastCityIndex].visited and lastCityIndex != start_city_index:
        print(cities[lastCityIndex].num, cities[start_city_index].num)


def main():
    num_cities = int(input())
    cities = []

    # create the cities (nodes) of our graph
    for i in range(num_cities):
        cities.append(City(i + 1))

    # connect our cities based on the next inputs
    for i in range(num_cities):
        connection_line = input().split(" ")
        a = int(connection_line[0])
        b = int(connection_line[1])
        cities[a - 1].conns.append(b)
        cities[b - 1].conns.append(a)
        cities[a - 1].uncheckedNeighbors += 1
        cities[b - 1].uncheckedNeighbors += 1

    # print("start", cities)

    print_and_mark_leaves(cities)

    # print("leafs", cities)

    for i in range(num_cities):     # we use this for loop to eliminate multiple loops
        if not cities[i].visited:
            print_and_mark_loops(cities, i)

    # print("loops", cities)


main()
