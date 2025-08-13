from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = sorted(nums)
        return result[len(result) - k]

### Example usage:
solution = Solution()
print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5], 4))  # Output: 4