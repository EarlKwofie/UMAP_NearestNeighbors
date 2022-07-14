import numpy as np

def traverse(adjacency_matrix, startNodeNum, visited):
    x= adjacency_matrix.shape
    size = x[0]
    #mark starting node as visited
    visited[startNodeNum] = True 
    for i in range(0,size):
        if adjacency_matrix[startNodeNum][i] and not visited[i]:
                traverse(adjacency_matrix, i,visited)

def isConnected(adjacency_matrix):
    x= adjacency_matrix.shape
    size = x[0]
    visited = [False for i in range(0, size)]
    for i in range(0,size):
        for j in range(0, size):
            visited[j] = False
            traverse(adjacency_matrix,i, visited)
        for i in range(0, size):
            if not visited[i]:
                print("The Graph is Not Connected")
                return False
        
            print("The Graph is Connected")
            return True

adjM = np.array([[0,0,0,0,0],[0,0,1,1,0], [0,1,0,1,1], [0,1,1,0,1], [0,0,1,1,0]])
print(adjM)

isConnected(adjM)