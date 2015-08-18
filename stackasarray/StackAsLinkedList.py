__author__ = 'advoc'

import dynamiclistassinglylinkedlist.DynamicListAsSinglyLinkedList

class StackAsLinkedList:
    values = dynamiclistassinglylinkedlist.DynamicListAsSinglyLinkedList()
    size = 0

    def __init__(self):
        self.values = dynamiclistassinglylinkedlist.DynamicListAsSinglyLinkedList()
        self.size = 0

    def print_self(self):
        self.values.print_self()

    def push(self, val):
        self.values.add(val)

    def pop(self):
        self.values.remove()

    def top(self):
        return self.get_last_value()