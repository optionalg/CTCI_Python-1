"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2blc5a3. 
If the "compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""
def stringCompression(word):
    if len(word) <= 2:
        return word
    count = 1
    newStr = ""
    for letter in range(1,len(word)):
        if word[letter] == word[letter - 1]:
            count += 1
        else:
            newStr = newStr + word[letter - 1] + str(count)
            count = 1
    
    newStr = newStr + word[-1]+str(count)
    return newStr if len(newStr) < len(word) else word

print(stringCompression("aabccacccaaa"))