""" Find the Insertion Index
Easy
You are given a sorted array that contains unique values, along with an integer target.

If the array contains the target value, return its index.
Otherwise, return the insertion index. This is the index where the target would be if it were inserted in order, maintaining the sorted sequence of the array.
Example 1:
Input: nums = [1, 2, 4, 5, 7, 8, 9], target = 4
Output: 2
Example 2:
Input: nums = [1, 2, 4, 5, 7, 8, 9], target = 6
Output: 4
Explanation: 6 would be inserted at index 4 to be positioned between 5 and 7: [1, 2, 4, 5, 6, 7, 8, 9]. """
from typing import List

def find_the_insertion_index(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums)-1
    while lo<=hi:
        mid = (lo + hi) //2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            lo = mid + 1
        else:
            hi = mid -1
    # lo is the lowest possible index where value can go, hi is 
    # now lower than lo
    return lo 
#O Complexity: O(log n) 