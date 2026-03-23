from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        for index, value in enumerate(nums):
            if index != 0 and value == nums[index - 1]:
               continue
            j = len(nums) - 1
            i = index + 1
            while i < j:
                if (nums[i] + nums[j] + value) < 0:
                    i+=1
                elif (nums[i] + nums[j] + value) > 0:
                    j-=1
                elif (nums[i] + nums[j] + value) == 0:
                    sol.append([value, nums[i], nums[j]])
                    i += 1
                    while nums[i] == nums[i - 1] and i < j:
                        i+=1
        return sol
        #     for idx in range(index + 1, len(nums)):
        #         num_2 = nums[idx]
        #         if idx + 1 != len(nums):
        #             num_3 = nums[idx + 1]
        #         if (num_1 + num_2 + num_3) == 0 and [num_1, num_2, num_3] not in sol:
        #             sol.append([num_1, num_2, num_3])
        # return sol

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4])) ### [[-1,-1,2],[-1,0,1]]

