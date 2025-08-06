from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        elif numRows == 1:
            return [[1]]
        
        rows = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0 or i == j:
                    row.append(1)
                else:
                    row.append(rows[i-1][j-1] + rows[i-1][j])
            rows.append(row)
        return rows
    
### Example usage:
solution = Solution()
print(solution.generate(5))  ### Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print(solution.generate(0))  ### Output: []
print(solution.generate(1))  ### Output: [[1]]