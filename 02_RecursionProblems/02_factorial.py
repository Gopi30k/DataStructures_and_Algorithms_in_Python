def recursiveFctorial(num:int):
    if num == 1 or num == 0:
        return 1
    return num * recursiveFctorial(num-1)
if __name__ == "__main__":
    print(recursiveFctorial(5))
    print(recursiveFctorial(0))