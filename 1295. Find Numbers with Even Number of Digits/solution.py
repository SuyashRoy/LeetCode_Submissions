from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        countNumbers = 0
        for i in range(0, len(nums)):
            countDigits = 0
            number = nums[i]
            while(number != 0):
                number //= 10
                countDigits+=1
            if (countDigits % 2 == 0):
                countNumbers+=1
        return countNumbers

### Example usage:
solution = Solution()
print(solution.findNumbers([12, 345, 2, 6, 7896]))  ### Output: 2
print(solution.findNumbers([555, 901, 482, 1771]))  ### Output: 1