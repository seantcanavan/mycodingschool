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
        # print("pre order")
        # btree.print_depth_first_pre_order()
        # print("in order")
        # btree.print_depth_first_in_order()
        # print("post order")
        # btree.print_depth_first_post_order()
        # print("breadth first")
        # btree.print_breadth_first()
        btree.print_breadth_first()
        btree.delete_value(btree.root, 25)
        btree.print_breadth_first()

if __name__ == '__main__':
    unittest.main()
