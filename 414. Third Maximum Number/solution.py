from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        i = nums[0]
        j = nums[0]
        k = nums[0]
        if(len(nums) - 1 == 1):
            return nums[1]
        if(len(nums) - 1 == 0):
            return nums[0]
        for m in range(len(nums)):
            if(nums[m]<i):
                if(nums[m]<j):
                    if(i==j):
                        j = nums[m]
                    if(nums[m]<k):
                        if(i==k or j==k):
                            k = nums[m]
                    if(nums[m]>k):
                        k = nums[m]
                if(nums[m]>j):
                    k = j
                    j = nums[m]
            if(i<nums[m]):
                k = j
                j = i
                i = nums[m]
        if (k==j or k==i):
            return i
        return k

### Example usage:
solution = Solution()
print(solution.thirdMax([3, 2, 1]))  ### Output: 1
print(solution.thirdMax([1, 2]))  ### Output: 2
print(solution.thirdMax([2, 2, 3, 1]))  ### Output: 1