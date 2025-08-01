from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = len(accounts)
        max = 0
        for i in range(0,m):
            balance = 0
            n = len(accounts[i])
            for j in range(0,n):
                balance = balance + accounts[i][j]
            if (balance > max):
                max = balance
        return max

### Example usage:
sol = Solution()

accounts = [[1,2,3],[3,2,1]]
print(sol.maximumWealth(accounts))  ### Output should be 6

### Example usage with different accounts:
accounts_2 = [[1,5],[7,3],[3,5]]
print(sol.maximumWealth(accounts_2))  ### Output should be 10

### Example usage with three accounts:
accounts_3 = [[2,8,7],[7,1,3],[1,9,5]]
print(sol.maximumWealth(accounts_3))  ### Output should be 17