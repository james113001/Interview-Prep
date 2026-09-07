""" Invert Binary Tree
Easy
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
 """
from ds import TreeNode

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

#recursive solution

def invert_binary_tree(root: TreeNode) -> TreeNode:
    if root is None:
        return None
    #only runs if it has children, else returns itself
    root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(root.left)
    return root
#O(n) time, O(h) space where h is the height of the tree due to recursion stack


#iterative solution using BFS
from collections import deque

def invert_tree(root):
    if root is None:
        return None
    
    #use deque for efficient pop from left and to store nodes to visit
    queue = deque([root])
    while queue:
        
        #pop the leftmost (oldest) node from the queue, popping rightmost (newest) would be DFS instead of BFS
        node = queue.popleft()
        node.left, node.right = node.right, node.left   # swap children
        #queue now grows with the children of the current node, which will be processed in subsequent iterations
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    
    return root
#O(n) time, O(n) space where n is the number of nodes in the tree, 
# since we store all nodes in the queue at some point