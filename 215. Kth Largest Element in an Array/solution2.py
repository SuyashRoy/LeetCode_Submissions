from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
                
        return min_heap[0]

### Example usage:
solution = Solution()
print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5], 4))  # Output: 4

            
                
