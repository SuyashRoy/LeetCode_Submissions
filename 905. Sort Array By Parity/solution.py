from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while(i <= j):
            if(nums[i] % 2 != 0):
                temp = nums[j]
                nums[j]=nums[i]
                nums[i]=temp
                j-=1
            else:
                i+=1
        return nums

### Example usage:
solution = Solution()
print(solution.sortArrayByParity([3, 1, 2, 4]))  ### Output: [4, 2, 1, 3]
print(solution.sortArrayByParity([0]))  ### Output: [0]