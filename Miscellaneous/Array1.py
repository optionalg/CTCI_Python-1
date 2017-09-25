"""
Given an array, return the k-largest elements
"""

def kLargestElements(arr, k):
    if k > len(arr):
        return "Not enough elements in the array."

    elements = []
    arr.sort()

    for i in range(len(arr)-k, len(arr)):
        elements.append(arr[i])

    return elements

def main():
    arr = [-3, 40, 23, 50, 0, 23, 691, 495, -185, -351, 310, 1]
    k = 3
    print("Find the",k,"largest elements in the following array:")
    print(arr)
    print("Result:", kLargestElements(arr, k))

main()