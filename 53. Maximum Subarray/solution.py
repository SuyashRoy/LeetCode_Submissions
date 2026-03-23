from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]
        
        sol = 0
        max_val = -100001
        for index, value in enumerate(nums):
            sol += value
            if max_val < sol:
                max_val = sol
            if sol < 0:
                sol = 0
        return max_val

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) ### 6

