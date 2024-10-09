from collections import defaultdict

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0
        
        pre = 0  # Initialize prefix sum
        d = {0: -1}  # Map to store prefix sums and their indices
        ret = len(nums)
        
        for i, num in enumerate(nums):
            pre = (pre + num) % p  # Current prefix sum mod p
            mod_needed = (pre - target) % p
            
            if mod_needed in d:
                ret = min(ret, i - d[mod_needed])  # Found a valid subarray
            
            d[pre] = i  # Update the dictionary with the current prefix sum
            
        return ret if ret <len(nums) else -1