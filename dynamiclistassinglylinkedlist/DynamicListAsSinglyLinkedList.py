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
        print(self.to_str())

    def to_str(self):
        if self.link is None:
            return "[" + str(self.data) + "]"
        else:
            return "[" + str(self.data) + ", " + "->" + "]"


class DynamicListAsSinglyLinkedList:
    start = None
    size = 0
    end = None

    def __init__(self):
        self.start = None
        self.size = 0

    def get_size(self):
        return self.size

    def get_start(self):
        return self.start

    def get_start_data(self):
        return self.start.data

    def get_end(self):
        return self.end

    def get_end_data(self):  # for stack implementation
        return self.end.data

    def add(self, val):
        """O(n) to traverse to the end of the linked list to insert"""
        new = Node(val)
        current = self.start
        while current is not None and current.link is not None:
            current = current.link
        if current is None:
            self.start = new
        else:
            current.link = new
        self.end = new
        self.size += 1

    def add_at(self, val, pos):
        """Add val at pos in the list. Pos is 0th based index. Worst case O(n) at the end of the list"""
        new = Node(val)
        if self.size == 0:  # adding to an empty list
            self.start = new
        elif pos == 0:  # adding to the beginning of the list
            prev = self.start
            self.start = new
            self.start.link = prev
        elif self.size == 1:
            self.start.link = new
        else:
            count = 0
            current = self.start
            while (count < self.size) and (count < pos):  # traverse the list to find the node where we want to add
                prev = current
                current = current.link
                count += 1
            temp = prev.link
            prev.link = new
            new.link = temp
        self.end = new
        self.size += 1

    def add_at_end(self, val):
        """O(1) as a direct link to end is always stored"""
        new = Node(val)
        if self.size == 0:
            self.start = new
            self.end = new
        else:
            self.end.link = new
            self.end = new
        self.size += 1

    def remove(self):
        """O(n) as the list must be traversed to the end to delete the second to last reference"""
        if self.size == 0:
            return
        if self.size == 1:
            self.start = None
            self.size -= 1
            return
        current = self.start
        while current.link is not None:
            prev = current
            current = current.link
        prev.link = None
        self.size -= 1
        return current.data

    def remove_at(self, pos):
        """Remove the value at pos in the list. Pos is 0th based index. Worst case O(n) at the end of the list"""
        if self.size == 0:
            return
        elif pos == 0:
            self.start = self.start.link
        elif self.size == 1:
            self.start = None
        else:
            current = self.start
            count = 1  # start at one since we're initializing at one
            while (count < self.size) and (count < pos):  # traverse the list to find the node where we want to remove
                prev = current
                current = current.link
                count += 1
            temp = current
            prev.link = current.link
            temp.link = None
        self.size -= 1

    def print_self(self):
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
        """O(n^2) since nested for loop as removing at the end is O(n)"""
        for x in range(self.size, 0, -1):  # deconstruct from end to start removing all link references
            self.remove_at(x)
