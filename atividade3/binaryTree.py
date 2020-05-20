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

    def _setRoot(self, element):
        if self.root.element is None:
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
        if (node.lChild is not None) or (node.rChild is not None):
            return True
        else:
            return False

    def isExternal(self, node):
        if (node.lChild is None) and (node.rChild is None):
            return True
        else:
            return False

    def isRoot(self, node):
        if node.parent is None:
            return True
        else:
            return False
        
    def hasLeft(self, node):
        if node.lChild is not None:
            return True
        else:
            return False

    def hasRight(self, node):
        if node.rChild is not None:
            return True
        else:
            return False

    def left(self, node):
        if hasLeft(node) is True:
            return node.lChild
        else:
            return None

    def right(self, node):
        if hasRight(node) is True:
            return node.rChild
        else:
            return None

    def parent(self, node):
        if node.parent is not None:
            return node.parent
        else:
            return None

    def children(self, node):
        children = []
        if hasRight(node) is True:
            children.append(node.rChild)
        if hasLeft(node) is True:
            children.append(node.lChild)
        return children

    def addRoot(self, element):
        self._setRoot(element)
        self.size = 1
        

    def insertLeft(self, node, element):
        node.lChild = Position(element, node)
        self.size += 1

    def insertRight(self, node, element):
        node.rChild = Position(element, node)
        self.size += 1

    # # (consigo fazer recursssivamente se for só printando. )
    # def _toStringPreOrder(self, root):
    #     # result = []
    #     result = ""
    #     if root is not None:
    #         # result.append()
    #         result += " ".join(str(root.element))
    #         self._toStringPreOrder(root.lChild)
    #         self._toStringPreOrder(root.rChild)
    #     return result
    #     # " ".join(map(str, result))

    # def toStringPreOrder(self):
    #     return self._toStringPreOrder(self.root)


    def toStringPreOrder(self):
        node_stack = []
        result = []
        node = self.root

        while True:
            if node is not None:
                node_stack.append(node)
                result.append(node.element)
                node = node.lChild
            elif len(node_stack) > 0:
                node = node_stack.pop()
                node = node.rChild
            else:
                break

        return " ".join(map(str, result))

    def toStringPosOrder(self):
        node_stack = []
        result = []
        node = self.root

        while True:
            while node is not None:
                if node.rChild is not None:
                    node_stack.append(node.rChild)
                node_stack.append(node)
                node = node.lChild

            node = node_stack.pop()
            
            if (node.rChild is not None and len(node_stack) > 0 and node_stack[-1] is node.rChild):
                node_stack.pop()
                node_stack.append(node)
                node = node.rChild
            else:
                result.append(node.element)
                node = None

            if len(node_stack) == 0:
                break
            
        return " ".join(map(str, result))

    
    def detph(self, node):
        detph = -1 
        if node is not None:
            while node is not None:
                detph += 1
                node = node.parent
        
        return detph
    

    
if __name__ == "__main__":
    
    tree = LinkedBinaryTree()
    tree.addRoot(1)
    tree.insertLeft(tree.root, 2)
    tree.insertRight(tree.root, 3)
    tree.insertLeft(tree.root.lChild, 4)
    tree.insertLeft(tree.root.lChild.lChild, 5)
    tree.insertRight(tree.root.lChild, 6)
    tree.insertLeft(tree.root.lChild.rChild, 7)
    tree.insertRight(tree.root.lChild.rChild,8)

    print("PreOrdem: {}".format(tree.toStringPreOrder()))
    print("PosOrdem: {}".format(tree.toStringPosOrder()))
    print("Profundidade: {}".format(tree.detph(tree.root.lChild.rChild.rChild)))
   
 