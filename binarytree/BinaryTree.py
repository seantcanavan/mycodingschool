__author__ = 'advoc'

import components.TreeNode as Node


class BinaryTree:
    root = None

    def add(self, val):
        if self.root is None:
            new = Node.TreeNode(val)
            self.root = new
        else:
            current = self.root
            while current.value is not None:  # while we're inside a node with a value already, find a lower node
                if val > current.value:  # if new value is greater than current value, step right
                    if current.right is None:
                        current.right = Node.TreeNode(val)
                        return
                    else:
                        current = current.right
                elif val < current.value:  # if new value is less than current value, step left
                    if current.left is None:
                        current.left = Node.TreeNode(val)
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
