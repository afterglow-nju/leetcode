import unittest
from typing import List
from collections import defaultdict

class Solution:
  def maxTransferRate(self, throughput: List[int], n: int) -> int:
    ret=0
    h=[[-throughput[i],i] for i in range(len(throughput)) ]
    import heapq
    heapq.heapify(h)
    i=0
    while i <n:
      tem=heapq.heappop(h)
      i+=1
      ret+=-2*tem[0]
      more=h[0]
      if n-1-i+1>=2:
        ret+=-2*(tem[0]-more[0])
        i+=2
      else:
        ret+=-(tem[0]-more[0])
        i+=1
    return ret

class TestGetStablePeriodsCount(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()  # Assume the `Solution` class has `getStablePeriodsCount` implemented.

    def test_example1(self):
        throughput = [4,2,5]
        n = 4
        expected = 36
        self.assertEqual(self.solution.maxTransferRate(throughput,n), expected)



if __name__ == '__main__':
    unittest.main()