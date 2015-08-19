__author__ = 'advoc'

import unittest
import BinaryTree

class MyTestCase(unittest.TestCase):
    def test_something(self):
        btree = BinaryTree.BinaryTree()
        btree.add(1)
        btree.add(2)
        btree.add(3)
        btree.add(4)
        btree.add(5)
        btree.add(6)
        btree.add(7)
        btree.add(8)
        btree.add(9)

if __name__ == '__main__':
    unittest.main()
