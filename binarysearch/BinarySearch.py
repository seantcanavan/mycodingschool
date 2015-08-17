__author__ = 'seancanavan'


class BinarySearch:

    def binary_search(self, search, val):
        current = search
        while len(current) > 0:
            next_index = len(current) // 2
            next_value = current[next_index]
            if next_value == val:
                return True
            if len(current) == 1 and current[0] != val:
                return False
            new_current = []
            if next_value > val:
                for x in range(0, next_index):
                    new_current.append(current[x])
            elif next_value < val:
                for x in range(next_index, len(current)):
                    new_current.append(current[x])
            current = new_current
        return False
