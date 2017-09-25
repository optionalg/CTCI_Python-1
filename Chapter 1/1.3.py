"""
URLify : Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold
the additional characters, and that you are given the "true" length of the string.
"""

def URLify(str):
    newStr = [" "] * len(str)

    for char in range(len(str)):
        if str[char] != " ":
            newStr[char] = str[char]
        else:
            newStr[char] = "%20"

    newStr = "".join(newStr) #Construct string to be equal to all elements in list appended together

    return newStr

def main():
    str = "  My name is "
    expected = "%20%20My%20name%20is%20"
    if (expected == URLify(str)):
        print("Success")
    else:
        print("Failure")

main()