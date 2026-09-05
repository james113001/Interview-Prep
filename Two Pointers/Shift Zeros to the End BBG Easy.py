""" Shift Zeros to the End
Easy
Given an array of integers, modify the array in place to move all zeros to the end while maintaining the relative order of non-zero elements.

Example:
Input: nums = [0, 1, 0, 3, 2]
Output: [1, 3, 2, 0, 0] """
from typing import List

def shift_zeros_to_the_end(nums: List[int]) -> None:
    # Write your code here
    nonzeros = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nonzeros] = nums[i]
            nonzeros += 1
        
    for i in range(nonzeros, len(nums)):
        nums[i] = 0 
# O Complexity is O(n) where n is the length of the input array. We traverse the array twice: once to move non-zero elements and once to fill in zeros. 
# The space complexity is O(1) since we modify the array in place without using extra space.

