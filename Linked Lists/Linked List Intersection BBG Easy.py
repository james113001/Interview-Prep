""" Linked List Intersection
Easy
Return the node where two singly linked lists intersect. If the linked lists don't intersect, return null.

Example:

Output: Node 8
How the custom test cases work:
The input is designed to describe how the two input linked lists intersect. Here's how the skip inputs work:

skip_A: The number of nodes to skip in list A (from the head) to reach the intersection node.
skip_B: The number of nodes to skip in list B (from the head) to reach the intersection node.
For a linked list with no intersection, set skip_A and skip_B to the length of their respective linked lists, which effectively skips all nodes in each linked list. """
from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def linked_list_intersection(head_A: ListNode, head_B: ListNode) -> ListNode:
    pointerA, pointerB = head_A, head_B
    #if there is intersection, they both land on intersection node, if not, just None
    while pointerA!=pointerB:
        pointerA = pointerA.next if pointerA else head_B
        pointerB = pointerB.next if pointerB else head_A
    return pointerA
