__author__ = 'seanthomascanavan'

class DynamicListAsArray:
    """A dynamic list ADT with array as the implementation"""
    STARTING_SIZE = 10
    GROWTH_FACTOR = 2
    content = []
    position = -1

    def __init__(self):
        self.content = [-1 for x in range(self.STARTING_SIZE)]
        self.print_contents()

    def print_contents(self):
        len_string = "{" + str(len(self.content)) + "}"
        content_string = ""
        for x in range(0, len(self.content)):
            if x-1 == self.position:
                content_string += "|"
            content_string += str(self.content[x]) + " "
        if (self.position + 1) == len(self.content):
            content_string += "|"
        print(content_string + len_string)

    def get_size(self):
        print("{" + str(len(self.content)) + "}")

    def get_position(self):
        return self.position

    def get(self, pos):
        return self.content[pos]

    def double_size(self):
        print("double_size")
        new_array = [-1 for x in range(len(self.content) * self.GROWTH_FACTOR)]
        for x in range(0, len(self.content)):
            new_array[x] = self.content[x]
        self.content = new_array

    def shrink_size(self):
        print("shrink_size")
        new_array = [len(self.content) / self.GROWTH_FACTOR]
        for x in range(0, len(new_array)):
            new_array[x] = self.content[x]
        self.content = new_array

    def guarantee_size(self):
        if self.position == len(self.content) -1:
            self.double_size()
            print("size multiplied by " + str(self.GROWTH_FACTOR))
        elif (len(self.content) / self.GROWTH_FACTOR) > self.position and (len(self.content) > 10):
            self.shrink_size()
            print("size divided by " + str(self.GROWTH_FACTOR))

    def insert(self, val):
        self.guarantee_size()
        self.position += 1
        self.content[self.position] = val
        self.print_contents()

    def insert_at(self, val, pos):
        self.guarantee_size()
        if pos > self.position + 1:
            pos = self.position + 1
        self.content[pos] = val
        self.position += 1
        self.print_contents()

    def remove(self):
        if self.position != -1:
            self.position -= 1
            self.print_contents()
        else:
            print("can't remove. nothing to remove")

    def remove_at(self, pos):
        if self.position == -1:
            print("can't remove. nothing to remove")
        else:
            for x in range(pos, len(self.content) -1):
                self.content[x] = self.content[x+1]
            self.position -= 1
            self.print_contents()