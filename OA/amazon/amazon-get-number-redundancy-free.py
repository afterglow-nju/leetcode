import unittest
from typing import List

class Solution:
  def getNumberRedundancyFree(self, password: str) -> int:
    s=set()
    ret=0
    for i in password:
      if i in s:
        s=set()
        s.add(i)
        ret+=1
      else:
        s.add(i)
    if s:
      ret+=1
    return ret



class TestGetPairsCount(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        password="aabcdea"
        expected=3
        self.assertEqual(self.solution.getNumberRedundancyFree(password), expected)
        
    def test_example2(self):
        password="alabama"
        expected=4
        self.assertEqual(self.solution.getNumberRedundancyFree(password), expected)

    def test_example3(self):
        password="zebra"
        expected=1
        self.assertEqual(self.solution.getNumberRedundancyFree(password), expected)




if __name__ == '__main__':
    unittest.main()