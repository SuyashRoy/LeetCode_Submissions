from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0
        j = i+1
        key = False
        while(i != j):
            if(len(arr) == 0 or len(arr) == 1):
                key = False
                break
            if(arr[i] == 2*arr[j]):
                key = True
                break
            if(j != len(arr)):
                j+=1
                if(j == i):
                    j = i+1
            if(j == len(arr)):
                j = 0
                i+=1
            if(i >= len(arr)):
                key = False
                break
        return key

### Example usage:
solution = Solution()
print(solution.checkIfExist([10, 2, 5, 3]))  # Output: True
print(solution.checkIfExist([3,1,7,11]))  # Output: False