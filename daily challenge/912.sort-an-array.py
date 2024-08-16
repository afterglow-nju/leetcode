class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import random
        def quicksort(arr):
            if len(arr)<=1:
                return arr
            else:
                pivot=arr[random.randint(0,len(arr)-1)]
                left=[x for x in arr if x<pivot]
                middle=[x for x in arr if x==pivot]
                right=[x for x in arr if x>pivot]
                return quicksort(left)+middle+quicksort(right)
        return quicksort(nums)