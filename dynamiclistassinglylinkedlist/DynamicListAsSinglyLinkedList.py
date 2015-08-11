__author__ = 'advoc'

class Node:
    data = None
    link = None

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
        while current is not None and current.link is not None:
            current = current.link
        new = Node()
        new.data = val
        new.link = None
        if(current is None):

        current.link = new

    def print(self):
        current = self.start
        result = ""
        count = 0
        while current.link is not None:
            result += current.to_str()
            count += 1
            result += " "
            if count == 10:
                count = 0
                result += "\n"
            current = current.link



