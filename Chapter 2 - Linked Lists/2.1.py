"""
Remove Duplicates! Write code to remove duplicates from an unsorted linked list.
"""

def removeDuplicates(self):
    curr = self.head
    while curr != None:
        temp = curr
        succ = curr.next
        while succ != None:
            if curr.data == succ.data:
                succ = succ.next
                temp.next = succ
            else:
                temp = succ
                succ = succ.next
        curr = curr.next