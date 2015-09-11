__author__ = 'seancanavan'


class BinarySearch:

    @staticmethod
    def binary_array_search(search, val):
        current = search
        while len(current) > 0:
            next_index = len(current) // 2
            next_value = current[next_index]
            if next_value == val:
                return True
            if len(current) == 1 and current[0] != val:
                return False
            new_current = []
            if next_value > val:
                for x in range(0, next_index):
                    new_current.append(current[x])
            elif next_value < val:
                for x in range(next_index, len(current)):
                    new_current.append(current[x])
            current = new_current
        return False

    @staticmethod
    def binary_tree_key_search(tree, key):
        """BST search of a tree consisting of key nodes
        Could be used to search a set of human records by name and then return their entire 'record'"""
        current = tree.node
        while current is not None:
            if current.key == key:  # if we found the key we're looking for
                return current.value  # return the value
            elif current.key > key:
                current = current.left
            else:
                current = current.right
        return None

    @staticmethod
    def binary_tree_search(tree, val):
        """BST search of a tree consisting of tree nodes
        Could be used to tell whether a value exists or not in a set of values"""
        current = tree.node
        while current is not None:
            if current.value == val:
                return True
            elif current.value > val:
                current = current.left
            else:
                current = current.right
        return None
