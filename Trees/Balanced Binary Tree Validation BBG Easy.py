""" Balanced Binary Tree Validation
Easy
Determine if a binary tree is height-balanced, meaning no node's left subtree and right subtree have a height difference greater than 1.

Example:

Output: False """
from ds import TreeNode

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

def balanced_binary_tree_validation(root: TreeNode) -> bool:
    # Write your code here
    #checking left and right depths, -1 if imbalanced
    def check(node):
        if not node:
            return 0
        #any imbalance in left, just exit with -1
        left_height = check(node.left)
        if left_height == -1:
            return -1
        right_height = check(node.right)
        if right_height == -1:
            return -1
        #difference in height > 1? imbalanced
        if abs(left_height-right_height) > 1:
            return -1
        #height of the tree - 1 to include root
        return 1 + max(left_height, right_height)
    return check(root) != -1
#O(n) time, O(h) space where h is the height of the tree due to recursion stack