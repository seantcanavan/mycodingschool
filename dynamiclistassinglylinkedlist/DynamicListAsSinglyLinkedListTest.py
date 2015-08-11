__author__ = 'advoc'

import unittest
import DynamicListAsSinglyLinkedList

class MyTestCase(unittest.TestCase):
    def test_something(self):
        linked_list = DynamicListAsSinglyLinkedList.DynamicListAsSinglyLinkedList()
        linked_list.add(5)
        linked_list.add(10)
        linked_list.add(20)
        linked_list.add(30)

if __name__ == '__main__':
    unittest.main()
