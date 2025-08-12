from typing import List
import math

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_dif = 1000
        min_pair = []
        for i in range(len(arr) - 1):
            if math.fabs(arr[i+1] - arr[i]) <= min_dif:
                min_dif = math.fabs(arr[i+1] - arr[i])
        
        for i in range(len(arr) - 1):
            if math.fabs(arr[i+1] - arr[i]) == min_dif:
                min_pair.append([arr[i],arr[i+1]])
        return min_pair

### Example usage:
sol = Solution()
print(sol.minimumAbsDifference([4,2,1,3]))  ### Output: [[1,2],[2,3],[3,4]]
print(sol.minimumAbsDifference([1,3,6,10,15]))  ### Output: [[1,3]]
print(sol.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))  ### Output: [[-14,-10],[19,23],[23,27]]