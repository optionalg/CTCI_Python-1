from DataStructures import Stack
from DataStructures import BinaryTree


def buildParseTree(expression):
    expressionList = expression.split()
    s = Stack.Stack()
    rootTree = BinaryTree.BinaryTree('')
    s.push(rootTree)
    currentTree = rootTree

    for symbol in expressionList:
        if symbol == '(':
            currentTree.insertLeft('')
            s.push(currentTree)
            currentTree = currentTree.getLeft()
        elif symbol not in ['*', '-', '+', '/', ')']:
            currentTree.setRootVal(int(symbol))
            parent = s.pop()
            currentTree = parent
        elif symbol in ['*', '-', '+', '/']:
            currentTree.setRootVal(symbol)
            currentTree.insertRight('')
            s.push(currentTree)
            currentTree = currentTree.getRight()
        elif symbol == ')':
            currentTree = s.pop()
        else:
            raise ValueError

    return rootTree

pt = buildParseTree("( ( 10 * 3 ) * ( 30 + 5 ) )")
pt.inorder()
