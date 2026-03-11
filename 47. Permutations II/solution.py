from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = [[]]
        for num in nums:
            part_sol = []
            for mini_sol in sol:
                for i in range(len(mini_sol) + 1):
                    new_sol = mini_sol[:i] + [num] + mini_sol[i:]
                    part_sol.append(new_sol)
                    if i < len(mini_sol) and mini_sol[i] == num:
                        break
            sol = part_sol
        return sol

# Example usage:
solution = Solution()
print(solution.permuteUnique([1, 1, 2]))  # Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]