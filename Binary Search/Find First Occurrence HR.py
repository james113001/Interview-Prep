""" Given a sorted array of integers that may contain duplicates, return the index of the first occurrence of a target value or -1 if not found.

Example

Input:

nums = [1, 2, 3, 4, 5]
target = 3
Output:

2
Explanation:

We perform binary search on [1,2,3,4,5].

low=0, high=4 → mid=2 → nums[2]=3 equals target. Record result=2, then search left half.
Update high=mid-1=1. Now low=0, high=1 → mid=0 → nums[0]=1 < target, so move low to mid+1=1.
low=1, high=1 → mid=1 → nums[1]=2 < target, so move low to mid+1=2.
Now low(2)>high(1), terminate. The first occurrence found is at index 2.

Input Format

The input consists of two lines.

First line: two space-separated integers n and target, where 0 <= n <= 1000 and -10^9 <= target <= 10^9.

Second line: n space-separated integers nums[i], each satisfying -10^9 <= nums[i] <= 10^9, and nums is sorted in non-decreasing order.

Edge cases include: n = 0 (empty array), all elements less than target, all elements greater than target, multiple duplicates of target, single-element array.

Constraints

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9 for all 0 <= i < nums.length
-10^9 <= target <= 10^9
For all 0 <= i < nums.length - 1, nums[i] <= nums[i+1] (array is non-decreasingly sorted)
Output Format

Output a single integer: the index (0-based) of the first occurrence of target in the array nums. If target does not exist in nums, output -1.

Sample Input 0

0, 5
Sample Output 0

-1
Sample Input 1

1, 3, 3
Sample Output 1

0 """
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findFirstOccurrence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#
from bisect import bisect_left
from typing import List

def find_the_insertion_index(nums: List[int], target: int) -> int:
    return bisect_left(nums, target)
# O Complexity: O(log n)

# manual binary search version:
# def findFirstOccurrence(nums, target):
#     lo, hi = 0, len(nums)-1
#     result = -1
#     while lo<=hi:
#         mid = (lo+hi)//2
#         if nums[mid] == target:
#             result = mid #keep iterating to find leftmost occurrence

#         if nums[mid] < target:
#             lo = mid+1
#         else:
#             hi = mid-1

#     return result

#O Complexity: O(log n) where n is the length of the input array. 
# We perform binary search on the sorted array, which has a logarithmic time complexity. 
# The space complexity is O(1) since we use a constant amount of extra space for variables.

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = findFirstOccurrence(nums, target)

    print(result)
