"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, 
its entire row and column are set to 0.
"""

def zeroMatrix(matrix):

    if len(matrix) < 1:
       return matrix

    M = len(matrix)
    N = len(matrix[0])
    
    solnMatrix = [row[:] for row in matrix]
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                for l in range(M):
                    solnMatrix[l][j] = 0
                solnMatrix[i][0:N] = [0]*N
           
    return solnMatrix

testMatrix = [[1,2,3,4], [0,1,3,6], [2,0,1,3]]
print(zeroMatrix(testMatrix))