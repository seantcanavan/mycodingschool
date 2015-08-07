__author__ = 'advoc'

import unittest
import DynamicListAsArray
import random

class MyTestCase(unittest.TestCase):
    def test_something(self):
        dynamic_list = DynamicListAsArray.DynamicListAsArray()
        print("insert at the end")
        dynamic_list.insert(4) #1
        dynamic_list.insert(6) #2
        dynamic_list.insert(2) #3
        dynamic_list.insert(3) #4
        dynamic_list.insert(1) #5
        dynamic_list.insert(6) #6
        dynamic_list.insert(5) #7
        dynamic_list.insert(8) #8
        dynamic_list.insert(5) #9
        dynamic_list.insert(9) #10
        self.assertEqual(dynamic_list.get_at(9), 9) # assert 10th item = 9
        print("remove from the end")
        dynamic_list.remove() #1
        dynamic_list.remove() #2
        dynamic_list.remove() #3
        dynamic_list.remove() #4
        dynamic_list.remove() #5
        dynamic_list.remove() #6
        dynamic_list.remove() #7
        dynamic_list.remove() #8
        dynamic_list.remove() #9
        dynamic_list.remove() #10
        self.assertEqual(dynamic_list.get_position(), -1) # the position is reset to starting
        dynamic_list.remove()
        self.assertEqual(dynamic_list.get_position(), -1) # the position hasn't moved since there's nothing to remove
        print("insert along the end")
        dynamic_list.insert_at(4, 0)  #1
        dynamic_list.insert_at(10, 1) #2
        dynamic_list.insert_at(2, 2)  #3
        dynamic_list.insert_at(3, 3)  #4
        dynamic_list.insert_at(1, 4)  #5
        dynamic_list.insert_at(6, 5)  #6
        dynamic_list.insert_at(5, 6)  #7
        dynamic_list.insert_at(8, 7)  #8
        dynamic_list.insert_at(5, 8)  #9
        dynamic_list.insert_at(9, 9)  #10
        self.assertEqual(dynamic_list.get_at(9), 9) # assert 10th item = 9
        print("removing from the start")
        dynamic_list.remove_at(0) #1
        dynamic_list.remove_at(0) #2
        dynamic_list.remove_at(0) #3
        dynamic_list.remove_at(0) #4
        dynamic_list.remove_at(0) #5
        dynamic_list.remove_at(0) #6
        dynamic_list.remove_at(0) #7
        dynamic_list.remove_at(0) #8
        dynamic_list.remove_at(0) #9
        self.assertEqual(dynamic_list.get_at(0), 9) # the last value is now the first
        dynamic_list.remove_at(0) #
        self.assertEqual(dynamic_list.get_position(), -1) # the position is reset
        dynamic_list.remove_at(0)
        self.assertEqual(dynamic_list.get_position(), -1) # the position hasn't moved since there's nothing to remove
        print("insert at the end")
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
        print("expand the list")
        dynamic_list.insert(11)
        self.assertEqual(dynamic_list.get_position(), 10)
        print("insert at the end")
        dynamic_list.insert(12)
        dynamic_list.insert(13)
        dynamic_list.insert(14)
        dynamic_list.insert(15)
        dynamic_list.insert(16)
        dynamic_list.insert(12)
        dynamic_list.insert(13)
        dynamic_list.insert(14)
        dynamic_list.insert(15)
        self.assertEqual(dynamic_list.get_size(), 20)
        self.assertEqual(dynamic_list.get_max_size(), 20)
        print("expand the list")
        dynamic_list.insert(21)
        self.assertEqual(dynamic_list.get_max_size(), 40)
        dynamic_list.insert_at(22, 30) # there is nothing defined at position 30 so insertion takes place at the end
        self.assertEqual(dynamic_list.get_at(21), 22)
        dynamic_list.remove_at(30)
        dynamic_list.remove_at(30)
        dynamic_list.remove_at(30)
        dynamic_list.remove_at(30)
        dynamic_list.remove_at(30)
        dynamic_list.remove_at(30)
        dynamic_list.remove_at(30)
        dynamic_list.remove_at(30)
        print("shrink the list")
        dynamic_list.remove_at(11)
        dynamic_list.reset()
        random.seed()
        return True

if __name__ == '__main__':
    unittest.main()
