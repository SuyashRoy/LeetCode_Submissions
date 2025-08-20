from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        nums_copy = nums.copy()
        nums_copy.sort()
        j = len(nums) - 1
        i = 0
        while i < j:
            temp = (nums_copy[i] + nums_copy[j])
            if temp < target:
                i+=1
            elif temp > target:
                j-=1
            elif temp == target:
                a = nums_copy[i]
                b = nums_copy[j]
                break

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == b:
                return [nums.index(a), i]

### Example Usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  ### Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))  ### Output: [1, 2]
print(solution.twoSum([3, 3], 6))  ### Output: [0, 1]