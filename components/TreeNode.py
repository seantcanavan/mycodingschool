class TreeNode:
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
        result = ["[ "]
        if self.left is not None:
            result.append("<- |")
        if self.value is not None:
            result.append(str(self.value))
        if self.right is not None:
            result.append("| ->")
        result.append(" ]")
        return "".join(result[x] for x in range(0, len(result)))
