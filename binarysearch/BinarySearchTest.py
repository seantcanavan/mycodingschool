__author__ = 'seancanavan'

import unittest
import BinarySearch


class MyTestCase(unittest.TestCase):
    def test_something(self):
        values = []
        for x in range(0, 100):
            values.append(x)
        # pprint.pprint(values)
        bsearch = BinarySearch.BinarySearch()
        print(bsearch.binary_array_search(values, 56))

if __name__ == '__main__':
    unittest.main()
