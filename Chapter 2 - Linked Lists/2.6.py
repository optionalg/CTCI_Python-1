"""
Palindrome: Implement a function to check if a linked list is a palindrome.

"""

def isLinkedListPalindrome(self):
    dataList = []
    if not self.head or not self.head.next:
        return True
    curr = self.head
    while curr is not None:
        dataList.append(curr.data)
        curr = curr.next
    return dataList == dataList[::-1]