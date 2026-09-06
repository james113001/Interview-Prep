""" Remove the Kth Last Node From a Linked List
Medium
Return the head of a singly linked list after removing the kth node from the end of it.

Example:
Input: head = [1,2,3,4,5], k = 2
Output: [1,2,3,5]

Constraints:
The linked list contains at least one node. """
from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def remove_kth_last_node(head: ListNode, k: int) -> ListNode:
    # for edge case if removing head
    # two linked lists (dummy, and the original head)- dummy points to original head, and then we use lag (referencing original node) to skip over deletion
    dummy = ListNode(0, head) 
    lag, lead = dummy, dummy
    #set k+1 distance between lag and lead
    for _ in range(k+1):
        #if k larger than length of list
        if lead is None:
            return head
        lead = lead.next
    
    while lead:
        lag = lag.next
        lead = lead.next
    # lag is now at node before deletion
    lag.next = lag.next.next
    return dummy.next
# O Complexity: O(n) where n is the length of the linked list. We traverse the linked list once with two pointers, 
# and the space complexity is O(1) since we use a constant amount of extra space for variables.