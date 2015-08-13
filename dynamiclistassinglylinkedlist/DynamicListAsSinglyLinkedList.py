__author__ = 'advoc'

class Node:
    data = None
    link = None

    def __init__(self):
        self.data = None
        self.link = None

    def __init__(self, val):
        self.data = val
        self.link = None

    def print(self):
        if self.link is None:
            print("[" + str(self.data) + "]")
        else:
            print("[" + str(self.data) + ", " + "->" + "]")

    def to_str(self):
        if self.link is None:
            return "[" + str(self.data) + "]"
        else:
            return "[" + str(self.data) + ", " + "->" + "]"

class DynamicListAsSinglyLinkedList:
    start = None
    size = 0

    def get_len(self):
        return self.size

    def add(self, val):
        new = Node(val)
        current = self.start
        while current is not None and current.link is not None:
            current = current.link
        if current is None:
            self.start = new
        else:
            current.link = new
        self.size += 1
        self.print()

    def add_node(self, node1, node2, new_node):
        if node2 is None: # adding at the end, just append like add(self)
            node1.link = new_node
        else: # adding in the middle, we need to stitch them together
            node1.link = new_node
            new_node.link = node2

    def remove_node(self, node1, node2, node3):
        if node3 is None: # removing at the end, just cut off node2
            node1.link = None
        else: # else we need to stitch the links together around node2 to cut it out
            node1.link = node3
            node2.link = None # # isolate the node for garbage collection

    def remove(self):
        if self.size == 0:
            self.print()
            return
        if self.size == 1:
            self.start = None
            self.size -= 1
            self.print()
            return
        current = self.start
        while current.link is not None:
            prev = current
            current = current.link
        prev.link = None
        self.size -= 1
        self.print()

    def print(self):
        current = self.start
        result = ""
        if current is not None:
            result += current.to_str()
            result += " "
        while current is not None and current.link is not None:
            current = current.link
            result += current.to_str()
            result += " "
        result += " size=" + str(self.size)
        print(result.strip())

    def reset(self):
        for x in range(self.size, 0, -1):
            self.remove_at(x)