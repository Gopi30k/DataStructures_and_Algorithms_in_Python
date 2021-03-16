# Two Pointer Iterating
def uniqueArrayCounter(arr: list):  # O(n)
    counter = 0
    if len(arr) == 0:
        return counter
    for pos, val in enumerate(arr):
        if arr[counter] != arr[pos]:
            counter = counter + 1
            arr[counter] = arr[pos]
    # print(arr[0:counter+1])  # unique array
    return counter + 1, arr[0:counter+1]


if __name__ == "__main__":
    print(uniqueArrayCounter([1, 2, 3, 4, 4, 4, 7, 7, 7, 12, 12, 13]))
    print(uniqueArrayCounter([1, 2, 3, 4, 4, 3, 1, 7, 6]))
    print(uniqueArrayCounter([]))
