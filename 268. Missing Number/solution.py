from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = int(n*(n+1)/2)
        actual_sum = 0
        for num in nums:
            actual_sum += num
        return expected_sum - actual_sum

if __name__ == "__main__":
    solution = Solution()
    print(solution.missingNumber([3, 0, 1])) # 2
    print(solution.missingNumber([0, 1])) # 2
    print(solution.missingNumber([9,6,4,2,3,5,7,0,1])) # 8