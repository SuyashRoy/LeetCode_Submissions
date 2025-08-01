from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        window = 0
        for i in range(0, len(nums)):
            if(nums[i]==1):
                counter+=1
                if(counter > window):
                    window = counter
            else:
                counter = 0
        return window

### Example usage:
solution = Solution()
print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))  ### Output: 3
print(solution.findMaxConsecutiveOnes([1,0,1,1,0,1]))  ### Output: 2
print(solution.findMaxConsecutiveOnes([0,0,0,0]))      ### Output: 0