from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        j=0
        for i in range(len(nums)):
            if ((k<1) or (nums[i] > nums[i-1])):
                nums[k]=nums[i]
                k+=1
        for i in range(len(nums)):
            if((i == 0) or (nums[i] != nums[i-1])):
                if(j < k):
                    nums[j] = nums[i]
                    j+=1

        return k

### Example usage:
solution = Solution()
nums = [1, 1, 2]
k = solution.removeDuplicates(nums)
print(k)  ### Output: 2
print(nums[:k])  ### Output: [1, 2]

nums_2 = [0,0,1,1,1,2,2,3,3,4]
k_2 = solution.removeDuplicates(nums_2)
print(k_2)  ### Output: 5
print(nums_2[:k_2])  ### Output: [0, 1, 2, 3, 4]