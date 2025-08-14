from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        white_count = 0
        red_count = 0
        blue_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                red_count +=1
            elif nums[i] == 1:
                white_count +=1
            elif nums[i] == 2:
                blue_count +=1
        for i in range(red_count):
            nums[i]=0
        for j in range(white_count):
            nums[j+red_count] = 1
        for k in range(blue_count):
            nums[k + red_count + white_count] = 2
        
        return nums

        # return nums.sort()
            
### Example usage:
solution = Solution()
print(solution.sortColors([2, 0, 2, 1, 1, 0]))  # Output: [0, 0, 1, 1, 2, 2]
print(solution.sortColors([2, 0, 1]))  # Output: [0, 1, 2]