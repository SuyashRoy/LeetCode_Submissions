from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        n = len(nums)  ### Get the length of the input list
        counter = 0  ### Initialize a counter variable to keep track of the sum
        running_sum = [0] * n  ### Create a list to store the running sum
        
        for i in range(n):
            if i == 0:
                counter = nums[i]
                running_sum[i] = nums[i]
            else:
                counter += nums[i]
                running_sum[i] = counter
        
        return running_sum

### Example usage:
sol = Solution()
nums = [1, 2, 3, 4]
result = sol.runningSum(nums)
print(result)  ### Output should be [1, 3, 6, 10]

### Example usage:
nums_2 = [1, 1, 1, 1, 1]
result_2 = sol.runningSum(nums_2)
print(result_2)  ### Output should be [1, 2, 3, 4, 5]

### Example usage:
nums_3 = [3, 1, 2, 10, 1]
result_3 = sol.runningSum(nums_3)
print(result_3)  ### Output should be [3, 4, 6, 16, 17]

