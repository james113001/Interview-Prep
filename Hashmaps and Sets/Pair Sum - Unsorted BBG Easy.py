""" Pair Sum - Unsorted
Easy
Given an array of integers, return the indexes of any two numbers that add up to a target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example:
Input: nums = [-1, 3, 4, 2], target = 3
Output: [0, 2]
Explanation: nums[0] + nums[2] = -1 + 4 = 3

Constraints:
The same index cannot be used twice in the result. """
from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    # Write your code here
    seen={}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        seen[nums[i]]=i
    return []
# O Complexity is O(n) where n is the length of the input array. We traverse the array once, storing elements 
# in a hash map for quick lookups. The space complexity is also O(n) for the hash map storing seen numbers and their indices.