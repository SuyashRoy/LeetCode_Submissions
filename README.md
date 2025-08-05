
---

# **LeetCode\_Submissions**

## Overview

Enclosed are LeetCode problem solutions detailing progression in coding via gradual increase in problem difficulty. These problems aim to enhance problem-solving skills and understanding of algorithms through hands-on practice. The solutions showcase different techniques, from simple array manipulations to more complex in-place modifications.

---

## **Problems Solved**

### **1. 1089: Duplicate Zeroes**

* **Problem Description:** This problem involves duplicating every occurrence of zero in a given list and shifting the rest of the elements to the right, while ensuring the modification is done in place. The goal is to achieve the duplication without exceeding the original array's length.

---

### **2. 1480: Running Sum of 1d Array**

* **Problem Description:** The task is to compute the running sum of an array where each element at index `i` is the sum of all elements in the array from index `0` to `i`. The result should be stored in a new array, calculated in a single pass.

---

### **3. 1672: Richest Customer Wealth**

* **Problem Description:** Given an `m x n` grid representing bank accounts, where each element is the amount a customer has in a bank, return the maximum wealth any customer has. A customer's wealth is the sum of money across all their accounts.

---

### **4. 412: Fizz Buzz**

* **Problem Description:** For a given integer `n`, generate a string array where each index `i` contains:
* "Fizz" if divisible by 3,
* "Buzz" if divisible by 5,
* "FizzBuzz" if divisible by both, and
* the number itself if neither.

---

### **5. 1342: Number of Steps to Reduce a Number to Zero**
* **Problem Description:** Given an integer `num`, return the number of steps to reduce it to zero. If the number is even, divide it by 2; otherwise, subtract 1.

---

### **6. 876: Middle of the Linked List**
* **Problem Description:** Given a singly linked list, return the middle node. If there are two middle nodes, return the second one.

---

### **7. 383: Ransom Note**
* **Problem Description:** Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

> Each letter in magazine can only be used once in ransomNote.

---

### **8. 485: Max Consecutive Ones**
* **Problem Description:** Given a binary array `nums`, return the maximum number of consecutive `1`'s in the array.

---

### **9. 1295: Find Numbers with Even Number of Digits**
* **Problem Description:** Given an array `nums` of integers, return how many of them contain an even number of digits.

---

### **10. 977: Squares of a Sorted Array**
* **Problem Description:** Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

---

### **11. 88: Merge Sorted Array**
* **Problem Description:** You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

* Merge `nums1` and `nums2` into a single array sorted in **non-decreasing order.**

* The final sorted array should not be returned by the function, but instead be *stored inside* the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

---

### **12. 27: Remove Element**
* **Problem Description:** Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place.** The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

* Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:
    * Change the array nums such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
    * Return `k`.

---

### **13. 26: Remove Duplicates from Sorted Array**
* **Problem Description:** Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

* Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

    * Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
    * Return `k`.

---

### **14. 1346: Check If N and Its Double Exist**
* **Problem Description:** Given an array `arr` of integers, check if there exist two indices `i` and `j` such that :
* `i != j`
* `0 <= i, j < arr.length`
* `arr[i] == 2 * arr[j]`

---

### **15. 941: Valid Mountain Array**
* **Problem Description:** Given an array of integers `arr`, return `true` if and only if it is a valid mountain array.
* A mountain array must satisfy the following conditions:
    1. `arr.length >= 3`
    2. There exists some index `i` (0 < i < arr.length - 1) such that:
        - `arr[0] < arr[1] < ... < arr[i]`
        - `arr[i] > arr[i+1] > ... > arr[arr.length - 1]`

---

### **16. 283: Move Zeroes**
* **Problem Description:** Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.
* **Note** that you must do this in-place without making a copy of the array.

---

### **17. 905: Sort Array by Parity**
* **Problem Description:** Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.
* Return ***any array** that satisfies this condition*.

---

### **18. 1051: Height Checker**
* **Problem Description:** A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in **non-decreasing order** by height. Let this ordering be represented by the integer array `expected` where `expected[i]` is the expected height of the `ith` student in line.
* You are given an integer array `heights` representing the **current order** that the students are standing in. Each `heights[i]` is the height of the `i`th student in line (**0-indexed**).
* Return *the **number of indices** where* `heights[i] != expected[i]`.

---

### **19. 414: Third Maximum Number**
* **Problem Description:** Given an integer array `nums`, return *the **third distinct maximum** number in this array. If the third maximum does not exist, return the **maximum** number*.

---

### **20. 448: Find All Numbers Disappeared in an Array**
* **Problem Description:** Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return *an array of all the integers in the range `[1, n]` that do not appear in `nums`*.

---

### **21. 1299: Replace Elements with Greatest Element on Right Side**
* **Problem Description:** Given an array `arr`, replace every element in that array with the greatest element among the elements to its right, and replace the last element with `-1`.

---

### **22. 1991: Find the Middle Index in Array**
* **Problem Description:** Given a **0-indexed** integer array `nums`, find the **leftmost** `middleIndex` (i.e., the smallest amongst all the possible ones).

    - A `middleIndex` is an index where `nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1]`.

    - If `middleIndex == 0`, the left side sum is considered to be `0`. Similarly, if `middleIndex == nums.length - 1`, the right side sum is considered to be `0`.

    - Return *the **leftmost** `middleIndex` that satisfies the condition, or `-1` if there is no such index*.

---

### **23. 904: Fruit Into Baskets**
* **Problem Description:** You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the **type** of fruit the `ith` tree produces.
* You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
    - You only have **two** baskets, and each basket can only hold a **single type** of fruit. There is no limit on the amount of fruit each basket can hold.
    - Starting from any tree of your choice, you must pick **exactly one fruit from every** tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
    - Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
    - Given the integer array `fruits`, return *the **maximum** number of fruits you can pick*.

---

### **24. 3447: Fruit Into Baskets II**
* **Problem Description:** You are given two arrays of integers, `fruits and baskets`, each of length `n`, where `fruits[i]` represents the **quantity** of the $i^{th}$ type of fruit, and `baskets[j]` represents the capacity of the $j^{th}$ basket.

* From left to right, place the fruits according to these rules:
    - Each fruit type must be placed in the **leftmost available basket** with a capacity **greater than or equal** to the quantity of that fruit type.
    - Each basket can hold **only one** type of fruit.
    - If a fruit type **cannot be placed** in any basket, it remains **unplaced**.
    - Return the number of fruit types that remain unplaced after all possible allocations are made.

---

These problems serve as foundational exercises in array manipulation, helping to strengthen core programming skills and enhance problem-solving abilities.

---
