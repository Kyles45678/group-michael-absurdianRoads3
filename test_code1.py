def single_connection(graph, a, b):
    graph[a][b] = True
    if not graph[a].get("connections"):
        graph[a]["connections"] = []
    if b not in graph[a]["connections"]:
        graph[a]["connections"].append(b)


def apply_connection(graph, index_a, index_b):
    single_connection(graph, index_a, index_b)
    single_connection(graph, index_b, index_a)


def print_and_remove_leaves(graph):
    cities_to_remove = []

    for cityNum, cityConnections in graph.items():
        if sum(cityConnections["connections"]) == 1:
            cities_to_remove.append(cityNum)
            print(cityNum, cityConnections["connections"][0])


    for i in cities_to_remove:
        graph.pop(i)
        #for _, oCc in graph.items():
        #    if cityNum in oCc["connections"]: oCc["connections"].remove(cityNum)
        #    if oCc.get(cityNum) is not None: oCc.pop(cityNum)



def remove_connections_from_last_except_one(graph):
    last_key = sorted(graph.keys())[-1]
    cityConns = graph[last_key];
    remove_conns = []
    connToKeep = None

    for cityNum, val in cityConns.items():
        if cityNum != "connections":
            if val:
                if not connToKeep:
                    connToKeep = cityNum;
                elif connToKeep:
                    remove_conns.append(cityNum)

    for i in remove_conns:
        cityConns[i] = False
    cityConns["connections"] = [connToKeep]

def print_cycles(graph):
    for i, conns in enumerate(graph):
        cityNum = i + 1
        conns = graph[i]
        if sum(conns) > 1:  # this isn't a leaf
            print(cityNum, conns.index(1) + 1)


def main():
    graph = {};

    num_cities = int(input())

    for i in range(num_cities):
        row = {}
        for i2 in range(num_cities):
            row[i2 + 1] = False
        graph[i + 1] = row

    print(graph)

    for i in range(num_cities):
        connection_line = input().split(" ")
        a = int(connection_line[0])
        b = int(connection_line[1])
        apply_connection(graph, a, b)

    print(graph)

    #while len(graph.keys()) > 0:
    #print("before", graph)
    print_and_remove_leaves(graph)

    print(graph)

main()
