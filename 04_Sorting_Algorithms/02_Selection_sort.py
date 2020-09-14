def selection_sort(arr: list):  # O(n2)
    for i in range(0, len(arr)):
        lowest = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[lowest]:
                lowest = j
        if i != lowest:  # to check if minimum is already in correct position
            print(i, lowest)
            [arr[i], arr[lowest]] = [arr[lowest], arr[i]]
    print(arr)


if __name__ == '__main__':
    selection_sort([0, 2, 34, 22, 10, 19, 17])
