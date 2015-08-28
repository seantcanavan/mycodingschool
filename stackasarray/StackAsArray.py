__author__ = 'advoc'

import dynamiclistasarray.DynamicListAsArray as Array


class StackAsArray:
    array = Array.DynamicListAsArray()

    def push(self, val):
        self.array.add(val)

    def pop(self):
        return self.array.remove()

    def top(self):
        return self.get_at_end()

    def is_empty(self):
        return self.array.is_empty()

    def get_max_size(self):
        return self.array.get_max_size()

    def get_size(self):
        return self.array.get_size()

    def print_self(self):
        self.array.print_self()
