# Two Pointer Iterating
def uniqueArrayCounter(arr: list):  # O(n)
    i = 0
    if len(arr) == 0:
        return i
    for j in range(0, len(arr)):
        if arr[i] != arr[j]:
            i = i+1
            arr[i] = arr[j]
    # print(arr[0:i+1]) # unique array 
    return i + 1


if __name__ == "__main__":
    print(uniqueArrayCounter([1, 2, 3, 4, 4, 4, 7, 7, 7, 12, 12, 13]))
    print(uniqueArrayCounter([]))
