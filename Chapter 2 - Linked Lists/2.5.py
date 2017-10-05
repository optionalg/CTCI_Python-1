import LinkedList

"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1 's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input:(7-> 1 -> 6) + (5 -> 9 -> 2).Thatis,617 + 295. Output:2 -> 1 -> 9.That is,912.


FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295. Output:9 -> 1 -> 2.That is,912.

"""

# In reverse order
def sumListsReverse(first, second):
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

    for i in sumList[::-1]:
        sumLinkedList.add(i)

    return sumLinkedList

# In forward order (FOLLOW UP)
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