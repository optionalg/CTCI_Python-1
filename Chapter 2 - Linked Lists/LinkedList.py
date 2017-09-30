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