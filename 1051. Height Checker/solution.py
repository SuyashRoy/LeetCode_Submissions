from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        expectation = [0]* len(heights)
        for i in range(len(heights)):
            expectation[i]=heights[i]
        expectation.sort()
        for i in range(len(heights)):
            if(heights[i] != expectation[i]):
                count+=1
        return count

### Example Usage:
sol = Solution()
print(sol.heightChecker([1,1,4,2,1,3]))  # Output: 3
print(sol.heightChecker([5,1,2,3,4]))    # Output: 5
print(sol.heightChecker([1,2,3,4,5]))    # Output: 0