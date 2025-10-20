# linkedlist.py
# ----------------------------
# Implements a simple singly linked list using Node objects.
# Includes methods for appending, reversing, and retrieving list values.

from typing import Any, List, Optional
from .node import Node


class LinkedList:
    """A singly linked list implementation using Node objects."""

    def __init__(self, head: Node):
        """
        Initialise a LinkedList instance.

        Args:
            head (Node): The first node (head) of the linked list.
        """
        self.head = head

    def appendNode(self, node: Node) -> None:
        """
        Append a node to the end of the linked list.

        Args:
            node (Node): The node to be appended to the list.
        """
        current = self.head
        # Traverse until the end of the list is reached
        while current.next:
            current = current.next
        current.next = node  # Attach the new node at the end

    def getList(self) -> List[Any]:
        """
        Return all values from the linked list in order as a Python list.

        Returns:
            List[Any]: A list of all node values in sequence.
        """
        output = []
        current = self.head
        # Traverse through the linked list and collect all node values
        while current:
            output.append(current.value)
            current = current.next
        return output

    def reverseList(self) -> None:
        """
        Reverse the linked list in place.

        The head of the list will point to what was previously the last node.
        """
        previous: Optional[Node] = None
        current: Optional[Node] = self.head

        # Iterate through the list, reversing the 'next' pointer of each node
        while current:
            future = current.next      # Temporarily store reference to next node
            current.next = previous    # Reverse the link
            previous = current         # Move 'previous' one step forward
            current = future           # Move 'current' one step forward

        # After the loop, 'previous' points to the new head
        self.head = previous

    def __repr__(self) -> str:
        """Return a developer-friendly string representation of the linked list."""
        return f"LinkedList({self.getList()!r})"
