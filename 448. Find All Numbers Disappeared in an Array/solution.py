from typing import List
import math

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        index = 0
        solution = []
        # List<Integer> solution = new ArrayList<>();
        for i in range(len(nums)):
            index = math.floor(math.fabs(nums[i])) - 1
            if(nums[index] > 0):
                nums[index] = -nums[index]
        for i in range(len(nums)):
            if(nums[i] > 0):
                solution.append(i+1)
        return solution

### Example usage:
sol = Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # Output: [5, 6]
print(sol.findDisappearedNumbers([1, 1]))  # Output: [2]
    