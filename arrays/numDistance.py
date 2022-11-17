def findDistance(Arr: list [int], x: int, y: int):
    distance = 0
    for i in range(len(Arr)):
        # Arr[y] < distance < Arr[x]:
        if x > y:
            if Arr[i] < x and Arr[i] > y:
                distance += 1

        # Arr[x] < distance < Arr[y]:
        elif y > x:
            if Arr[i] > x and Arr[i] < y:
                distance += 1

    return distance

Arr = [4, 5, 3, 1, 2]
distance = findDistance(Arr, 5, 1)
print(f'Final Distance: {distance}')