from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_element = 0
        max_index = 0
        
        for i, num in enumerate(nums):
            if max_element < num:
                max_element = num
                max_index = i
        
        for i in range(len(nums)):
            if i != max_index:
                if max_element < 2*nums[i]:
                    return -1
            else:
                continue
        return max_index
                
### Example usage:
sol = Solution()
print(sol.dominantIndex([3, 6, 1, 0]))  ### Output: 1
print(sol.dominantIndex([1, 2, 3, 4]))    ### Output: -1