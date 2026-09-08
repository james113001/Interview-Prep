""" Maximum Subarray Sum
Medium
Given an array of integers, return the sum of the subarray with the largest sum.

Example:
Input: nums = [3, 1, -6, 2, -1, 4, -9]
Output: 5
Explanation: subarray [2, -1, 4] has the largest sum of 5.

Constraints:
The input array contains at least one element. """
from typing import List

def maximum_subarray_sum(nums: List[int]) -> int:
    # Kadane's algorithm (basic DP)
    if not nums:
        return 0
    #has base case
    currentsum = best = nums[0]
    #currentsum and best depend on previous number's values of them
    for num in nums[1:]:
        #defining feature of DP - updating the current state based on previous state
        currentsum = max(num, currentsum+num)
        best = max(best, currentsum)
    return best
# O Complexity: O(n) where n is the length of the input array. The algorithm iterates through the array once,
# performing constant-time operations for each element. 
# The space complexity is O(1) since we are using a constant amount of extra space for the variables currentsum and best, 
# regardless of the input
