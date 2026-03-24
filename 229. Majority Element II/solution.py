from typing import List
import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        sol = []
        hashmap = {}
        threshold = math.floor(len(nums)/3) + 1
        if len(nums) == 1:
            return nums
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            if hashmap[num] == threshold:
                sol.append(num)
        return sol
        # counts = Counter(nums)
        # for value in nums:
        #     if counts[value] > threshold and value not in sol:
        #         sol.append(value)
        # return sol

if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,2,3])) ### [3]
    print(sol.majorityElement([1])) ### [1]
    print(sol.majorityElement([1,2])) ### [1,2]