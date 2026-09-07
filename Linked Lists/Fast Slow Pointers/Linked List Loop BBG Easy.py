""" Linked List Loop
Easy
Given a singly linked list, determine if it contains a cycle. A cycle occurs if a node's next pointer references an earlier node in the linked list, causing a loop.

Example:

Output: True """
from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def linked_list_loop(head: ListNode) -> bool:
    # fast moves twice as fast, and if there is a cycle,
    # should lap slow
    slow = fast = head
    #ensure fast and fast.next are not None, otherwise will get error when trying to access fast.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
#O(n) time, O(1) space