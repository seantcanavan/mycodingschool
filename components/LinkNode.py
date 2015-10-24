class LinkNode:
    data = None
    link = None

    def __init__(self, val):
        self.data = val
        self.link = None

    def print(self):
        print(self.to_str())

    def to_str(self):
        if self.link is None:
            return "[" + str(self.data) + "]"
        else:
            return "[" + str(self.data) + ", " + "->" + "]"
