import string


def main():
    input_str = "Yek CHaractere kheyli AJ!!IB ghA@*Rib Mine$#visim"
    input_str = remove_spaces(input_str)
    sort(input_str)


def sort(input_str):
    alphabet = []
    digits = []
    others = []
    for ch in input_str:
        if ch in string.ascii_letters:
            alphabet.append(ch)
        elif ch in string.digits:
            digits.append(ch)
        else:
            others.append(ch)
    print(''.join(others) +
          ''.join(sorted(digits)) +
          ''.join(sorted(alphabet, key=lambda s: s.lower())))


def remove_spaces(input_str):
    input_str = ''.join(input_str.split())
    return input_str


if __name__ == '__main__':
    main()
