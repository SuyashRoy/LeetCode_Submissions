from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count = 0 ### Counter to determine the # of 0s
        j = 0
        for i in range(0, len(arr)):
            if arr[i] == 0:
                count+=1

        ### Declaring a new array with the required size
        new_arr_len = len(arr) + count
        addition = [0] * new_arr_len
        j = new_arr_len - 1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 0:
                addition[j]= 0
                j-=1
                addition[j]= 0
                j-=1
            else:
                addition[j]=arr[i]
                j-=1

        for i in range(0, len(arr)):
            arr[i]=addition[i]

### Example usage:
sol = Solution()
arr = [1,0,2,3,0,4,5,0]
sol.duplicateZeros(arr)
print(arr)  ### Output should be [1,0,0,2,3,0,0,4]

### Example usage with no zeros:
arr_2 = [1,2,3]
sol.duplicateZeros(arr_2)
print(arr_2)  ### Output should be [1,2,3]