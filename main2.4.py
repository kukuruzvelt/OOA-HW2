import numbers


class BinarySearchTree:  # добавить проверки типов
    """ Class for working with a binary tree. """

    def __init__(self):
        """ Initializes variables. """
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def put(self, key, val):
        """ Puts element in binary tree. """
        if not isinstance(key, int):
            raise TypeError("key is not int")
        if not isinstance(val, numbers.Number):
            raise TypeError("val is not number")
        if self.root:
            self.__put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def __put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self.__put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self.__put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def get(self, key):
        """ Gets element from binary tree. """
        if self.root:
            res = self.__get(key, self.root)
            if res:
                return res.val
        return None

    def __get(self, key, currentNode):
        if not currentNode:
            raise ValueError("wrong key")
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self.__get(key, currentNode.leftChild)
        else:
            return self.__get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, k, v):
        self.put(k, v)


class TreeNode:
    """ Contains tree node. """
    def __init__(self, key, val, left=None, right=None,
                 parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        """ Determines if there is a left child. """
        return self.leftChild

    def hasRightChild(self):
        """ Determines if there is a right child. """
        return self.rightChild


try:
    bst = BinarySearchTree()
    bst[5] = 10
    bst[1] = 20
    bst[3] = 30
    bst[4] = 40

    code = int(input("Enter code: "))
    number = float(input("Enter num: "))
    print("total value = ", bst[code] * number)

except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
