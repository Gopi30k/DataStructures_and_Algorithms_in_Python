def naivePower(base: int, exponent: int):
    power = 1
    for _ in range(0, exponent):
        power = power*base
    return power


def recursivePower(base: int, exponent: int):
    if exponent == 0:
        return 1
    return base * recursivePower(base, exponent-1)


if __name__ == "__main__":
    print(naivePower(2, 4))
    print(naivePower(3, 2))
    print(naivePower(2, 0))
    print(recursivePower(2, 4))
    print(recursivePower(3, 2))
    print(recursivePower(2, 0))
