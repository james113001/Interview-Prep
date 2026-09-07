""" Palindromic Linked List
Easy
Given the head of a singly linked list, determine if it's a palindrome.

Example 1:

Output: True
Example 2:

Output: False """
from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


def palindromic_linked_list(head: ListNode) -> bool:
    curr = head
    s =[]
    while curr:
        s.append(curr.val)
        curr= curr.next
    lo, hi = 0, len(s)-1
    while lo<hi:
        if s[lo]!=s[hi]:
            return False
        lo+=1
        hi-=1
    return True
# O Complexity is O(n) where n is the length of the linked list. We traverse the linked list once to store its values 
# in a list and then use two pointers to check for palindrome properties.

# O(1) space solution:§
def is_palindrome(head):
    if not head or not head.next:
        return True   # empty list or single node — trivially a palindrome

    # Step 1: find the middle using fast/slow
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: reverse the second half (starting at slow)
    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    # `prev` is now the head of the reversed second half

    # Step 3: compare first half and reversed second half
    left, right = head, prev
    while right:   # right (reversed second half) is the shorter or equal-length side
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True