import math


def getDigitAtPos(num: int, pos: int):
    # Math.floor(Math.abs(num) / Math.pow(10, i)) % 10
    return (abs(num) // 10 ** pos) % 10


def getDigitCount(num: int):
    if num == 0:
        return 1
    #  len(str(abs(num)))
    return math.floor(math.log10(abs(num)))+1


def getMaxDigitArr(numArr: list):
    maxDigit = 0
    for i in range(0, len(numArr)):
        maxDigit = max(maxDigit, getDigitCount(numArr[i]))
    return maxDigit


def radixSort(numArr: list):
    maxDigitnArr = getMaxDigitArr(numArr)
    for k in range(0, maxDigitnArr):
        digitBuckets = [[] for _ in range(10)]
        for i in range(0, len(numArr)):
            digitPos = getDigitAtPos(numArr[i], k)
            digitBuckets[digitPos].append(numArr[i])
        numArr = [num for nestedNumArr in digitBuckets for num in nestedNumArr]
    return numArr


if __name__ == '__main__':
    # print(getDigitAtPos(2345, 3))
    # print(getDigitCount(2345))
    print(radixSort([23, 345, 5467, 12, 2345, 9852]))

# Time Complexity                                       |   Space Complexity
#   Best-Case      |  Average-Case    |  Worst-Case    |
#   O(n log n)    |     O(n log n)   |  O(n2)         |        O(n log n)
