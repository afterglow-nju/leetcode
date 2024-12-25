import unittest
from typing import List

class Solution:
    @staticmethod
    def getMin(serverType: str) -> int:
        n = len(serverType)
        dp_0, dp_1 = 0, 0
        if serverType[0] == '0':
            dp_1 = float('inf')
        elif serverType[0] == '1':
            dp_0 = float('inf')
        for i in range(1, n):
            new_dp_0, new_dp_1 = float('inf'), float('inf')
            if serverType[i] in '0?':
                new_dp_0 = min(dp_0, dp_1 + 1)
            if serverType[i] in '1?':
                new_dp_1 = min(dp_1, dp_0 + 1)
            dp_0, dp_1 = new_dp_0, new_dp_1
        return min(dp_0, dp_1)


class TestGetMin(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        serverType = "10?01?"
        expected = 2
        self.assertEqual(self.solution.getMin(serverType), expected)

    def test_example2(self):
        serverType = "??011??0"
        expected = 2
        self.assertEqual(self.solution.getMin(serverType), expected)

    def test_example3(self):
        serverType = "0?1?0?1"
        expected = 3
        self.assertEqual(self.solution.getMin(serverType), expected)

    def test_example4(self):
        serverType = "?????"
        expected = 0
        self.assertEqual(self.solution.getMin(serverType), expected)

    def test_example5(self):
        serverType = "1111?0000?"
        expected = 1
        self.assertEqual(self.solution.getMin(serverType), expected)

    def test_example6(self):
        serverType = "0"
        expected = 0
        self.assertEqual(self.solution.getMin(serverType), expected)

    def test_example7(self):
        serverType = "01"
        expected = 1
        self.assertEqual(self.solution.getMin(serverType), expected)

if __name__ == '__main__':
    unittest.main()