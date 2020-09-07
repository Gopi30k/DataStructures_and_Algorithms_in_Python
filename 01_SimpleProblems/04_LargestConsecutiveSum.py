# Sliding Window Problem
def naiveSolution(arr: list, num: int):  # O(n**2)
    if num > len(arr):
        return 0
    max = float('-inf')
    for i in range(0, len(arr)-num+1):
        temp = 0
        for j in range(0, num):
            temp = temp + arr[i+j]
        if temp > max:
            max = temp
    return max


def maxSumSubArray(arr: list, num: int):  # O(n)
    if num > len(arr):
        return 0
    tempSum = 0
    maxSum = 0
    for i in range(0, num):
        maxSum = maxSum + arr[i]

    tempSum = maxSum
    for i in range(num, len(arr)):
        tempSum = tempSum - arr[i-num] + arr[i]
        maxSum = tempSum if tempSum > maxSum else maxSum
    return maxSum


if __name__ == "__main__":
    print(naiveSolution([2, 6, 9, 2, 1, 8, 5, 6, 3], 3))
    print(maxSumSubArray([2, 6, 9, 2, 1, 8, 5, 6, 3], 3))
