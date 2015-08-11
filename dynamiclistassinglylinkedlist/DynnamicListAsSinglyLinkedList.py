__author__ = 'advoc'

import unittest
import DynamicListAsSinglyLinkedList

class MyTestCase(unittest.TestCase):
    def test_something(self):
        list = DynamicListAsSinglyLinkedList.DynamicListAsSinglyLinkedList()
        list.add(5)
        list.print()


if __name__ == '__main__':
    unittest.main()
