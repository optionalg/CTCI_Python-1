"""
Return Kth to Last: Implement an algorithm to  nd the kth to last element of a singly linked list.
"""

def returnKthToLast(self, k):
    if not self.head or (not self.head.next and k > 1):
        return None
    elif not self.head.next and k==1:
        return self.head.data
    else:
        p1 = self.head
        p2 = self.head.next
        size = 1
        while p2 != None:
            p2 = p2.next
            size += 1
        count = 0
        if k > size:
            return None
        while count < (size - k):
            p1 = p1.next
            count += 1
        return p1.data