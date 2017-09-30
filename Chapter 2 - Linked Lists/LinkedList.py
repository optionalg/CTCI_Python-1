class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def add(self, item):
		itemNode = Node(item)
		if not self.head:
			self.head = itemNode
		else:
			itemNode.next = self.head
			self.head = itemNode

	def insertToBack(self, item):
		itemNode = Node(item)
		if not self.head:
			self.head = itemNode
		else:
			curr = self.head
			while curr.next != None:
				curr = curr.next
			curr.next = itemNode

	def remove(self, item):
		if not self.head:
			return "List is empty"
		elif self.head.data == item:
			self.head = None
		else:
			curr = self.head
			while curr.next != None:
				if curr.next.data == item:
					curr.next = curr.next.next
				curr = curr.next
		
	def __str__(self):
		curr = self.head
		s = ""
		while curr.next != None:
			s = s + str(curr.data) + "->"
			curr = curr.next
		s += str(curr.data)
		return s


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
		