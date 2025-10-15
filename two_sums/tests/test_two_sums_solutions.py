"""
Unit Tests for Two Sum Solutions
--------------------------------
Tests both algorithmic approaches to the Two Sum problem:

1. two_pointers()  - assumes a sorted list (two-pointer technique)
2. hash_map_approach() - works with unsorted lists (hash map technique)

To run all tests:
    pytest

To run just these tests:
    pytest two_sums/tests/test_two_sums_solutions.py
"""

import pytest
from two_sums.src.two_sums_solutions import two_pointers_approach, hashmap_approach


# ============================================================
# 🧩 TESTS FOR two_pointers()  (Stage 1 — Sorted Array)
# ============================================================

def test_two_pointers_basic():
    """Test basic valid cases for the sorted array approach."""
    assert two_pointers_approach([2, 3, 4, 7, 11, 15], 10) == [1, 3]
    assert two_pointers_approach([-4, -2, 0, 4, 7], 2) == [1, 3]
    assert two_pointers_approach([1, 2, 3, 4, 5], 3) == [0, 1]
    assert two_pointers_approach([10, 20, 30, 40, 50], 70) == [1, 4]


def test_two_pointers_no_solution():
    """Test when no valid pair exists."""
    assert two_pointers_approach([1, 3, 5, 7], 100) is False


def test_two_pointers_invalid_input_type():
    """Test invalid input types (expect AssertionError)."""
    with pytest.raises(AssertionError):
        two_pointers_approach("not_a_list", 10)

    with pytest.raises(AssertionError):
        two_pointers_approach([1, 2, 3, 4], "ten")

    with pytest.raises(AssertionError):
        two_pointers_approach([1], 2)


def test_two_pointers_not_sorted():
    """Test unsorted input (should raise AssertionError)."""
    with pytest.raises(AssertionError):
        two_pointers_approach([3, 1, 4, 2], 5)


def test_two_pointers_floats():
    """Test with floating-point values."""
    with pytest.raises(AssertionError):
        two_pointers_approach([1.0, 2.5, 3.5, 4.0, 6.5], 7.5)


# ============================================================
# 🧩 TESTS FOR hash_map_approach()  (Stage 2 — Unsorted Array)
# ============================================================

def test_hash_map_basic():
    """Test basic valid cases for the hash map approach."""
    assert hashmap_approach([2, 7, 11, 15], 9) == [0, 1]
    assert hashmap_approach([-3, 1, 4, 9, 12], 9) == [0, 4]
    assert hashmap_approach([3, 3, 4, 5], 6) == [0, 1]
    assert hashmap_approach([1, 2, 4, 5], 7) == [1, 3]


def test_hash_map_no_solution():
    """Test when no valid pair exists (should return False)."""
    assert hashmap_approach([1, 2, 3, 4], 10) is False


def test_hash_map_invalid_input_type():
    """Test invalid input types (expect AssertionError)."""
    with pytest.raises(AssertionError):
        hashmap_approach("not_a_list", 10)

    with pytest.raises(AssertionError):
        hashmap_approach([1, 2, 3], "five")

    with pytest.raises(AssertionError):
        hashmap_approach([5], 10)

    with pytest.raises(AssertionError):
        hashmap_approach([1.2, 3.8, 5.5, 7.0], 9.0)


def test_hash_map_edge_cases():
    """Edge cases: duplicates, negatives, zero, and floats."""
    # Duplicates
    assert hashmap_approach([0, 4, 4, 5], 8) == [1, 2]

    # Negative numbers and zero
    assert hashmap_approach([-1, 0, 1, 2], -1) == [0, 1]
