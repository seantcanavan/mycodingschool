__author__ = 'seanthomascanavan'


class DynamicListAsArray:
    """A dynamic list ADT with array as the implementation"""
    STARTING_SIZE = 10
    GROWTH_FACTOR = 2
    SHRINK_FACTOR = 3
    content = []
    position = -1

    def __init__(self):
        self.content = [-1 for x in range(self.STARTING_SIZE)]
        print("initialized")

    def get(self):
        """O(1)"""
        return self.content[self.position + 1]

    def get_at(self, pos):
        """O(1)"""
        if pos > self.position + 1:
            pos = self.position + 1
        return self.content[pos]

    def add(self, val):
        """O(N) worst case on resize"""
        self.grow()
        self.position += 1
        self.content[self.position] = val

    def add_at(self, val, pos):
        """O(N) worst case on resize"""
        self.grow()
        if pos > self.position + 1:
            pos = self.position + 1
        self.content[pos] = val
        self.position += 1

    def remove(self):
        """O(N) worst case on resize"""
        if self.position != -1:
            self.position -= 1
            self.shrink()
        else:
            print("can't remove. nothing to remove")

    def remove_at(self, pos):
        """O(N) worst case on resize"""
        if self.position == -1:
            print("can't remove. nothing to remove")
        else:
            self.shrink()
            if pos > self.position + 1:
                pos = self.position + 1
            for x in range(pos, len(self.content) -1):
                self.content[x] = self.content[x+1]
            self.position -= 1

    def reset(self):
        """O(N) to rebuild the array"""
        self.content = [-1 for x in range(0, 10)]
        self.position = -1
        print("reset")

    def print_self(self):
        len_string = "{" + str(len(self.content)) + "}"
        content_string = ""
        for x in range(0, len(self.content)):
            if x-1 == self.position:
                content_string += "|"
            content_string += str(self.content[x]) + " "
        if (self.position + 1) == len(self.content):
            content_string += "|"
        print(content_string + len_string)

    def grow(self):
      if self.position == len(self.content) -1:
            new_array = [-1 for x in range(len(self.content) * self.GROWTH_FACTOR)]
            for x in range(0, len(self.content)):
                new_array[x] = self.content[x]
            self.content = new_array

    def shrink(self):
        if (len(self.content) / self.SHRINK_FACTOR) > self.position and (len(self.content) > self.STARTING_SIZE):
            new_array = [-1 for x in range((int(len(self.content) / self.GROWTH_FACTOR)))]
            for x in range(0, len(new_array)):
                new_array[x] = self.content[x]
            self.content = new_array

    def get_size(self):
        return self.position + 1

    def get_max_size(self):
        return len(self.content)

    def get_position(self):
        return self.position
