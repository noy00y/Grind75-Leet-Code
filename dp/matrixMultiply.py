import numpy as np

def findChain(p: list[list[int]]):
    n = len(p)
    m = [[0]*n]*n
    s = [[0]*n]*n

    for i in range(n):
        for j in range(n):
            if i < j:
                print("--------------------------------------------------------------------------")
                # print(f'[{i}, {j}]')
                m[i][j] = 10000000
                for k in range(i, j):
                    m[i][j] = m[i][k] + m[k + 1][j] + p[i][0] * p[k][1] * p[j][1]
                    s[i][j] = k
    return m, s

# Driver Code:
Arr = [
    [3, 2], 
    [2, 4],
    [4, 2], 
    [2, 5],
]

m, s = findChain(Arr)
print("--------------------------------------------------------------------------")
print(f'm: \n{np.array(m)}')
print(f's: \n{np.array(s)}')