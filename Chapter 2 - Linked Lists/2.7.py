"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect.
Return the inter­ secting node. Note that the intersection is determined based on reference, not value.
hat is, if the kth node of the  rst linked list is the exact same node (by reference)
as the jth node of the second linked list, then they are intersecting.
"""

def findIntersectingNode(list1, list2):
    p1 = list1.head
    p2 = list2.head

    while p1 is not p2:
        p1 = list2.head if not p1 else p1.next
        p2 = list1.head if not p2 else p2.next

    return p1