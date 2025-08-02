from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            if(num!=val):
                nums[k]=num
                k+=1
        return k

### Example usage:
solution = Solution()
nums = [3, 2, 2, 3]
val = 3
k = solution.removeElement(nums, val)
print(k)  ### Output: 2
print(nums[:k])  ### Output: [2, 2]