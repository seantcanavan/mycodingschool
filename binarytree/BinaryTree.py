__author__ = 'advoc'


class Node:
    value = None
    left = None
    right = None

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def print(self):
        print(self.to_str())

    def to_str(self):
        result = "[ "
        if self.left is not None:
            result += "<- |"
        if self.value is not None:
            result += str(self.value)
        if self.right is not None:
            result += "| ->"
        result += " ]"
        return result


class KeyNode:
    """Used to store comparable values in the BinaryTree which can then point to records or values
    This adds functionality so the BinaryTree search isn't merely a true / false result but can return complex values"""
    value = None
    key = None
    left = None
    right = None

    def __init__(self, key, val):
        self.key = key
        self.value = val

    def __init__(self, key, val, left, right):
        self.key = key
        self.value = val
        self.left = left
        self.right = right

    def print(self):
        print(self.to_str())

    def to_str(self):
        result = ""
        if self.left is not None:
            result += "<-"
        result += " | "
        if self.key is not None:
            result += "'" + str(self.key) + "'"
        result += " = "
        if self.value is not None:
            result += "'" + str(self.value) + "'"
        result += " | "
        if self.right is not None:
            result += "->"
        return result


class BinaryTree:
    root = None

    def add(self, val):
        if self.root is None:
            new = Node(val)
            self.root = new
        else:
            current = self.root
            while current.value is not None:  # while we're inside a node with a value already, find a lower node
                if val > current.value:  # if new value is greater than current value, step right
                    if current.right is None:
                        current.right = Node(val)
                        return
                    else:
                        current = current.right
                elif val < current.value:  # if new value is less than current value, step left
                    if current.left is None:
                        current.left = Node(val)
                        return
                    else:
                        current = current.left

    def search(self, val):
        """Return the value you're searching for in O(log(n))"""
        if self.root is None:
            return None
        else:
            return self.recursive_search(self.root, val)

    @staticmethod
    def recursive_search(root, val):
        """Search the current tree for the key
        Will return the key if it's found, None otherwise. Returned node may or may not contain a 'value' component"""
        current = root
        while current.left is not None or current.right is not None:  # until we hit a leaf node, traverse the tree
            if current.data == val:
                return current.data
            elif current.data > val:
                current = current.left
            else:
                current = current.right
        return None

    def print(self):
        if self.root is None:
            return
        else:
            self.recursive_print(self.root)

    def recursive_print(self, tree):
        if tree.left is not None:
            self.recursive_print(tree.left)
        if tree.right is not None:
            self.recursive_print(tree.right)
        tree.print()

    # def breadth_first_print(self, tree):
