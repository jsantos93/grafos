class Position:

    def __init__(self, element, parent = None, lChild = None, rChild = None):
        self.element = element
        self.parent = parent 
        self.lChild = lChild
        self.rChild = rChild


class LinkedBinaryTree:

    def __init__(self):
        self.root = Position(None)
        self.size = 0

    def getRoot(self):
        return self.root

    def __setRoot(self, element):
        if self.root.element == None:
            self.root.element = element

    def getSize(self):
        return self.size

    def setSize(self, size):
        this.size = size

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def isInternal(self, node):
        if (node.lChild != None) or (node.rChild != None):
            return True
        else:
            return False

    def isExternal(self, node):
        if (node.lChild == None) and (node.rChild == None):
            return True
        else:
            return False

    def isRoot(self, node):
        if node.parent == None:
            return True
        else:
            return False
        
    def hasLeft(self, node):
        if node.lChild != None:
            return True
        else:
            return False

    def hasRight(self, node):
        if node.rChild != None:
            return True
        else:
            return False

    def left(self, node):
        if hasLeft(node) == True:
            return node.lChild
        else:
            return None

    def right(self, node):
        if hasRight(node) == True:
            return node.rChild
        else:
            return None

    def parent(self, node):
        if node.parent != None:
            return node.parent
        else:
            return None

    def children(self, node):
        children = []
        if hasRight(node) == True:
            children.append(node.rChild)
        if hasLeft(node) == True:
            children.append(node.lChild)
        return children

    def addRoot(self, element):
        self.__setRoot(element)
        self.size = 1
        

    def insertLeft(self, node, element):
        node.lChild = Position(element, node)

    def insertRight(self, node, element):
        node.rChild = Position(element, node)

    def toStringPreOrder(self, node):
        if node != None:
            print(node.element)
            self.toStringPreOrder(node.lChild)
            self.toStringPreOrder(node.rChild)


    # def toStringPreOrder(self):
    #     if self.root != None:
    #         print(self.root.element)
    #         self.toStringPreOrder(self.root.lChild)
    #         self.toStringPreOrder(self.root.rChild)

    def toStringPosOrder(self):
        pass
    

    
if __name__ == "__main__":
    
    binaryTree = LinkedBinaryTree()
    binaryTree.addRoot(1)
    binaryTree.insertLeft(binaryTree.root, 2)
    binaryTree.insertRight(binaryTree.root, 3)
    binaryTree.insertLeft(binaryTree.root.lChild, 4)

    binaryTree.toStringPreOrder(binaryTree.root)