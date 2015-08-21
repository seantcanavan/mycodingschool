__author__ = 'advoc'

import unittest
import DynamicListAsSinglyLinkedList
import time
import random


class MyTestCase(unittest.TestCase):
    def test_something(self):
        linked_list = DynamicListAsSinglyLinkedList.DynamicListAsSinglyLinkedList()

        linked_list.add_at_end(1)
        linked_list.add_at_end(2)
        linked_list.add_at_end(3)
        linked_list.add_at_end(4)
        linked_list.add_at_end(5)
        linked_list.add_at_end(6)
        linked_list.add_at_end(7)
        linked_list.add_at_end(8)
        self.assertEquals(8, linked_list.get_end_data())
        self.assertEquals(8, linked_list.get_size())
        self.assertEquals(1, linked_list.get_start_data())

        linked_list.add_at(9, 9)
        self.assertEquals(9, linked_list.get_end_data())


        # random.seed()
        # for x in range(0, 100):
        #     action = random.randint(1, 4)
        #     val = random.randint(1,100)
        #     if action == 1 or action == 2:
        #         print("removing")
        #         linked_list.remove()
        #     else:
        #         print("adding " + str(val))
        #         linked_list.add(val)
        #     time.sleep(1)


        # random.seed()
        # for x in range(0, 100):
        #     pos = random.randint(0,9)
        #     action = random.randint(1, 4)
        #     val = random.randint(1,100)
        #     if action == 1 or action == 2:
        #         print("removing at: " + str(pos))
        #         linked_list.remove_at(pos)
        #     else:
        #         print("adding " + str(val) + " at: " + str(pos))
        #         linked_list.add_at(val, pos)
        #     time.sleep(1)

        #[70, ->] [29, ->] [53, ->] [64, ->] [54]  len=5
        #removing at: 2
        #
        # linked_list.add(70)
        # linked_list.add(29)
        # linked_list.add(53)
        # linked_list.add(64)
        # linked_list.add(54)
        # linked_list.remove_at(2)

if __name__ == '__main__':
    unittest.main()
