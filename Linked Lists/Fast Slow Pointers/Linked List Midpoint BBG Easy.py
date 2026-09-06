""" Linked List Midpoint
Easy
Given a singly linked list, find and return its middle node. If there are two middle nodes, return the second one.

Example 1:

Output: Node 4
Example 2:

Output: Node 4
Constraints:
The linked list contains at least one node.
The linked list contains unique values. """
from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def linked_list_midpoint(head: ListNode) -> ListNode:
    #When fast is at end, slow is at middle, regardless of odd or even nodes
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
#O(n) time O(1) space  