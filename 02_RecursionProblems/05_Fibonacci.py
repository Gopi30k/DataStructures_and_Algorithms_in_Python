def fibonacci(num: int):
    if num <= 2:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)


if __name__ == "__main__":
    print(fibonacci(4))
    print(fibonacci(10))
    print(fibonacci(28))
    print(fibonacci(35))
