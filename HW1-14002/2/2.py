def main():
    n, m = parse_input()
    result = eratosthenes(n, m)
    return result


def parse_input():
    n = input()
    n = int(n)
    m = input()
    m = int(m)
    return n, m


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def least_factor(number):
    if number <= 1:
        return 1
    for i in range(2, number):
        if number % i == 0:
            return i


def eratosthenes(n, m):
    if is_prime(m):
        return -1
    count = 0
    for r in range(m):
        if not is_prime(r) and least_factor(r) <= least_factor(m):
            count += 1
    for r in range(m + 1, n + 1):
        if not is_prime(r) and least_factor(r) < least_factor(m):
            count += 1
    return count


if __name__ == '__main__':
    print(main())
