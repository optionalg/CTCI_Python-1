"""
Check Permutation: Given two strings,write a method to decide if one is a permutation of the
other.
"""

def isStringPermutation(str1, str2):
    if len(str1) != len(str2):
        return False

    lettersFreq = {}
    for letter in str1:
        if letter not in lettersFreq:
            lettersFreq[letter] = 1
        else:
            lettersFreq[letter] = lettersFreq[letter] + 1

    for letter in str2:
        if letter not in lettersFreq:
            return False
        elif lettersFreq[letter] == 1:
            del lettersFreq[letter]
        else:
            lettersFreq[letter] = lettersFreq[letter] - 1

    return True



def main():
    str1 = "ab  d  "
    str2 = "d a  b "
    print("Are the strings", str1, "and", str2, "permutations of each other?")
    print("Result:", isStringPermutation(str1, str2))

main()