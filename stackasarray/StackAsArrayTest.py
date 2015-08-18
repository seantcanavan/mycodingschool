__author__ = 'advoc'

import unittest
import StackAsArray
import random
import time

class MyTestCase(unittest.TestCase):
    def test_something(self):
        stack = StackAsArray.StackAsArray()

        for x in range(0, 100):
            val = random.randint(1,100)
            if x > 50:
                print("popped off: " + str(stack.pop()))
            else:
                stack.push(val)
                print("pushed: " + str(val))
            stack.print_self()
            time.sleep(1)

if __name__ == '__main__':
    unittest.main()
