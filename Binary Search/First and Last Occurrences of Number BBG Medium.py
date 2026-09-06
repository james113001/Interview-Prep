""" First and Last Occurrences of a Number
Medium
Given an array of integers sorted in non-decreasing order, return the first and last indexes of a target number. If the target is not found, return [-1, -1] .

Example 1:
Input: nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11],
       target = 4
Output: [3, 5]
Explanation: The first and last occurrences of number 4 are indexes 3 and 5, respectively. """
from typing import List

def first_and_last_occurrences_of_a_number(nums: List[int], target: int) -> int:
    #binary search twice, once for each side
    def findboundary(nums: List[int], target: int, findfirst: bool):
        lo, hi = 0, len(nums)-1
        result = -1
        while lo<=hi:
            mid = (lo +hi)//2
            if nums[mid]==target:
                result = mid
                if findfirst:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid]<target:
                lo = mid + 1
            else:
                hi= mid - 1
        return result
    
    first = findboundary(nums, target, True)
    if first == -1:
        return [-1,-1]
    last = findboundary(nums, target, False)
    return [first, last]
# O Complexity: O(log n) 
