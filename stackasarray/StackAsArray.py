__author__ = 'advoc'


class StackAsArray:
    size = 0
    values = []
    STARTING_SIZE = 10
    SHRINK_FACTOR = 3
    GROWTH_FACTOR = 2

    def __init__(self):
        self.size = 0
        self.values = [-1 for x in range(0, self.STARTING_SIZE)]

    def push(self, val):
        self.grow()
        self.values[self.size] = val
        self.size += 1

    def pop(self):
        if  self.size > 0:
            self.shrink()
            val = self.values[self.size - 1]
            self.size -= 1
            return val
        else:
            return None

    def top(self):
        if self.size > 0:
            return self.values[self.size -1]
        else:
            return "n/a"

    def is_empty(self):
        return self.size == 0

    def grow(self):
      if self.size == len(self.values) -1:
            new_array = [-1 for x in range(len(self.values) * self.GROWTH_FACTOR)]
            for x in range(0, len(self.values)):
                new_array[x] = self.values[x]
            self.values = new_array

    def get_actual_size(self):
        return len(self.values)

    def get_size(self):
        return self.size

    def shrink(self):
        if (len(self.values) / self.SHRINK_FACTOR) > self.size and (len(self.values) > self.STARTING_SIZE):
            new_array = [-1 for x in range((int(len(self.values) / self.GROWTH_FACTOR)))]
            for x in range(0, len(new_array)):
                new_array[x] = self.values[x]
            self.values = new_array

    def print_self(self):
        len_string = "{" + str(len(self.values)) + "}"
        content_string = ""
        for x in range(0, len(self.values)):
            if x == self.size:
                content_string += "|"
            content_string += str(self.values[x]) + " "
        if (self.size + 1) == len(self.values):
            content_string += "|"
        print(content_string + len_string)