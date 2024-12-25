import unittest
from typing import List

class Solution:
    def getPairsCount(self, process: List[int], k: int) -> int:
        process.sort()
        left, right = 0, 0
        ret = 0
        while right < len(process) :
            if process[right] - process[left] <= k:
                right += 1
            else:
                while process[right] - process[left] > k:
                    ret += right - 1 - left
                    left += 1
        #print(right, left,'-------------')
        #if right == len(process):
        right-=1
        while left<right:
            print(ret, right, left)
            ret += right  - left
            left += 1
        return ret

class TestGetPairsCount(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        process = [100, 200, 300, 400]
        k = 250
        expected = 5
        self.assertEqual(self.solution.getPairsCount(process, k), expected)

    def test_example2(self):
        process = [10, 12, 11]
        k = 0
        expected = 0
        self.assertEqual(self.solution.getPairsCount(process, k), expected)

    def test_empty_list(self):
        process = [7,10,13,11]
        k = 3
        expected = 4
        self.assertEqual(self.solution.getPairsCount(process, k), expected)
        
    def test_empty_list(self):
        process = []
        k = 10
        expected = 0
        self.assertEqual(self.solution.getPairsCount(process, k), expected)

    def test_single_element(self):
        process = [100]
        k = 50
        expected = 0
        self.assertEqual(self.solution.getPairsCount(process, k), expected)

    def test_large_k(self):
        process = [1, 2, 3, 4, 5]
        k = 100
        expected = 10  # All pairs are valid
        self.assertEqual(self.solution.getPairsCount(process, k), expected)

    def test_no_valid_pairs(self):
        process = [1, 10, 20]
        k = 5
        expected = 0
        self.assertEqual(self.solution.getPairsCount(process, k), expected)

    def test_multiple_identical_elements(self):
        process = [1, 1, 1, 1]
        k = 0
        expected = 6  # (1,1) appears 6 times
        self.assertEqual(self.solution.getPairsCount(process, k), expected)


if __name__ == '__main__':
    unittest.main()