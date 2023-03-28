def assign_roads_to_cities(num_cities, roads):
    assigned_roads = []
    city_used = [False] * (num_cities + 1)

    for road in roads:
        city1, city2 = road
        if not city_used[city1] and not city_used[city2]:
            assigned_roads.append(road)
            city_used[city1] = True
            city_used[city2] = True

    return assigned_roads


def main():
    num_cities = int(input());
    roads = [];

    for i in range(num_cities):
        connection_line = input().split(" ")
        a = int(connection_line[0])
        b = int(connection_line[1])
        roads.append((a, b))

    #print(num_cities)
    #print(roads);

    assigned_roads = assign_roads_to_cities(num_cities, roads)

    for road in assigned_roads:
        print(road[0], road[1])


main()