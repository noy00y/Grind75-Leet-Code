def maxSubArray(Arr: list[int]):
    # Call subAux:
    n = len(Arr)
    localMax = 0
    globalMax = -1000000

    for i in range(n):
        print(f'Arr[{i}] = {Arr[i]}, lMax = {localMax}, gMax: {globalMax}')
        localMax = max(Arr[i], Arr[i] + localMax)
        if localMax > globalMax: globalMax = localMax

    return globalMax
    
print(maxSubArray([-1]))
        