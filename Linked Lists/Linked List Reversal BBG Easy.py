""" Linked List Reversal
Easy
Reverse a singly linked list.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL"""
from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def linked_list_reversal(head: ListNode) -> ListNode:
    curr = head
    #previous node- will be setting next as previous    
    prev = None
    #reversing in-place
    while curr:
        #save next node first so you don't lose reference when overwriting next to prev
        next_node = curr.next
        curr.next = prev
        # once pointer is set, can update prev and curr
        prev = curr
        curr = next_node
    #by end curr will be None, and prev will be the last node, which is now the head of the reversed list
    return prev
#O(n) time, O(1) space