def bubble_sort_naive(arr: list):  # O(n**2)
    length = len(arr)
    for i in range(0, length):
        for j in range(0, length):
            if j+1 < length and arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)


def bubble_sort(arr: list):  # O(n**2)
    length = len(arr)
    for i in range(length, 0, -1):
        for j in range(0, i-1):
            print(arr,arr[j],arr[j+1])
            if arr[j] > arr[j+1]:
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]]
    print(arr)


# If Nearly Sorted Array O(N)(Approx. on best case)
def bubble_sort_optimized(arr: list):
    length = len(arr)
    swapFlag = True
    for i in range(length, 0, -1):
        swapFlag = True
        for j in range(0, i-1):
            print(arr,arr[j],arr[j+1])
            if arr[j] > arr[j+1]:
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]]
                swapFlag = False
        if swapFlag:
            break

    print(arr)


if __name__ == '__main__':
    # bubble_sort_naive([5, 3, 4, 1, 2])
    # bubble_sort([5, 3, 4, 1, 2])
    bubble_sort([8, 1, 2, 3, 4, 5, 6])
    print('### optimized on nearly Sorted array ###')
    bubble_sort_optimized([8, 1, 2, 3, 4, 5, 6])
