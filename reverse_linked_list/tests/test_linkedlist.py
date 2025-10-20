# test_linkedlist.py
# ----------------------------
# Unit tests for the LinkedList and Node classes using pytest.
# Each test ensures the linked list behaves as expected.

import pytest
from reverse_linked_list.src.node import Node
from reverse_linked_list.src.linkedlist import LinkedList


@pytest.fixture
def simple_linked_list():
    """
    A pytest fixture that creates a simple linked list for testing:
    '1' -> '2' -> '3' -> '4' -> '5'
    """
    n1, n2, n3, n4, n5 = Node("1"), Node("2"), Node("3"), Node("4"), Node("5")
    ll = LinkedList(n1)
    ll.appendNode(n2)
    ll.appendNode(n3)
    ll.appendNode(n4)
    ll.appendNode(n5)
    return ll


def test_node_initialisation():
    """Test that a Node stores a value and has no next node by default."""
    node = Node("test")
    assert node.value == "test"
    assert node.next is None


def test_linked_list_creation(simple_linked_list):
    """Test that the linked list initialises correctly with a given head."""
    ll = simple_linked_list
    assert ll.head.value == "1"
    assert ll.getList() == ["1", "2", "3", "4", "5"]


def test_append_node(simple_linked_list):
    """Test appending a node to the linked list."""
    ll = simple_linked_list
    new_node = Node("6")
    ll.appendNode(new_node)
    assert ll.getList() == ["1", "2", "3", "4", "5", "6"]


def test_reverse_list(simple_linked_list):
    """Test that reversing the linked list works correctly."""
    ll = simple_linked_list
    ll.reverseList()
    assert ll.getList() == ["5", "4", "3", "2", "1"]


def test_reverse_twice_returns_original(simple_linked_list):
    """Reversing the list twice should restore the original order."""
    ll = simple_linked_list
    original = ll.getList().copy()
    ll.reverseList()
    ll.reverseList()
    assert ll.getList() == original


def test_repr_methods(simple_linked_list):
    """Test the __repr__ methods for both Node and LinkedList."""
    node = Node("X")
    assert repr(node) == "Node('X')"
    ll = simple_linked_list
    assert "LinkedList" in repr(ll)
    assert all(value in repr(ll) for value in ll.getList())
