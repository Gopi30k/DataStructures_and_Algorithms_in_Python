def frequencyCounterPattern(arr1: list, arr2: list):  # O(n)
    freqCounter_1 = {}
    freqCounter_2 = {}
    for i in arr1:
        freqCounter_1[i] = freqCounter_1[i] + \
            1 if i in freqCounter_1.keys() else 1
    for i in arr2:
        freqCounter_2[i] = freqCounter_2[i] + \
            1 if i in freqCounter_2.keys() else 1
    for key in freqCounter_1.keys():
        if key ** 2 not in freqCounter_2.keys():
            return False
        elif freqCounter_2[key**2] != freqCounter_1[key]:
            return False
    return True


if __name__ == "__main__":
    print(frequencyCounterPattern([1, 1, 2, 3], [9, 1, 1, 4]))
