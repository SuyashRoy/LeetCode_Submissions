import math

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = [0] * len(nums)
        k = 0
        j = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if(math.fabs(nums[j]) < math.fabs(nums[k])):
                output[i]=nums[k]*nums[k]
                k+=1
            else:
                output[i]=nums[j]*nums[j]
                j-=1
        return output

# class Solution(object):
#     def sortedSquares(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         output = []
#         for num in nums:
#             output.append(num * num)
#         output.sort()
#         return output

### Example usage:
solution = Solution()
print(Solution().sortedSquares([-4,-1,0,3,10]))  # Output: [0, 1, 9, 16, 100]
print(Solution().sortedSquares([-7,-3,2,3,11]))  # Output: [4, 9, 9, 49, 121]
