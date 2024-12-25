class Solution:
      def getOutlierValue(self, arr: List[int]) -> int:
    #Step 1
    max_val = max(arr)
    max_index = arr.index(max_val)

    #Step 2, check if max(arr) is the outlier
    arr_without_max = arr[:max_index] + arr[max_index+1:]
    second_max = max(arr_without_max)
    second_max_index = arr_without_max.index(second_max)
    arr_without_second_max = arr_without_max[:second_max_index] + arr_without_max[second_max_index+1:]
    if sum(arr_without_second_max) == second_max:
      #Max is the largest outlier
      return max_val
      
    #Step 3: If max is not an outlier, it must be the sum of other elements because all 
    #elements in arr are positive by constraint
    sum_others = sum(arr_without_max)

    #Step 4: outlier = sum_others - max
    outlier = sum_others - max_val

    #Step 5: Because it is guaranteed by the problem an outlier exists, just return it
    return outlier