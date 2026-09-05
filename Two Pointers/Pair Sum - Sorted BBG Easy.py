""" Pair Sum - Sorted
Easy
Given an array of integers sorted in ascending order and a target value, return the indexes of any pair of numbers in the array that sum to the target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example 1:
Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]
Explanation: nums[2] + nums[3] = 3 + 4 = 7

Example 2:
Input: nums = [1, 1, 1], target = 2
Output: [0, 1]
Explanation: other valid outputs could be [1, 0], [0, 2], [2, 0], [1, 2] or [2, 1].
 """
from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    # Write your code here
    lo,hi = 0, len(nums) -1
    while lo<hi:
        addition = nums[lo] + nums[hi]
        if target == addition:
            return [lo,hi]
        elif target > addition:
            lo += 1
        else:
            hi -= 1
    return []
# O Complexity is O(n) where n is the length of the input array. In the worst case, we may need to traverse the entire array with two pointers. 
#   The space complexity is O(1) since we are using a constant amount of extra space for the pointers and variables.