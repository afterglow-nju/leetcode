import unittest
from typing import List
from collections import defaultdict


class Solution:
  def findMaximumNum(self, answered: List[int], needed: List[int], q: int) -> int:
    d=[needed[i]-answered[i] for i in range(len(needed))]
    d.sort()
    ret=0
    for i in range(len(d)):
      if q>=d[i]:
        q-=d[i]
        ret+=1
      else:
        break
    return ret

class TestGetStablePeriodsCount(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()  # Assume the `Solution` class has `getStablePeriodsCount` implemented.

    def test_example1(self):
        answered = [24, 27, 0]
        needed = [51, 52, 100]
        q = 100
        expected = 2
        #5 4 2
        # 5+5,5+4,4+5,
        self.assertEqual(self.solution.findMaximumNum(answered,needed,q), expected)



if __name__ == '__main__':
    unittest.main()