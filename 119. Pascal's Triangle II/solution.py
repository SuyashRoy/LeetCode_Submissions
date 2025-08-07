from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = []
        for i in range(rowIndex + 1):
            row = []
            for j in range(i+1):
                if j==0 or i==j:
                    row.append(1)
                else:
                    row.append(rows[i-1][j-1] + rows[i-1][j])
            rows.append(row)  

        return rows[rowIndex]
    
### Example usage:
sol = Solution()
print(sol.getRow(0))  ### Output: [1]
print(sol.getRow(1))  ### Output: [1, 1]
print(sol.getRow(2))  ### Output: [1, 2, 1]
print(sol.getRow(3))  ### Output: [1, 3, 3, 1]