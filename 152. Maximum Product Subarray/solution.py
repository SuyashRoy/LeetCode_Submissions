from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = -11
        prefix = 1
        suffix = 1
        for index in range(0, len(nums)):
            prefix *= nums[index]
            suffix *= nums[len(nums) - index - 1]
            maxProd = max(maxProd, max(prefix, suffix))
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
        return maxProd

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct([2, 3, -2, 4])) # 6
    print(solution.maxProduct([-2, 0, -1])) # 0
    print(solution.maxProduct([-2, 3, -4])) # 24