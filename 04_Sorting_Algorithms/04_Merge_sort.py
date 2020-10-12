def merge(arr1: list, arr2: list):
    results = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            results.append(arr1[i])
            i += 1
        else:
            results.append(arr2[j])
            j += 1

    while i < len(arr1):
        results.append(arr1[i])
        i += 1

    while j < len(arr2):
        results.append(arr2[j])
        j += 1
    return results


def mergeSort(arr: list):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)


if __name__ == '__main__':
    print(mergeSort([10, 24, 76, 23, 56, 1, 5, 9]))


# Time Complexity                        | Space Complexity
# Best-Case    Average-Case  Worst-Case  |
# O(n log n)    O(n log n)     O(n log n)  |     O(n)
