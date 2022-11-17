def detectCycle(numCourses: int, prereq: list[list[int]]) -> bool:
    # Setup Adj matrix, degree
    adj = [[] for i in range(len(prereq))]
    degree = [0] * (len(prereq))

    # Add vars to matrix:
    for u, v in prereq:
        print(f'({u}, {v})')
        adj[u - 1].append(v)
        degree[v] += 1
    
    

    # Loop through each course:
    for i in range(numCourses):
        pass
    return        
    

prereq = [[1, 0], [3, 2], [2, 1], [4, 0]]
credits = 2

print(detectCycle(credits, prereq))