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

    def get_len(self):
        return self.size

    def add(self, val):
        new = Node()
        new.data = val
        if self.size == 0:
            self.start = new
            self.size += 1
            return
        current = self.start
        while current.link is not None: # check for 2+ elements
            current = current.link
            current.link = new
        self.size+=1
        self.print()
        return

    def add_at(self, val, pos):
        new = Node()
        new.data = val
        if self.size == 0:
            self.start = new
            self.size += 1
            return
        if pos == 0:
            prev = self.start
            self.start = new
            new.next = prev
            return
        if pos > self.size:
            pos = self.size
        count = 0
        current = self.start
        while count < pos:
            prev = current
            current = current.link
            count += 1
        prev.link = new
        new.link = current
        self.size += 1
        self.print()
        return

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
        self.size-=1
        self.print()
        return

    def remove_at(self, pos):
        if self.size == 0:
            self.print()
            return
        if self.size == 1:
            self.start = None
            self.size -= 1
            self.print()
            return
        if pos > self.size:
            pos = self.size
        current = self.start
        count = 0
        while count < pos:
            prev = current
            current = current.link
            count += 1
        prev.link = current.link
        self.size -= 1
        self.print()
        return

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
        result += " len=" + str(self.size)
        print(result.strip())

    def reset(self):
        for x in range(self.size, 0, -1):
            self.remove_at(x)