from LinkedList import LinkedList
from LinkedList import Node

l = LinkedList()
print("\n")

print("Initial list:")
l.insertToBack(2)
l.insertToBack(3)
l.insertToBack(3)
l.insertToBack(4)
l.insertToBack(3)
print(l)
l.removeDuplicates()
print("After removing duplicates:")
print(l)
print("\n")

print("Initial list:")
l.insertToBack(5)
print(l)
print("\n")
print("return kth from last element, k = 2")
print(l.returnKthToLast(2))
