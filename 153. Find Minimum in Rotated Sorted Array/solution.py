from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0, len(nums) - 1
        min_element = 5001
        while left <= right:
            middle = (left + right) // 2
            min_element = min(nums[left], nums[middle], nums[right], min_element)
            if nums[left] < nums[right]:
                if nums[left] < nums[middle]:
                    right = middle - 1
                else:
                    left += 1
            else:
                if nums[right] < nums[middle]:
                    left = middle + 1
                else:
                    right -= 1
            # min_element = min(nums[left], nums[middle], nums[right], min_element)
        return min_element

# Example usage:
solution = Solution()
print(solution.findMin([3,4,5,1,2]))  # Output: 1
print(solution.findMin([4,5,6,7,0,1,2]))  # Output: 0