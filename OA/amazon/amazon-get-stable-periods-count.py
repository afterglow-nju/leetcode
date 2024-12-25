import unittest
from typing import List
from collections import defaultdict
class Solution:
    def getStablePeriodsCount(self,revenues, k):
        n = len(revenues)
        MOD = 10**9 + 7
        freq = defaultdict(int)  # Keep track of frequency of each value
        start = 0  # Window start
        total_periods = 0
        distinct_count = 0  # Number of distinct values in current window

        # For each possible ending point
        for end in range(n):
            # Add new value to frequency counter
            freq[revenues[end]] += 1
            if freq[revenues[end]] == 1:
                distinct_count += 1

            # Shrink window while we have too many distinct values
            while distinct_count > k:
                freq[revenues[start]] -= 1
                if freq[revenues[start]] == 0:
                    distinct_count -= 1
                start += 1

            # Add number of valid periods ending at current position
            # This is equal to the length of current valid window
            total_periods = (total_periods + (end - start + 1)) % MOD

        return total_periods

class TestGetStablePeriodsCount(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()  # Assume the `Solution` class has `getStablePeriodsCount` implemented.

    def test_example1(self):
        revenues = [1, 2, 1]
        k = 1
        expected = 3
        self.assertEqual(self.solution.getStablePeriodsCount(revenues, k), expected)

    def test_example2(self):
        revenues = [1]
        k = 1
        expected = 1
        self.assertEqual(self.solution.getStablePeriodsCount(revenues, k), expected)

    def test_example3(self):
        revenues = [1, 2, 3, 4]
        k = 1
        expected = 4
        self.assertEqual(self.solution.getStablePeriodsCount(revenues, k), expected)

    def test_example4(self):
        revenues = [3, 3, 3, 3]
        k = 1
        expected = 10
        self.assertEqual(self.solution.getStablePeriodsCount(revenues, k), expected)

    def test_example5(self):
        revenues = [1, 2, 1, 2, 1]
        k = 2
        expected = 15
        self.assertEqual(self.solution.getStablePeriodsCount(revenues, k), expected)

    def test_example6(self):
        revenues = [1, 2, 1, 3, 4]
        k = 2
        expected = 8
        self.assertEqual(self.solution.getStablePeriodsCount(revenues, k), expected)

    def test_example7(self):
        revenues = [1] * 1000
        k = 1
        expected = 500500 % (10**9 + 7)
        self.assertEqual(self.solution.getStablePeriodsCount(revenues, k), expected)

    def test_example8(self):
        revenues = [i for i in range(1, 101)]
        k = 100
        expected = 5050
        self.assertEqual(self.solution.getStablePeriodsCount(revenues, k), expected)

    def test_example9(self):
        revenues = [1, 2, 3, 2, 1, 3, 2, 1]
        k = 2
        expected = 18
        self.assertEqual(self.solution.getStablePeriodsCount(revenues, k), expected)

    def test_example10(self):
        revenues = [4, 4, 4, 4, 4]
        k = 1
        expected = 15
        self.assertEqual(self.solution.getStablePeriodsCount(revenues, k), expected)

    def test_example11(self):
        revenues = [5, 6, 7, 8, 9]
        k = 1
        expected = 5
        self.assertEqual(self.solution.getStablePeriodsCount(revenues, k), expected)

if __name__ == '__main__':
    unittest.main()