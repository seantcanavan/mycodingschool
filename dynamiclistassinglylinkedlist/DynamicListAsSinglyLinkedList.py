__author__ = 'advoc'

class Node:
    data = None
    link = None

    def __init__(self):
        self.data = None
        self.link = None

    def print(self):
        if self.link is None:
            print("[" + str(self.data) + ", " + "0" + "]")
        else:
            print("[" + str(self.data) + ", " + "->" + "]")

    def to_str(self):
        if self.link is None:
            return "[" + str(self.data) + ", " + "0" + "]"
        else:
            return "[" + str(self.data) + ", " + "->" + "]"

class DynamicListAsSinglyLinkedList:
    start = None
    size = 0

    def add(self, val):
        current = self.start
        new = Node()
        new.data = val
        new.link = None
        if current is None:
            self.start = new
        else:
            while current.link is not None : # check for 2+ elements
                current = current.link
            current.link = new
        self.print()

    def print(self):
        current = self.start
        result = ""
        count = 0
        if current is not None:
            result += current.to_str()
            count += 1
            result += " "
        while current.link is not None:
            current = current.link
            result += current.to_str()
            count += 1
            result += " "
            if count == 10:
                count = 0
                result += "\n"
        print(result.strip())


