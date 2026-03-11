from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # arr = []
        # sol = []
        # while len(sol) != math.factorial(len(nums)):
        #     while len(arr) != len(nums):
        #         num = nums[random.randrange(0, len(nums))]
        #         if num not in arr:
        #             arr.append(num)
        #     if arr not in sol:
        #         sol.append(arr)
        #     arr = []
        # return sol
        
        sol = [[]]
        for num in nums:
            part_sol = []
            for mini_sol in sol:
                for i in range(len(mini_sol)+1):
                    mini_sol_copy = mini_sol.copy()
                    mini_sol_copy.insert(i,num)
                    part_sol.append(mini_sol_copy)
            sol = part_sol
        return sol

# Example usage:
solution = Solution()
print(solution.permute([1, 2, 3]))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]