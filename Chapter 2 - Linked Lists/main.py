from LinkedList import LinkedList
from LinkedList import Node


def sumListsForward(first, second):
    curr1 = first.getHead()
    curr2 = second.getHead()
    sumList = []
    sumLinkedList = LinkedList()
    carry = 0
    while curr1 is not None and curr2 is not None:
        sum = curr1.data + curr2.data + carry
        if sum > 9:
            sumList.append(sum - 10)
            carry = 1
        else:
            sumList.append(sum)
            carry = 0
        curr1 = curr1.next
        curr2 = curr2.next
    if carry == 1:
        sumList.append(1)

    for i in sumList:
        sumLinkedList.add(i)

    return sumLinkedList

first = LinkedList()
first.add(6)
first.add(1)
first.add(7)

second = LinkedList()
second.add(2)
second.add(9)
second.add(5)

print(first)
print(second)
print(sumListsForward(first, second))
