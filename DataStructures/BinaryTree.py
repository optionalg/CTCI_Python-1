class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insertLeft(self, val):
        if not self.left:
            self.left = BinaryTree(val)
        else:
            tree = BinaryTree(val)
            tree.left = self.left
            self.left = tree

    def insertRight(self, val):
        if not self.right:
            self.right = BinaryTree(val)
        else:
            tree = BinaryTree(val)
            tree.right = self.right
            self.right = tree

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setRootVal(self, val):
        self.key = val

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key)
        if self.right:
            self.right.inorder()

b = BinaryTree(2)
b.insertLeft(3)
b.insertRight(5)
