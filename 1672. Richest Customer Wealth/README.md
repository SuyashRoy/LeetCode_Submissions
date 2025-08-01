
---

# Richest Customer Wealth

**Leetcode Problem 1672**
[View on LeetCode](https://leetcode.com/problems/richest-customer-wealth/)

## Problem Statement

You are given an `m x n` integer grid `accounts` where `accounts[i][j]` is the amount of money the `i`<sup>th</sup> customer has in the `j`<sup>th</sup> bank.
Return the **wealth that the richest customer has**.

A customer's **wealth** is defined as the **sum of money in all their bank accounts**.
The richest customer is the one with the **maximum total wealth**.

---

### Example 1:

```
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6

Explanation:
Customer 1 wealth = 1 + 2 + 3 = 6  
Customer 2 wealth = 3 + 2 + 1 = 6  
Both customers have wealth = 6, so the richest has 6.
```

### Example 2:

```
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10

Explanation:
Customer 1 wealth = 6  
Customer 2 wealth = 10  
Customer 3 wealth = 8  
Richest customer has wealth = 10
```

### Example 3:

```
Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
```

---

### Constraints

* `m == accounts.length`
* `n == accounts[i].length`
* `1 <= m, n <= 50`
* `1 <= accounts[i][j] <= 100`

---

## Solution

The algorithm iterates over each customer's list of accounts, calculates the total wealth, and keeps track of the maximum wealth encountered.

### Example Usage

```python
sol = Solution()

accounts = [[1,2,3],[3,2,1]]
print(sol.maximumWealth(accounts))  # Output: 6

accounts_2 = [[1,5],[7,3],[3,5]]
print(sol.maximumWealth(accounts_2))  # Output: 10

accounts_3 = [[2,8,7],[7,1,3],[1,9,5]]
print(sol.maximumWealth(accounts_3))  # Output: 17
```

---