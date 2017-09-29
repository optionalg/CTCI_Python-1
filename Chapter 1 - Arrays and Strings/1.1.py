"""
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

"""
Using a dictionary (hashmap)
Time efficiency: O(n)
Space efficiency: O(n)
"""
def isUniqueStringDict(str):
    charFreq = {}

    for char in str:
        if char in charFreq:
            return False
        else:
            charFreq[char] = True

    return True


""" 
Using no additional data structures
Assuming ASCII character set
Time efficiency: O(n)
Space efficiency: O(1)
"""
def isUniqueString(str):
    asciiMap = [False] * 256
    for char in str:
        val = ord(char) #Convert character to integer
        if asciiMap[val]:
            return False
        else:
            asciiMap[val] = True

    return True

def main():
    str = "pythonic"
    print("Is the string", str, "unique?")
    print("Result:", isUniqueString(str))

main()