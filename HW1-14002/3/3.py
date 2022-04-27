def main():
    num = parse_input()
    stars_coordinates = find_stars(num)
    x, y = stars_coordinates[-1]
    print(x, y)
    draw(num, stars_coordinates)


def find_stars(num):
    coordinates = []
    for i in range(1, num + 1):
        x, y = find_x_y(i)
        coordinates.append((x, y))
    return coordinates


def draw(num, stars_coordinates):
    mat = create_pixels(num)
    insert_stars(mat, num, stars_coordinates)

    for row in mat:
        print("".join(row))


def insert_stars(mat, num, stars_coordinates):
    for x, y in stars_coordinates:
        if num % 4 == 0 or num % 4 == 1:
            mat[num // 2 - 2 * y][num // 2 + 2 * x] = "* "
        if num % 4 == 2:
            mat[num // 2 - 1 - 2 * y][num // 2 - 1 + 2 * x] = "* "
        if num % 4 == 3:
            mat[num // 2 + 1 - 2 * y][num // 2 - 1 + 2 * x] = "* "


def create_pixels(num):
    if num % 2 == 0:
        mat = [["  " for _ in range(num + 1)] for _ in range(num + 1)]
    else:
        mat = [["  " for _ in range(num)] for _ in range(num)]

    return mat


def find_x_y(num):
    x, y = 0, 0
    if num % 4 == 0:
        x, y = - num // 4, num // 4
    if num % 4 == 1:
        x, y = -(num - 1) // 4, -(num - 1) // 4
    if num % 4 == 2:
        x, y = (num + 2) // 4, -(num - 2) // 4
    if num % 4 == 3:
        x, y = (num + 1) // 4, (num + 1) // 4
    return x, y


def parse_input():
    num = input()
    num = int(num)
    return num


if __name__ == '__main__':
    main()
