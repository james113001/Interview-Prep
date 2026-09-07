""" Cutting Wood
Medium
You are given an array representing the heights of trees, and an integer k representing the total length of wood that needs to be cut.

For this task, a woodcutting machine is set to a certain height, H . The machine cuts off the top part of all trees taller than H, while trees shorter than H remain untouched. Determine the highest possible setting of the woodcutter (H) so that it cuts at least k meters of wood.

Assume the woodcutter cannot be set higher than the height of the tallest tree in the array.

Example:

Input: heights = [2, 6, 3, 8], k = 7
Output: 3
Explanation: The highest possible height setting that yields at least k = 7 meters of wood is 3, which yields 8 meters of wood. Any height setting higher than this will yield less than 7 meters of wood.

Constraints:
It's always possible to attain at least k meters of wood.
There's at least one tree. """
from typing import List

def cutting_wood(heights: List[int], k: int) -> int:
    #binary search on answer
    def findwoodresult(h: int):
        total = 0
        for i in heights:
            if i<=h:
                continue
            else:
                total += i-h
        return total

    #possible h values
    lo, hi = 0, max(heights)
    result = 0
    while lo<=hi:
        mid = (lo+hi)//2
        #might not be able to get exactly k, so >=, not ==
        if findwoodresult(mid) >= k:
            result = mid
            #want to search higher
            lo= mid + 1
        #not enough wood cut, then lower h
        elif findwoodresult(mid) < k:
            hi= mid - 1

        else:
            lo= mid + 1
    return result
# O Complexity: O(n log m) where n is the number of trees and m is the maximum height of the trees. 
# The binary search runs in log m time, and for each mid value, we iterate through the heights array 
# to calculate the total wood cut, which takes O(n) time. 
# The space complexity is O(1) since we are using a constant amount of extra space for variables.