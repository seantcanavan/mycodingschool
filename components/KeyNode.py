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
        result = []
        if self.left is not None:
            result.append("<-")
        result.append(" | ")
        if self.key is not None:
            result.append("'")
            result.append(str(self.key))
            result.append("'")
        result.append(" = ")
        if self.value is not None:
            result.append("'")
            result.append(str(self.value))
            result.append("'")
        result.append(" | ")
        if self.right is not None:
            result.append("->")
        return "".join(result[x] for x in range(0, len(result)))
