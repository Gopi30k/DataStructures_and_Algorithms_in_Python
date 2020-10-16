def pivot(arr: list, start=0, end=None):
    if end is None:
        end = len(arr)+1
    pivotEle = arr[start]
    swapIndex = start

    for i in range(start+1, len(arr)):
        if arr[i] < pivotEle:
            swapIndex += 1
            [arr[swapIndex], arr[i]] = [arr[i], arr[swapIndex]]
    [arr[start], arr[swapIndex]] = [arr[swapIndex], arr[start]]
    return swapIndex


def quickSort(arr: list, left=0, right=None):
    if right is None:
        right = len(arr)-1
    if left < right:  # Avoid Infinite loop : Left and right if same(1 element)
        pivotIndex = pivot(arr, left, right)
        # Finish Left SubArray
        quickSort(arr, left, pivotIndex-1)
        # Finish Right SubArray
        quickSort(arr, pivotIndex+1, right)
    return arr


if __name__ == '__main__':
    print(quickSort([4, 8, 2, 1, 5, 7, 6, 3]))
    print(quickSort([4, 6, 9, 1, 2, 5]))

# Time Complexity                                       |   Space Complexity
#   Best-Case      |  Average-Case    |  Worst-Case    |
#   O(nk)         |     O(nk)        |    O(nk)       |        O(n+k)
