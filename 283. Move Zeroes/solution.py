from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[j] = nums[i]
                j+=1
        for i in range(len(nums)):
            if(i>=j):
                nums[i]=0

### Example usage:
solution = Solution()
nums = [0, 1, 0, 3, 12]
nums2 = [0]
solution.moveZeroes(nums)
solution.moveZeroes(nums2)
print(nums)  # Output should be [1, 3, 12, 0, 0]
print(nums2)  # Output should be [0]