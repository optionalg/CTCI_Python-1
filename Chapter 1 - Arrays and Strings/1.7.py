"""
Rotate Matrix: 
Given an image represented by an NxN matrix,write a method to rotate the image by 90 degrees. 
Can you do this in place?
"""


def rotateNotInPlace(matrix):
    if len(matrix) <= 1:
        return matrix

    newMatrix = [row[:] for row in matrix]
    N = len(matrix)
    for i in range(N):
        for j in range(N):
            newMatrix[j][N-1-i] = matrix[i][j]

    return newMatrix

def rotateInPlace(matrix):
    if len(matrix) <= 1:
        return matrix

    N = len(matrix
    for i in range(N):
        for j in range(N):
            
testMatrix = [[1,2,3], ["a", "b", "c"], ["@", "!", "%"]]
print(rotateNotInPlace(testMatrix))
print(rotateInPlace(testMatrix))