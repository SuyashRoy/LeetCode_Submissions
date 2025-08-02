from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        count = 0
        key = False
        index = 0
        if(len(arr) < 3):
            key = False
            return key
        while (i != len(arr) - 1):
            if(arr[index] < arr[i]):
                index = i
            i+=1
        if (index == 0 or index == len(arr) -1):
            key = False
            return key
        i = 0
        while (i < index):
            if(arr[i] >= arr[i+1]):
                key = False
                return key
            if(arr[i]<arr[i+1]):
                key = True
                if(arr[index]==arr[i+1]):
                    key = True
                    count+=1
            if(count>1):
                key = False
                return key
            i+=1
        i = len(arr) - 1
        count = 0
        while (i > index):
            if(arr[i] >= arr[i-1]):
                key = False
                return key
            if(arr[i]<arr[i-1]):
                key = True
                if(arr[index]==arr[i-1]):
                    key = True
                    count+=1
            if(count>1):
                key = False
                return key
            i-=1
        return key

### Example usage:
solution = Solution()
print(solution.validMountainArray([2, 1]))  ### Output: False
print(solution.validMountainArray([3, 5, 5]))  ### Output: False
print(solution.validMountainArray([0, 3, 2, 1]))  ### Output: True