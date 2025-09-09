class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_map = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        numbers = []
        total = 0
        carry = 0

        for string in s:
            for symbol in symbol_map:
                if symbol_map[symbol] == string:
                    numbers.append(symbol)
        
        for i in range(0, len(numbers) - 1):
            if numbers[i] >= numbers[i+1]:
                total+=numbers[i]
            else:
                carry+=numbers[i]
        total += numbers[len(numbers) - 1]
        total = total - carry
        return total

### Example Usage
solution = Solution()
print(solution.romanToInt("III"))      ### Output: 3
print(solution.romanToInt("LVIII"))    ### Output: 58
print(solution.romanToInt("MCMXCIV"))  ### Output: 1994