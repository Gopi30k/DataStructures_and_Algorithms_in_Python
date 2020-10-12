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
        digitBuckets = [0] * (10)
        print(digitBuckets)
        for i in range(0, len(numArr)):
            # print(numArr[i])
            digitPos = getDigitAtPos(numArr[i], k)
            # print(digitPos)
            # print(numArr[i])
            # print(digitBuckets[digitPos])
            digitBuckets.insert(digitPos, numArr[i])
        print(digitBuckets)
        # print(reversed(digitBuckets))
        # numArr = [].extend(digitBuckets)
        # print('--------')
        # print(numArr)


if __name__ == '__main__':
    # print(getDigitAtPos(2345, 3))
    # print(getDigitCount(2345))
    print(radixSort([23, 345, 5467, 12, 2345, 9852]))
