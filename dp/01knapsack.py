import numpy as np

def knapsack(p: list[int], w: list[int], m: int):
    # Create bag that is length of price/weight + 1 by bag weight + 1
    bag = [[0 for m in range(m + 1)] for p in range(len(p) + 1)] 
    
    for i in range(len(p) + 1): # looping rows --> ie. price and weight 
        for j in range(m + 1): # looping cols --> ie. bag weights 0, 1, ..., m 
            if i == 0 or j == 0: # if either index 0 --> profit at that index is 0
                bag[i][j] = 0
            elif w[i - 1] <= j: # If weight of var <= current bag weight --> add the max() to bag
                bag[i][j] = max(bag[i-1][j], p[i-1]+ bag[i-1][j-w[i-1]]) 
            else: 
                bag[i][j] = bag[i - 1][j] 

    return bag

# Driver Code:
price = [1, 2, 5, 6]
weight = [2, 3, 4, 5]
maxWeight = 8
bag = knapsack(price, weight, maxWeight)
print(f'Current Bag:\n {np.array(bag)} \n --------------------')

# Printing Selected Weights
maxProfit = bag[len(bag) - 1][maxWeight]
selectedWeights = []
for i in range(len(bag) -1, 0, -1):
    if maxProfit != bag[i - 1][maxWeight]:
        selectedWeights.append(weight[i - 1])
        maxWeight -= weight[i - 1]
        maxProfit -= price[i - 1]

print(f'Folloing weights optimizes profit from bag: {selectedWeights}')