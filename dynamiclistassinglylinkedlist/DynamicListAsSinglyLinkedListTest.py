__author__ = 'advoc'

import unittest
import DynamicListAsSinglyLinkedList
import time
import random

class MyTestCase(unittest.TestCase):
    def test_something(self):
        linked_list = DynamicListAsSinglyLinkedList.DynamicListAsSinglyLinkedList()
        # linked_list.add(5)
        # linked_list.add(10)
        # linked_list.add(20)
        # linked_list.add(30)
        # linked_list.remove()
        # linked_list.remove()
        # linked_list.remove()
        # linked_list.remove()
        # linked_list.add(1)
        # linked_list.add(2)
        # linked_list.add(3)
        # linked_list.add(4)
        # linked_list.add(5)
        # linked_list.add(6)
        # linked_list.add(7)
        # linked_list.add(8)
        # linked_list.add(9)
        # linked_list.add(10)
        # linked_list.remove_at(5)
        # linked_list.add_at(6, 5)
        # linked_list.remove_at(20)
        # linked_list.reset()
        # linked_list.add(10)
        # linked_list.add(9)
        # linked_list.add(8)
        # linked_list.add(7)
        # linked_list.add(6)
        # linked_list.add(5)
        # linked_list.add(4)
        # linked_list.add(3)
        # linked_list.add(2)
        # linked_list.add(1)
        # linked_list.reset()

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

        linked_list.add_at(1, 4)
        linked_list.add_at(2, 4)
        linked_list.add_at(3, 4)
        linked_list.add_at(4, 4)
        linked_list.add_at(5, 4)
        linked_list.add_at(6, 4)
        linked_list.add_at(7, 4)

        linked_list.remove_at(4)
        linked_list.remove_at(4)
        linked_list.remove_at(4)
        linked_list.remove_at(4)
        linked_list.remove_at(4)
        linked_list.remove_at(4)
        linked_list.remove_at(4)

if __name__ == '__main__':
    unittest.main()
