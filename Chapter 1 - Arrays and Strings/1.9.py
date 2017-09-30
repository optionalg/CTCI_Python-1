"""
String Rotation:
Assume you have a method isSubstring which checks if one word is a substring of another.
 Given two strings, sl and s2, write code to check if s2 is a rotation of sl 
 using only one call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").
"""

def isRotatedString(s1, s2):
    if not s1 or not s2:
        return False
    if len(s1) != len(s2):
        return False

    return isSubstring(s1 + s1, s2)

def isSubstring(s1, s2):
    return s2 in s1

print(isRotatedString("waterbottle", "erbottlewat"))