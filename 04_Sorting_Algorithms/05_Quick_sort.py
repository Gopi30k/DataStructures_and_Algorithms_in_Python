def pivot(arr: list, start=0, end=None):
    print(arr)
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
    if left < right:
        pivotIndex = pivot(arr, left, right)
        quickSort(arr, left, pivotIndex-1)
        quickSort(arr, pivotIndex+1, right)
        # print(arr)
    return arr


if __name__ == '__main__':
    print(quickSort([4, 8, 2, 1, 5, 7, 6, 3]))
    print(quickSort([4, 6, 9, 1, 2, 5]))
