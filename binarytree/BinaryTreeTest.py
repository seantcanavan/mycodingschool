__author__ = 'advoc'

import unittest
import BinaryTree


class MyTestCase(unittest.TestCase):
    def test_something(self):
        btree = BinaryTree.BinaryTree()
        btree.add(50)
        btree.add(25)
        btree.add(75)
        btree.add(12)
        btree.add(37)
        btree.add(62)
        btree.add(87)
        btree.add(6)
        btree.add(18)
        btree.add(31)
        btree.add(43)
        btree.add(56)
        btree.add(68)
        btree.add(81)
        btree.add(93)
        btree.print()


if __name__ == '__main__':
    unittest.main()
