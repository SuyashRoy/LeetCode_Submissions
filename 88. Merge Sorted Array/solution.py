from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n2 = n-1
        if (m == 0):
            for i in range(0, len(nums1)):
                nums1[i]=nums2[i]
        else:
            for i in range((m+n)-1, m - 1, -1):
                if(n2 != -1):
                    nums1[i]=nums2[n2]
                    n2-=1
                else:
                    break
            nums1.sort()
        print(nums1)

### Example usage:
solution = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution.merge(nums1, m, nums2, n)
# Output: nums1 = [1, 2, 2, 3, 5, 6]

nums1_2 = [1]
m2 = 1
nums2_2 = []
n2 = 0
solution.merge(nums1_2, m2, nums2_2, n2)
# Output: nums1_2 = [1]

nums1_3 = [0]
m3 = 0
nums2_3 = [1]
n3 = 1
solution.merge(nums1_3, m3, nums2_3, n3)
# Output: nums1_3 = [1]