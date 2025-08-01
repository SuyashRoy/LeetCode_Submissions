class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while(num != 0):
            if (num % 2 == 0):
                num /= 2
                counter += 1
            else:
                num -= 1
                counter += 1
        return counter

### Example usage:
sol = Solution()
num = 14
num2 = 8
num3 = 123
print(sol.numberOfSteps(num))   ### Output: 6
print(sol.numberOfSteps(num2))  ### Output: 4
print(sol.numberOfSteps(num3))  ### Output: 12