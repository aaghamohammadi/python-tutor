def is_magical(t):
    item = t[0]
    list_ = t[1]
    # your code goes here
    return False


if __name__ == '__main__':
    assert is_magical((3, [1, 5, 2, 7, 12, 5]))
    assert is_magical((7, [3, 23, 4]))
    assert is_magical((-3, [-17, 12, 14, 103]))
    assert not is_magical((4, [5, 1, 2, 1]))
    assert not is_magical((6, [5, 2, 7, 17]))
