# LeetCode Problem 46: Permutations

## Problem Description
The problem asks us to return all possible permutations of a given list of distinct integers. Each permutation must be in the form of a unique arrangement of the integers.

**Example:**
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

## Solution Approach

### Approach Used: Backtracking
The solution uses a **backtracking** approach to generate all permutations. Backtracking is a recursive algorithm that explores all possible configurations and backtracks when a configuration is invalid or complete.

### Steps:
1. **Base Case:** If the current permutation is complete (i.e., its length matches the input list), add it to the result.
2. **Recursive Case:** Iterate through the input list and add each unused number to the current permutation. Mark the number as used and recursively build the next level of the permutation.
3. **Backtrack:** After exploring a path, remove the last number from the current permutation and mark it as unused to explore other possibilities.

### Complexity:
- **Time Complexity:** O(n!) - There are n! permutations for a list of size n.
- **Space Complexity:** O(n) - Space used for recursion and tracking the current permutation.

### Code:
Refer to the `solution.py` file for the implementation.

```python
# solution.py
class Solution:
    def permute(self, nums):
        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path, used)
                    path.pop()
                    used[i] = False

        result = []
        backtrack([], [False] * len(nums))
        return result
```

## How to Run
1. Place the `solution.py` file in your working directory.
2. Import the `Solution` class and call the `permute` method with your input list.
3. Example:
   ```python
   from solution import Solution

   nums = [1, 2, 3]
   sol = Solution()
   print(sol.permute(nums))
   ```

## Resources
- [LeetCode Problem 46](https://leetcode.com/problems/permutations/)
- [Backtracking Algorithm](https://en.wikipedia.org/wiki/Backtracking)
