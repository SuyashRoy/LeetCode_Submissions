from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = [-1] * (len(digits))
        carry = 0
        
        if digits == [9]:
            return [1, 0]
        
        for i in range(len(digits)-1, -1, -1):
            result[i] = digits[i]
            if i== len(digits)-1:
            
                if digits[i] != 9:
                    result[i]+=1
                else:
                    result[i]= 0
                    carry = 1
            else:
                if carry > 0:
                    if result[i] != 9:
                        result[i]+=carry
                        carry = 0
                    else:
                        result[i] += 1
                        carry = 1
                    
        if result[0] > 9:
            result.append(0)
            for i in range(len(digits)):
                if i != 0:
                    result[i+1] = result[i]
                else:
                    result[0] = 1
                    result[1] = 0
        
        for i in range(len(digits)):
            if result[i] == 10:
                result[i] = 0
                    
        return result

### Example usage:
solution = Solution()
print(solution.plusOne([1, 2, 3]))  ### Output: [1, 2, 4]
print(solution.plusOne([9, 9, 9]))  ### Output: [1, 0, 0, 0]
print(solution.plusOne([4, 3, 2, 1]))  ### Output: [4, 3, 2, 2]
print(solution.plusOne([9]))  ### Output: [1, 0]
                    