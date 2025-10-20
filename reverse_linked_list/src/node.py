# node.py
# ----------------------------
# Defines a simple Node class for use in a singly linked list.
# Each node stores a value and a reference to the next node in the sequence.

from typing import Any, Optional


class Node:
    """Represents a single element (node) in a singly linked list."""

    def __init__(self, value: Any):
        """
        Initialise a Node instance.

        Args:
            value (Any): The data value to store in the node.
        """
        self.value = value  # The actual data stored in this node
        self.next: Optional["Node"] = None  # Reference to the next node (or None if end of list)

    def __repr__(self) -> str:
        """Return a developer-friendly string representation of the node."""
        return f"Node({self.value!r})"
