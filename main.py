# ---------------------------------------------------------
# Data class for the city (only city number)
# ---------------------------------------------------------
class City:
    def __init__(self, city_num):
        self.num = city_num
        self.edges = []


# ---------------------------------------------------------
# Data class for the edge. Only the two cities that are connected
# ---------------------------------------------------------
class Edge:
    def __init__(self, city1, city2):
        self.city1 = city1
        self.city2 = city2
        self.owner = None;


# ---------------------------------------------------------
# Method for creating a unique edge.
# @param unique_edge_list - A list of edges in the form of tuples. That 
#                          help us determine if they an edge has been added
# @param city1 - The first city node connected to the edge
# @param city2 - The second city node connected to the edge
# @return - The new (non duplicate) edge
# ---------------------------------------------------------
def create_edge(city1, city2):
    new_edge = Edge(city1, city2);
    return new_edge;

    # new_edge_tuple = (city1.num, city2.num)
    # new_edge = Edge(city1, city2)
    # Check if the edge we are attempting to add has already been added
    # if new_edge_tuple in unique_edge_list:
    #   new_edge_tuple = (city2.num, city1.num)
    #   new_edge = Edge(city2, city1)
    # unique_edge_list.append(new_edge_tuple)
    # return new_edge


def get_city(cities, city_num):
    if cities[city_num]:
        return cities[city_num]
    else:
        c = City(city_num)
        cities[city_num] = c
        return c


def main():
    edges = []
    citiesDic = {}
    num_cities = int(input())
    # List for keeping track of which edges have been added already
    unique_edge_list = []
    # Gathering input and creating each edge
    for i in range(num_cities):
        connection_line = input().split(" ")
        a = int(connection_line[0])
        b = int(connection_line[1])
        city_a = get_city(citiesDic, a)
        city_b = get_city(citiesDic, b)
        new_edge = create_edge(city_a, city_b)
        edges.append(new_edge)

    for edge in edges:
        city1 = edge.city1
        city2 = edge.city2
        # Print out for each unique connection
        print("{} {}".format(city1.num, city2.num))


main()
