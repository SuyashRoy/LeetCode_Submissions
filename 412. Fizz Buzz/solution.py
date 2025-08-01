from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [0] * n
        for i in range(1, n+1):
            if (i % 3 == 0 and i % 5 == 0):
                answer[i-1]="FizzBuzz"
            elif (i % 3 == 0):
                answer[i-1]= "Fizz"
            elif(i % 5 == 0):
                answer[i-1]="Buzz"
            else:
                answer[i-1]= str(i)
        return answer

### Example usage:
sol = Solution()
n = 3
n2 = 5
n3 = 15
print(sol.fizzBuzz(n))   # Output: ["1", "2", "Fizz"]
print(sol.fizzBuzz(n2))  # Output: ["1", "2", "Fizz", "4", "Buzz"]
print(sol.fizzBuzz(n3))  # Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]

### Note: The code is written in Python, but the logic is similar to Java.