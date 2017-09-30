from LinkedList import LinkedList


l = LinkedList()
print("\n")

print("Initial list:")
l.insertToBack(2)
l.insertToBack(3)
l.insertToBack(3)
l.insertToBack(4)
l.insertToBack(3)
print(l)
print("\n")
l.removeDuplicates()
print("After removing duplicates:")
print(l)

print("\n")
print(l)

print("return kth from last element, k = 3")

print(l.returnKthToLast(4))
