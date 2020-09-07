def recursiveSum(num: int):
    if num == 0:
        return 0
    return num + recursiveSum(num-1)


if __name__ == "__main__":
    print(recursiveSum(6))
    print(recursiveSum(10))
