def productOfArray(arr: list):
    length = len(arr)
    if length == 0:
        return 1
    return arr[length-1] * productOfArray(arr[:-1])


if __name__ == "__main__":
    print(productOfArray([1, 2, 3, 10]))
