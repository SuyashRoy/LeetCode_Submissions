
---

# **1480: Running Sum of 1d Array**

## **Problem Statement**

Given an integer array `nums`, you need to compute and return the **running sum** of the array.

The running sum is defined as:

```
runningSum[i] = sum(nums[0] + nums[1] + ... + nums[i])
```

Return the resulting running sum array.

---

## **Function Signature**

```python
def runningSum(nums: List[int]) -> List[int]:
    pass
```

### **Input**

* An integer array `nums`, where `1 <= nums.length <= 1000`.
* Each element in `nums` is an integer, where `-10^6 <= nums[i] <= 10^6`.

### **Output**

* Return an integer array that represents the **running sum** of the input array.

---

## **Examples**

### Example 1:

```python
nums = [1, 2, 3, 4]
print(runningSum(nums))
```

**Output:**

```python
[1, 3, 6, 10]
```

**Explanation:** The running sum is calculated as:

* `runningSum[0] = 1`
* `runningSum[1] = 1 + 2 = 3`
* `runningSum[2] = 1 + 2 + 3 = 6`
* `runningSum[3] = 1 + 2 + 3 + 4 = 10`

### Example 2:

```python
nums = [1, 1, 1, 1, 1]
print(runningSum(nums))
```

**Output:**

```python
[1, 2, 3, 4, 5]
```

**Explanation:** The running sum is calculated as:

* `runningSum[0] = 1`
* `runningSum[1] = 1 + 1 = 2`
* `runningSum[2] = 1 + 1 + 1 = 3`
* `runningSum[3] = 1 + 1 + 1 + 1 = 4`
* `runningSum[4] = 1 + 1 + 1 + 1 + 1 = 5`

### Example 3:

```python
nums = [3, 1, 2, 10, 1]
print(runningSum(nums))
```

**Output:**

```python
[3, 4, 6, 16, 17]
```

**Explanation:** The running sum is calculated as:

* `runningSum[0] = 3`
* `runningSum[1] = 3 + 1 = 4`
* `runningSum[2] = 3 + 1 + 2 = 6`
* `runningSum[3] = 3 + 1 + 2 + 10 = 16`
* `runningSum[4] = 3 + 1 + 2 + 10 + 1 = 17`

---

## **Constraints**

* `1 <= nums.length <= 1000`
* `-10^6 <= nums[i] <= 10^6`

---

## **Approach**

To compute the running sum:

1. Traverse the array `nums`.
2. Maintain a cumulative sum that is updated as you iterate through the array.
3. Store the cumulative sum in a new array (or update the original array if required).
4. Continue the summing process for each index in the array.

### **Step-by-Step Plan:**

* Initialize a variable `current_sum` to 0.
* Iterate through each element in the `nums` array.
* At each iteration, add the current element to `current_sum` and update the corresponding index of the result array.
* After processing all elements, the result array will contain the desired running sum.

---

## **Complexity Analysis**

* **Time Complexity:** `O(n)`, where `n` is the length of the input array `nums`. We only need to traverse the array once to compute the running sum.
* **Space Complexity:** `O(n)`, where `n` is the length of the array. The space complexity is due to the output array, which stores the running sum.

---

## **Edge Cases**

* **Single Element Array:** If the array contains just one element, the running sum will be the element itself.

  Example:

  ```python
  nums = [5]
  print(runningSum(nums))  # Output: [5]
  ```

* **Negative Numbers:** The algorithm handles negative numbers in the array by correctly adding them to the running sum.

  Example:

  ```python
  nums = [-1, -2, -3, -4]
  print(runningSum(nums))  # Output: [-1, -3, -6, -10]
  ```

---

## **Additional Notes**

* This solution handles arrays with negative and large values due to the constraints `-10^6 <= nums[i] <= 10^6`.
* The algorithm computes the running sum efficiently in a single pass (`O(n)` time complexity), making it optimal for large arrays.

---
