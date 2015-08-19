__author__ = 'advoc'

import DynamicListAsSinglyLinkedList


class StackAsLinkedList:
    values = DynamicListAsSinglyLinkedList.DynamicListAsSinglyLinkedList()
    size = 0

    def __init__(self):
        self.values = DynamicListAsSinglyLinkedList.DynamicListAsSinglyLinkedList()
        self.size = 0

    def print_self(self):
        self.values.print_self()

    def push(self, val):
        self.values.add(val)

    def pop(self):
        return self.values.remove()

    def top(self):
        return self.get_last_value()
