def controller():
    x = parse_int()
    outs = compute(x)
    print_results(outs)


def print_results(outs):
    for element in outs:
        print(element)


def compute(x):
    outs = []
    for _ in range(x):
        reach_star = False
        n, k = 100, 2
        while not reach_star:
            inp = input()
            if inp == "*":
                reach_star = True
                outs.append(josephus(n, k))
            elif inp == "n":
                n = parse_int()
            elif inp == "k":
                k = parse_int()
    return outs


def parse_int():
    return int(input())


def g(n, k):
    if n == 1:
        return 0
    return (g(n - 1, k) + k) % n


def josephus(n=100, k=2):
    return g(n, k) + 1


if __name__ == '__main__':
    controller()
