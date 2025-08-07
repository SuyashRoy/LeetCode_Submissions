from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            right_sum = total - num -left_sum
            if right_sum == left_sum:
                return i
            left_sum+=num
        return -1
        
    
### Example usage:
sol = Solution()
print(sol.pivotIndex([2, 3, -1, 8, 4]))  ### Output: 3
print(sol.pivotIndex([1, -1, 4]))  ### Output: 2
print(sol.pivotIndex([2, 5]))  ### Output: -1