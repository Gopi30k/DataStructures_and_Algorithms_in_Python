# Sliding Window Problem
def naiveSolution(arr: list, w_num: int):  # O(n**2)
    if w_num > len(arr):
        return 0
    max = float('-inf') # Greatest negative number
    for i in range(0, len(arr)-w_num+1):
        temp = 0
        for j in range(0, w_num):
            temp = temp + arr[i+j]
        if temp > max:
            max = temp
    return max


def maxSumSubArray(arr: list, w_num: int):  # O(n)
    if w_num > len(arr):
        return 0
    tempSum = 0
    maxSum = 0
    for i in range(0, w_num):
        maxSum = maxSum + arr[i]

    tempSum = maxSum
    for i in range(w_num, len(arr)):
        tempSum = tempSum - arr[i-w_num] + arr[i]
        maxSum = tempSum if tempSum > maxSum else maxSum
    return maxSum


if __name__ == "__main__":
    print(naiveSolution([2, 6, 9, 2, 1, 8, 5, 6, 3], 3))
    print(maxSumSubArray([2, 6, 9, 2, 1, 8, 5, 6, 3], 3))
