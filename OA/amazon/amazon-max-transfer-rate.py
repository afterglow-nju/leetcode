import unittest
from typing import List
from collections import defaultdict

class Solution:
  def maxTransferRate(self, throughput: List[int], k: int) -> int:
    n = len(throughput)
    throughput.sort(reverse=True)
    max_heap = []
    result = 0
    import heapq
    # Initialize the heap with self-pairs (i, i)
    for i in range(n):
        # Push (-sum, index1, index2) into the heap
        heapq.heappush(max_heap, (-(throughput[i] + throughput[i]), i, i))
    
    # Extract the top-k pairs
    
    index=0
    while max_heap and index < k:
        # Get the largest sum pair
        neg_sum, i, j = heapq.heappop(max_heap)
        print(i,j)
        result+=throughput[i]+throughput[j]
        index+=1
        # If possible, push the next candidate pair (i, j+1)
        if j + 1 < n:
            heapq.heappush(max_heap, (-(throughput[i] + throughput[j + 1]), i, j + 1))
        
        # If possible, push the next candidate pair (j, i+1)
        if i + 1 < n  :  # Avoid duplicates for self-pairs
            heapq.heappush(max_heap, (-(throughput[j] + throughput[i + 1]), j, i + 1))
    
    return result

class TestGetStablePeriodsCount(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()  # Assume the `Solution` class has `getStablePeriodsCount` implemented.

    def test_example1(self):
        throughput = [4,2,5]
        k = 4
        expected = 36
        #5,4,2
        # 5+5,5+4,4+5,
        self.assertEqual(self.solution.maxTransferRate(throughput,k), expected)



if __name__ == '__main__':
    unittest.main()