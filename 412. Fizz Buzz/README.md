
---

# Fizz Buzz

**Leetcode Problem 412**
[View on LeetCode](https://leetcode.com/problems/fizz-buzz/)

## Problem Statement

Given an integer `n`, return a string array `answer` (1-indexed) where:

* `answer[i] == "FizzBuzz"` if `i` is divisible by both **3 and 5**
* `answer[i] == "Fizz"` if `i` is divisible by **3**
* `answer[i] == "Buzz"` if `i` is divisible by **5**
* `answer[i] == i` (as a string) if none of the above conditions are true

---

### Examples

#### Example 1:

```
Input: n = 3
Output: ["1", "2", "Fizz"]
```

#### Example 2:

```
Input: n = 5
Output: ["1", "2", "Fizz", "4", "Buzz"]
```

#### Example 3:

```
Input: n = 15
Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
```

---

### Constraints

* `1 <= n <= 10⁴`

---

## Methodology

To solve this problem, iterate through the numbers from `1` to `n`. For each number:

1. Check if it's divisible by both 3 and 5:

   * If so, add `"FizzBuzz"` to the result list.
2. If not, check if it's divisible by only 3:

   * If so, add `"Fizz"`.
3. If not, check if it's divisible by only 5:

   * If so, add `"Buzz"`.
4. If none of the above, convert the number to a string and add it to the result.

This ensures that each number from 1 to `n` is evaluated against the Fizz Buzz conditions and added appropriately to the output list.

---

## Complexity Analysis

* **Time Complexity**: O(n) — You loop through the numbers once.
* **Space Complexity**: O(n) — You store `n` strings in the result list.

---