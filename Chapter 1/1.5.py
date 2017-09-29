"""
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
Given two strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE
pale,  ple   -> true 
pales, pale -> true 
pale,  bale  -> true 
pale,  bake  -> false
"""

def oneAway(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False
    else:
        differences = 0
        firstStringFreq = {}
        for letter in str1:
            if letter not in firstStringFreq:
                firstStringFreq[letter] = 1
            else:
                firstStringFreq[letter] += 1
        for letter in str2:
            if letter not in firstStringFreq:
                differences += 1
            else:
                if firstStringFreq[letter] > 0:
                    firstStringFreq[letter] -= 1
                else:
                    differences += 1
    
    return differences <= 1

print(oneAway("pale", "pa le"))