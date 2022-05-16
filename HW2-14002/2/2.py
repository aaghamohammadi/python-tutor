def main():
    n, m = parse_number_of_cities_airlines()
    cities = parse_cities(n)
    airlines = parse_air_lines(m)
    print_destinations(cities, airlines)


def print_destinations(cities, airlines):
    for city in cities:
        destinations = airlines.get(city, [])
        if destinations:
            print(len(destinations))
            for dest in destinations:
                print(dest)
        else:
            print(0)


def parse_cities(n):
    cities = [input() for _ in range(n)]
    return cities


def parse_air_lines(m):
    airlines = dict()
    for i in range(m):
        start, dest = input().split()
        destinations = airlines.get(start, [])
        destinations.append(dest)
        airlines[start] = destinations
    return airlines


def parse_number_of_cities_airlines():
    n, m = input().split()
    n = int(n)
    m = int(m)
    return n, m


if __name__ == '__main__':
    main()
