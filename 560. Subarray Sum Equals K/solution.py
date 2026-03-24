from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        curr_sum = 0
        hashmap = {0:1}
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            counter += hashmap.get(diff, 0)
            hashmap[curr_sum] = hashmap.get(curr_sum, 0) + 1
        return counter

if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1,1,1], 2)) ### 2
    print(sol.subarraySum([1,2,3], 3)) ### 2
    print(sol.subarraySum([1], 0)) ### 0