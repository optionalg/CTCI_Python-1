"""
Delete Middle Node: Implement an algorithm to delete a node in the middle 
(i.e., any node but the  rst and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
"""

def deleteMiddleNode(self, node):
    if node is None or node.next is None:
        return None
    else:
        node.data = node.next.data
        node.next = node.next.next