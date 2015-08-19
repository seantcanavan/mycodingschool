__author__ = 'advoc'


class Node:
    data = None
    left = None
    right = None

    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def print(self):
        print(self.to_str())

    def to_str(self):
        result = "[ "
        if self.left is not None:
            result += "<- |"
        if self.data is not None:
            result += str(self.data)
        if self.right is not None:
            result += "| ->"
        result += " ]"


class BinaryTree:
    root = None

    def add(self, val):
        if self.root is None:
            new = Node(val)
            self.root = new
        else:
            current = self.root
            while current.data is not None:  # while we're inside a node with a value already, find a lower node
                if val > current.data:  # if new value is greater than current value, step right
                    if current.right is None:
                        current.right = Node(val)
                        return
                    else:
                        current = current.right
                elif val < current.data:  # if new value is less than current value, step left
                    if current.left is None:
                        current.left = Node(val)
                        return
                    else:
                        current = current.left

    def print(self):
        if self.root is None:
            return
        else:
            self.recursive_print(self.root)

    def recursive_print(self, tree):
        if tree.left is None and tree.right is None:
            tree.print()
        if tree.left is not None:
            self.recursive_print(tree.left)
        if tree.right is not None:
            self.recursive_print(tree.right)
