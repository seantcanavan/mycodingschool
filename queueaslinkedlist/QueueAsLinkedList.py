import dynamiclistassinglylinkedlist.DynamicListAsSinglyLinkedList as LinkedList


class QueueAsLinkedList:
    values = LinkedList.DynamicListAsSinglyLinkedList()
    size = 0

    def print_self(self):
        self.values.print_self()

    def enqueue(self, val):
        self.values.add_at_end(val)

    def dequeue(self):
        return self.values.remove_at_start()

    def peek(self):
        return self.values.get_start()
