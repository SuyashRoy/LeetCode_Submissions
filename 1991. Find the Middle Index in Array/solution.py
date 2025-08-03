from typing import List

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = 0
        for i in range(0, len(nums)):
            if i == 0:
                left_sum = 0
            else:
                for j in range(0,i):
                    left_sum+=nums[j]
            if i == len(nums) - 1:
                right_sum = 0
            else:
                for k in range(len(nums) -1, i, -1):
                    right_sum+=nums[k]
            if left_sum == right_sum:
                return i
            elif left_sum != right_sum and i == len(nums) - 1:
                return -1
            left_sum = 0
            right_sum = 0

### Example usage:
sol = Solution()
print(sol.findMiddleIndex([2, 3, -1, 8, 4]))  ### Output: 3
print(sol.findMiddleIndex([1, -1, 4]))  ### Output: 2
print(sol.findMiddleIndex([2, 5]))  ### Output: -1
