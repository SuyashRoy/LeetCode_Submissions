# LeetCode Problem 13: Roman to Integer

---
## Problem Description

The problem **"Roman to Integer"** requires converting a Roman numeral string into its integer equivalent. Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D`, and `M`, each with a specific integer value.

### Roman Numeral Rules:
1. Symbols are placed from left to right in order of value, starting with the largest.
2. When a smaller numeral appears before a larger numeral, it is subtracted (e.g., `IV = 4`).
3. Otherwise, the numerals are added together (e.g., `VI = 6`).

### Constraints:
- The input is guaranteed to be a valid Roman numeral within the range from `1` to `3999`.

---

## Approach

The solution uses a **greedy algorithm** to traverse the Roman numeral string and calculate the integer value. The key steps are:

1. **Mapping Roman Symbols to Values**:
    - A dictionary is used to map each Roman numeral symbol to its corresponding integer value.

2. **Iterating Through the String**:
    - Traverse the string from left to right.
    - Compare the current symbol's value with the next symbol's value:
      - If the current value is smaller, subtract it from the total.
      - Otherwise, add it to the total.

3. **Edge Cases**:
    - Handle cases like `IV`, `IX`, `XL`, etc., where subtraction is required.
    - Ensure the algorithm works for the largest Roman numeral `MMMCMXCIX` (3999).

---

## Complexity Analysis

- **Time Complexity**: \(O(n)\), where \(n\) is the length of the Roman numeral string.
- **Space Complexity**: \(O(1)\), as the space used for the dictionary is constant.

---

## Example

### Input:
```plaintext
s = "MCMXCIV"
```

### Output:
```plaintext
1994
```

### Explanation:
- `M = 1000`
- `CM = 900`
- `XC = 90`
- `IV = 4`
- Total = 1000 + 900 + 90 + 4 = 1994

---