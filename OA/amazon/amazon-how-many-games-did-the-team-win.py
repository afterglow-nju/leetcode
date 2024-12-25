import unittest
from typing import List


class Solution:
  def howManyGamesDidTheyWin(self, n: int, g1: List[int], g2: List[int]) -> int:
    diff=[g1[i]-g2[i] for i in range(n)]
    diff.sort()
    left,right=0,1
    ret=0
    mod=10**9+7
    for right in range(1,n):
      if diff[left]+diff[right]>0:
        continue
      else:
        ret+=(right-1-left)%mod
        while left<right and diff[left]+diff[right]<=0:
          left+=1
    while left<n-1:
        ret=(ret+n-1-left)%mod
        left+=1
    print(left,right,ret)
    
    return ret



class TestGetPairsCount(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        n = 3
        g1 = [1, 2, 3]
        g2 = [3, 2, 1]
        #[-2,0,2]
        expected=1
        self.assertEqual(self.solution.howManyGamesDidTheyWin(n, g1,g2), expected)


    def test_example1(self):
        n = 3
        g1 = [1, 2, 3]
        g2 = [3, 2, 1]
        expected = 1
        self.assertEqual(self.solution.howManyGamesDidTheyWin(n, g1, g2), expected)

    def test_example2(self):
        n = 2
        g1 = [1, 1]
        g2 = [1, 1]
        # All games will be ties
        expected = 0
        self.assertEqual(self.solution.howManyGamesDidTheyWin(n, g1, g2), expected)

    def test_example3(self):
        n = 4
        g1 = [2, 3, 4, 5]
        g2 = [1, 2, 3, 4]
        # g1 wins most games as all their values are higher
        expected = 5  # out of 6 possible pairs
        self.assertEqual(self.solution.howManyGamesDidTheyWin(n, g1, g2), expected)

    def test_example4(self):
        n = 3
        g1 = [1, 1, 1]
        g2 = [2, 2, 2]
        # g2 wins all games
        expected = 0
        self.assertEqual(self.solution.howManyGamesDidTheyWin(n, g1, g2), expected)

    def test_example5(self):
        n = 5
        g1 = [10, 20, 30, 40, 50]
        g2 = [1, 2, 3, 4, 5]
        # g1 wins all games due to much higher values
        expected = 10  # 5C2 = 10 pairs
        self.assertEqual(self.solution.howManyGamesDidTheyWin(n, g1, g2), expected)

    def test_max_constraints(self):
        n = 10**5
        g1 = [10**9] * n
        g2 = [1] * n
        # Test with maximum allowed values
        # Result should be (n * (n-1) // 2) % (10**9 + 7)
        expected = (n * (n-1) // 2) % (10**9 + 7)
        self.assertEqual(self.solution.howManyGamesDidTheyWin(n, g1, g2), expected)

if __name__ == '__main__':
    unittest.main()