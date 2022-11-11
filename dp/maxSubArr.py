def crossArr(Arr: list[int], low: int, mid: int, high: int):
    leftSum = -10000
    rightSum = -10000
        
    # Left:
    sum = 0
    for i in range(low, mid):
        sum += Arr[i]
        if sum > leftSum:
            leftSum = sum 
            maxLeft = i
        
    # Right
    sum = 0
    for i in range(mid + 1, high):
        sum += Arr[i]
        if sum > rightSum: 
            rightSum = sum 
            maxRight = i
                
    return maxLeft, maxRight, leftSum + rightSum
    
def maxAux(Arr: list[int], low: int, high: int):
    if low == high: 
        return low, high, Arr[low]
        
    # Divide the array in 3 parts and find whichever array will be the maximum
    # left, right or some mix in between
    else:
        mid = (low + high) / 2
        lLow, lHigh, leftSum = maxAux(Arr, low, mid) # Left Arr added to stack
        rLow, rHigh, rightSum = maxAux(Arr, mid + 1, high) # Right Arr added to stack
        cLow, cHigh, crossSum = crossArr(Arr, low, mid, high) # O(n) operation to get sum b/w left n right

        if (leftSum >= rightSum and leftSum >= crossSum):
            return lLow, lHigh, leftSum
        elif (rightSum >= leftSum and rightSum >= crossSum):
            return rLow, rHigh, rightSum
        
def maxSubArray(nums: list[int]) -> int:
    # Call subAux:
    low, high, sum = maxAux(nums, 0, len(nums))
    return sum
    
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
        