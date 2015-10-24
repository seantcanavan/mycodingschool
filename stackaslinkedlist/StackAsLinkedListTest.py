import unittest
import stackaslinkedlist.StackAsLinkedList as Stack
import time
import random


class MyTestCase(unittest.TestCase):
    def test_something(self):
        stack = Stack.StackAsLinkedList()
        for x in range(0, 100):
            val = random.randint(1, 100)
            if x > 10:
                print("popped off: " + str(stack.pop()))
            else:
                stack.push(val)
                print("pushed: " + str(val))
            stack.print_self()
            time.sleep(1)


if __name__ == '__main__':
    unittest.main()
