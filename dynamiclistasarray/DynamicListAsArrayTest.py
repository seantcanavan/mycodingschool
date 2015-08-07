__author__ = 'advoc'

import unittest
import DynamicListAsArray

class MyTestCase(unittest.TestCase):
    def test_something(self):
        dynamic_list = DynamicListAsArray.DynamicListAsArray()
        dynamic_list.insert(4)
        dynamic_list.insert(10)
        dynamic_list.insert(2)
        dynamic_list.insert(3)
        dynamic_list.insert(1)
        dynamic_list.insert(6)
        dynamic_list.insert(5)
        dynamic_list.insert(8)
        dynamic_list.insert(5)
        dynamic_list.insert(9)
        self.assertEqual(dynamic_list.get(9), 9) # assert 10th item = 9
        dynamic_list.remove()
        dynamic_list.remove()
        dynamic_list.remove()
        dynamic_list.remove()
        dynamic_list.remove()
        dynamic_list.remove()
        dynamic_list.remove()
        dynamic_list.remove()
        dynamic_list.remove()
        dynamic_list.remove()
        self.assertEqual(dynamic_list.get_position(), -1) # the position is reset to starting
        dynamic_list.remove()
        self.assertEqual(dynamic_list.get_position(), -1) # the position hasn't moved since there's nothing to remove
        dynamic_list.insert_at(4, 0)
        dynamic_list.insert_at(10, 1)
        dynamic_list.insert_at(2, 2)
        dynamic_list.insert_at(3, 3)
        dynamic_list.insert_at(1, 4)
        dynamic_list.insert_at(6, 5)
        dynamic_list.insert_at(5, 6)
        dynamic_list.insert_at(8, 7)
        dynamic_list.insert_at(5, 8)
        dynamic_list.insert_at(9, 9)
        self.assertEqual(dynamic_list.get(9), 9) # assert 10th item = 9
        dynamic_list.remove_at(0)
        dynamic_list.remove_at(0)
        dynamic_list.remove_at(0)
        dynamic_list.remove_at(0)
        dynamic_list.remove_at(0)
        dynamic_list.remove_at(0)
        dynamic_list.remove_at(0)
        dynamic_list.remove_at(0)
        dynamic_list.remove_at(0)
        dynamic_list.remove_at(0)
        self.assertEqual(dynamic_list.get(0), 9) # the last value is now the first
        self.assertEqual(dynamic_list.get_position(), -1) # the position is reset
        dynamic_list.remove_at(0)
        self.assertEqual(dynamic_list.get_position(), -1) # the position hasn't moved since there's nothing to remove
        dynamic_list.insert(4)
        dynamic_list.insert(10)
        dynamic_list.insert(2)
        dynamic_list.insert(3)
        dynamic_list.insert(1)
        dynamic_list.insert(6)
        dynamic_list.insert(5)
        dynamic_list.insert(8)
        dynamic_list.insert(5)
        dynamic_list.insert(9)
        print(dynamic_list.get_position())
        dynamic_list.insert(11)
        self.assertEqual(dynamic_list.get_position(), 10)
        return True


if __name__ == '__main__':
    unittest.main()
