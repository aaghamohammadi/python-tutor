def main():
    x1, y1, x2, y2 = parse_input()
    print(slope(x1, y1, x2, y2))
    print(intercept(x1, y1, x2, y2))
    print(linear(x1, y1, x2, y2))


def linear(x1, y1, x2, y2):
    a = slope(x1, y1, x2, y2)
    b = intercept(x1, y1, x2, y2)
    if float(b) >= 0:
        return f"{a}x+{b}"
    return f"{a}x{b}"


def slope(x1, y1, x2, y2):
    if y1 - y2 == 0:
        return f"{0:.2f}"
    return f"{(y1 - y2) / (x1 - x2):0.2f}"


def intercept(x1, y1, x2, y2):
    if y1 * x2 == y2 * x1:
        return f"{0:.2f}"
    b = y1 - (y1 - y2) / (x1 - x2) * x1
    return f"{b:0.2f}"


def parse_input():
    line1 = input()
    line2 = input()
    x1, y1 = line1.split()
    x1, y1 = int(x1), int(y1)
    x2, y2 = line2.split()
    x2, y2 = int(x2), int(y2)
    return x1, y1, x2, y2


if __name__ == '__main__':
    main()
