""" Jump to the End
Medium
You are given an integer array in which you're originally positioned at index 0. Each number in the array represents the maximum jump distance from the current index. Determine if it's possible to reach the end of the array.

Example 1:

Input: nums = [3, 2, 0, 2, 5]
Output: True
Example 2:

Input: nums = [2, 1, 0, 3]
Output: False
Constraints:
There is at least one element in nums.
All integers in nums are non-negative integers. """
from typing import List

def jump_to_the_end(nums: List[int]) -> bool:
    # Write your code here
    farthest = 0
    for i, jump in enumerate(nums):
        #first check can we even get here
        if i > farthest:
            return False
        #if you can reach, update farthest
        farthest = max(farthest, i + jump)
    return True
# O Complexity: O(n) where n is the length of the input array. The algorithm iterates through the array once,
# performing constant-time operations for each element. O(1) space complexity since we are using a constant amount of extra space for the variables farthest and length,