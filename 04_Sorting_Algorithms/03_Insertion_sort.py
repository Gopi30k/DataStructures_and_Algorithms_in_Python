def insertion_sort(arr: list):  # O(N)in best case O(N2) in worst case
    for i in range(1, len(arr)):
        currentVal = arr[i]
        j = i-1
        while j >= 0 and currentVal < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = currentVal
    return arr


if __name__ == '__main__':
    print(insertion_sort([6, 2, 4, 7, 89, 0, 45]))
    print(insertion_sort([2, 1, 9, 76, 4]))

# Time Complexity                      | Space Complexity
# Best-Case  Average-Case  Worst-Case  |
#   O(n)        O(n2)         O(n2)    |     O(1)
