class Stack:
    def __init__(self):
        self.lst = []

    def push(self, item):
        self.lst.append(item)

    def peek(self):
        return self.lst[-1]

    def pop(self):
        return self.lst.pop(-1)

    def size(self):
        return len(self.lst)
