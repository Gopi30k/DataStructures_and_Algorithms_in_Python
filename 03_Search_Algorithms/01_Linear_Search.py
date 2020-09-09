def linear_search(arr: list, search_item):
    for i in range(0, len(arr)):
        if arr[i] == search_item:
            return i
    else:
        return -1


if __name__ == "__main__":
    print(linear_search([1, 43, 8, 2, 67, 23, 43, 88, 24], 85))
