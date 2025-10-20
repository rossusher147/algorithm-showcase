# 🔁 Reversing a Singly Linked List in Python

This project implements the algorithm to **reverse a singly linked list**. A classic problem in computer science that tests one’s understanding of **pointers**, **iteration**, and **in-place data manipulation**.  
The solution is written in clean, well-documented Python, and includes comprehensive unit tests using `pytest`.

---

## 🧩 Problem Statement

The challenge is simple to state but conceptually tricky:

> **Given a singly linked list, reverse the order of its nodes _in place_ without using any extra data structures.**

That means:
- You must not create a new list or array.
- You can only manipulate the existing `next` pointers between nodes.
- The solution should work in **O(n)** time and **O(1)** extra space.

---

## 🧠 What Is a Linked List?

A **linked list** is a linear data structure where each element (called a *node*) contains:
- A value (the stored data)
- A reference (or pointer) to the **next node** in the sequence

Unlike Python lists (which use contiguous memory), linked lists store elements in separate memory locations connected by pointers.  
This makes **insertions and deletions** efficient, but **traversal** requires following the chain of references.

Example structure:

[1] → [2] → [3] → [4] → [5] → None

Reversing this list should yield:

[5] → [4] → [3] → [2] → [1] → None

---

## ⚙️ The Challenge

Reversing a linked list means you must **re-wire all the `next` pointers** so that each node points to its previous node, rather than its next one.

**The main challenge:**

You must keep track of **three pointers** during the process:
  1. `previous` - the node that comes before the current one (initially `None`)
  2. `current` - the node currently being processed
  3. `future` - the node that comes after the current one (so you don’t lose the rest of the list)

If you forget to store the `future` node before reassigning `current.next`, you lose access to the rest of the list!

---

## 💡 Solution Overview

This project contains two classes:

### 1. `Node`
A simple class representing a single node:
- Holds a `value`
- Points to the `next` node (or `None` if it’s the end)

### 2. `LinkedList`
Manages a collection of connected nodes, supporting:
- `appendNode(node)`: add a node to the end of the list
- `getList()`: return all values in list form
- `reverseList()`: reverse the linked list **in place**

### 🔄 Reversal Algorithm (Iterative)

The core algorithm uses three pointers:

```python
def reverseList(self):
    previous = None
    current = self.head

    while current:
        future = current.next      # Save reference to next node
        current.next = previous    # Reverse pointer direction
        previous = current         # Move previous one step forward
        current = future           # Move current one step forward

    self.head = previous
```

## Complexity Analysis

| Operation       | Time Complexity | Space Complexity | Explanation                          |
| --------------- | --------------- | ---------------- | ------------------------------------ |
| `appendNode()`  | O(n)            | O(1)             | Must traverse to end to append       |
| `getList()`     | O(n)            | O(n)             | Collects all values in a Python list |
| `reverseList()` | **O(n)**        | **O(1)**         | Reverses pointers once per node      |

---

## 🧪 Testing

Unit tests are written using pytest and can be found in the tests/ directory.
They cover:
- Node initialisation
- List creation and appending
- Reversal correctness
- Double reversal returning the original list
- `__repr__` method consistency