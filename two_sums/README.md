# 🔢 Two Sum Problem

The **Two Sum** problem is a classic algorithmic challenge often used in interviews and technical assessments.
It asks us to determine **which two numbers** in a given list add up to a specified target value.

This problem is explored here in **two stages**, each reflecting a different input constraint and approach:

---

## 🧩 Stage 1 — Sorted Array

### 🧠 Problem Description

Given a **sorted** list of integers `nums` and an integer `target`, find the **indices** of the two numbers that add up to `target`.

### 💡 Intuition

Because the list is already sorted, we can use a **two-pointer technique** to efficiently find the pair.

- Start with two pointers:
  - `left` at the beginning of the list
  - `right` at the end
- Move them inward based on whether their sum is less than or greater than the target.

This approach eliminates the need for nested loops or extra memory.

### ⏱️ Time Complexity

O(n) — We only pass through the array once using two pointers.
Each iteration moves one of the pointers (left or right), and no element is revisited.

### 💾 Space Complexity

O(1) — Only two extra variables (left and right) are used, regardless of input size.

---

## 🧩 Stage 2 — Unsorted Array

### 🧠 Problem Description

Given an unsorted list of integers nums and an integer target, find the indices of the two numbers that add up to target.
You may assume that exactly one solution exists and that the same element cannot be used twice.

### 💡 Intuition

Since the array isn’t sorted, the two-pointer technique no longer works efficiently.
Instead, we can use a hash map (Python Dictionary) to store each number and its index as we iterate.

At each step, we check whether the complement (target - num) already exists in the map:
    If yes → we’ve found our pair.
    If no → store the current number in the map for future reference.
    
### ⏱️ Time Complexity

O(n) — Each lookup in the hash map is O(1) on average, and we process each element exactly once.
Therefore, the total time is linear in the size of the array.

### 💾 Space Complexity

O(n) — In the worst case, all elements may be stored in the hash map before the pair is found.

---

## 🧪 Unit Testing & Continuous Integration

This repository uses unit tests (via pytest) to verify the correctness of both implementations.

### 🧰 Test Coverage

For the sorted version:

    ✅ Correct indices returned for valid inputs
    ✅ Handles edge cases (small arrays, negative numbers, duplicates)
    ✅ Returns empty list or None if no pair exists

For the unsorted version:

    ✅ Correct handling of unordered input
    ✅ Tests for repeated numbers
    ✅ Ensures only one valid pair is returned
 
### 🧱 CI Integration

The Continuous Integration (CI) pipeline runs automatically on every push and pull request using GitHub Actions.
It performs the following steps:

🧩 Set up Python and install dependencies
🧪 Run all unit tests
🧹 Check code formatting and linting
✅ Report test status directly on GitHub pull requests
