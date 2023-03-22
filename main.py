def main():
    num_citys = int(input())
    cities = [None for _ in range(num_citys)]
    for i in range(num_citys):
        connection_line = input().split(" ")
        a = int(connection_line[0])
        b = int(connection_line[1])

main()
