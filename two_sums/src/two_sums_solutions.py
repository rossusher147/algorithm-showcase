def two_pointers_approach(nums: list[int], target: int) -> list[int] | bool:
    """
    Two Sum (Sorted Array) — Two Pointer Technique
    ----------------------------------------------
    Given a sorted list of integers and a target sum, return the indices of
    the two numbers that add up to the target.

    Args:
        nums (list[int]): A sorted list of integers.
        target (int): The target sum value.

    Returns:
        list[int] | bool: A list of two indices if a valid pair is found,
                          otherwise False.

    Raises:
        AssertionError: If the inputs are invalid or the list is not sorted.

    Example:
        >>> two_pointers([2, 3, 4, 7, 11, 15], 9)
        [1, 3]
    """

    # -----------------------------------------------------------
    # Input Validation
    # -----------------------------------------------------------

    # Ensure input is a list of integers
    assert isinstance(nums, list), "Input must be a list."
    assert all(isinstance(x, int) for x in nums), "All elements must be an integer."

    # Ensure the list has at least two elements
    assert len(nums) >= 2, "List must contain at least two elements."

    # Ensure target is a number
    assert isinstance(target, int), "Target must be an integer."

    # Ensure the list is sorted in non-decreasing order
    assert all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)), "Input list must be sorted."

    # -----------------------------------------------------------
    # Algorithm Implementation (Two Pointers)
    # -----------------------------------------------------------

    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        # Found the correct pair
        if current_sum == target:
            return [left, right]

        # If sum too large, move right pointer left
        elif current_sum > target:
            right -= 1

        # If sum too small, move left pointer right
        else:
            left += 1

    # No valid pair found
    return False



def hashmap_approach(nums: list[int], target: int) -> list[int] | bool:
    """
    Two Sum (Unsorted Array) — Hash Map Approach
    --------------------------------------------
    Given an unsorted list of integers and a target sum, return the indices
    of the two numbers that add up to the target.

    This approach uses a hash map (dictionary) to achieve O(n) time and space complexity
    by storing previously seen numbers and their indices.

    Args:
        nums (list[int]): An unsorted list of integers.
        target (int): The target sum value.

    Returns:
        list[int] | bool: A list containing the two indices if a valid pair
                          is found, otherwise False.

    Raises:
        AssertionError: If inputs are invalid or incorrectly formatted.

    Example:
        >>> hash_map_approach([2, 7, 11, 15], 9)
        [0, 1]
    """

    # -----------------------------------------------------------
    # Input Validation
    # -----------------------------------------------------------

    # Ensure input is a list
    assert isinstance(nums, list), "Input must be a list."

    # Ensure all elements are numeric
    assert all(isinstance(x, int) for x in nums), "All elements must be an integer."

    # Ensure at least two numbers are present
    assert len(nums) >= 2, "List must contain at least two elements."

    # Ensure target is numeric
    assert isinstance(target, int), "Target must be an integer."

    # -----------------------------------------------------------
    # Algorithm Implementation (Hash Map)
    # -----------------------------------------------------------

    hashmap = {}  # Stores each number and its index

    for i, num in enumerate(nums):
        complement = target - num

        # If the complement has already been seen, return both indices
        if complement in hashmap:
            return [hashmap[complement], i]

        # Otherwise, store the current number and its index
        hashmap[num] = i

    # No valid pair found
    return False
