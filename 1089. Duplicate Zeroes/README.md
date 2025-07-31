
---

# **1089: Duplicate Zeroes**

## **Problem Statement**

Given a fixed-length integer array `arr`, your task is to **duplicate each occurrence of zero** in the array while **shifting the remaining elements to the right**. This modification must be done **in place**, meaning that you cannot use extra space to store the result. Additionally, you should not return anything, and the array should be modified directly.

**Note:**

* Elements beyond the length of the original array should not be written.
* If multiple zeros are present, all of them must be duplicated.

---

## **Function Signature**

```python
def duplicateZeros(arr: List[int]) -> None:
    pass
```

### **Input**

* An integer array `arr` where `1 <= arr.length <= 10^4`.
* Each element in `arr` is a non-negative integer: `0 <= arr[i] <= 9`.

### **Output**

* Modify the given list `arr` in place. There is no return value.

---

## **Examples**

### Example 1:

```python
arr = [1,0,2,3,0,4,5,0]
duplicateZeros(arr)
print(arr)
```

**Output:**

```python
[1, 0, 0, 2, 3, 0, 0, 4]
```

**Explanation:** The zero at index 1 is duplicated, and the rest of the elements are shifted to the right. The same happens for the second zero at index 4, and the array becomes `[1, 0, 0, 2, 3, 0, 0, 4]`.

### Example 2:

```python
arr = [1, 2, 3]
duplicateZeros(arr)
print(arr)
```

**Output:**

```python
[1, 2, 3]
```

**Explanation:** No zeros are present in the array, so the array remains unchanged.

---

## **Constraints**

* `1 <= arr.length <= 10^4`
* `0 <= arr[i] <= 9`

---

## **Approach**

The goal is to **duplicate the zeros** while **shifting the remaining elements to the right**, all while modifying the array **in place**.

### **Step-by-Step Plan:**

1. **Identify the number of zeros** in the array and determine how many elements will be shifted.
2. **Shift elements** to make space for duplicated zeros. This needs to be done from the **end of the array** to the **beginning** to avoid overwriting elements that have not yet been moved.
3. For each zero found, insert an extra zero in the correct position and shift the subsequent elements.

---

## **Edge Cases**

* **No zeros:** If the array contains no zeros, the array should remain unchanged.
* **Array with only zeros:** The array should handle arrays where all elements are zeros correctly by duplicating all of them.

---

## **Complexity Analysis**

* **Time Complexity:** `O(n)` where `n` is the length of the input array. We traverse the array a constant number of times (once for counting and once for shifting).
* **Space Complexity:** `O(1)` because we are modifying the array in place without using any extra space.

---

## **Additional Notes**

* This problem requires modifying the array in place, which means we cannot use additional data structures like another list or array for holding intermediate results.
* Be careful about index shifting; as you duplicate zeros, you may run into situations where elements need to be moved after other modifications.

---