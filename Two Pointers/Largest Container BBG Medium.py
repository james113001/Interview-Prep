""" Largest Container
Medium
You are given an array of numbers, each representing the height of a vertical line on a graph. A container can be formed with any pair of these lines, along with the x-axis of the graph. Return the amount of water which the largest container can hold.

Example:
Example
Input: heights = [2, 7, 8, 3, 7, 6]
Output: 24 """
from typing import List

def largest_container(heights: List[int]) -> int:
    highesta = 0
    lo, hi = 0, len(heights)-1
    while lo<hi:
        a = min(heights[lo], heights[hi]) * (hi - lo)
        highesta = max(a, highesta) 
        #bring shorter walls in
        if heights[lo]<heights[hi]: 
            lo +=1
        else:
            hi -=1
    return highesta
# O Complexity is O(n) where n is the length of the input array. We use a two-pointer approach to traverse the 
# array from both ends, calculating the area at each step and updating the maximum area found. 
# The space complexity is O(1) as we are using a constant amount of extra space.