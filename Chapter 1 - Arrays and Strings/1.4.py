"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome.
A palindrome is a word or phrase that is the same  forwards and backwards.
A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.
 
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""

def palindromePermutation(str):
    newStr = "".join(str.split()).lower()
    letterFreq = {}
    lettersWithOddFreqCount = 0

    for char in newStr:
        if char not in letterFreq:
            letterFreq[char] = 1
            lettersWithOddFreqCount +=  1
        elif letterFreq[char] % 2 == 0:
            letterFreq[char] += 1
            lettersWithOddFreqCount += 1
        else:
            letterFreq[char] +=1
            lettersWithOddFreqCount -= 1

    if lettersWithOddFreqCount > 1:
        return False

    return True

print(palindromePermutation("Tact Coa"))