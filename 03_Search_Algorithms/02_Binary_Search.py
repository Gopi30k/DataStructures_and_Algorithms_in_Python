def binary_search_iterative(arr: list, search_item):
    left = 0
    right = len(arr)-1
    while left <= right:
        # middle = left + (right - left) // 2
        middle = (left + right)//2
        if arr[middle] == search_item:
            return middle
        elif arr[middle] > search_item:
            right = middle - 1
        elif arr[middle] < search_item:
            left = middle + 1
    return -1


def binary_search_recursive(arr: list,  left, right, search_item):
    if right > left:
        middle = (left + right) // 2
        if arr[middle] == search_item:
            return middle
        elif arr[middle] > search_item:
            return binary_search_recursive(arr, left, middle-1, search_item)
        else:
            return binary_search_recursive(arr, middle+1, right, search_item)
    else:
        return -1


if __name__ == '__main__':
    test_arr_1 = [1, 4, 6, 8, 11, 15, 23, 29,
                  42, 47, 50, 55, 61, 67, 74, 77, 80, 100]
    test_arr_2 = [2, 5, 6, 9, 13, 15, 28, 30]
    print(binary_search_iterative(test_arr_1, 67))
    print(binary_search_iterative(test_arr_2, 155))

    print(binary_search_recursive(test_arr_1, 0, len(test_arr_1),67))
    print(binary_search_recursive(test_arr_2, 0, len(test_arr_2),0))
