""" Triplet Sum
Medium
Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0 . The solution must not contain duplicate triplets (e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates). If no such triplets are found, return an empty array.

Each triplet can be arranged in any order, and the output can be returned in any order.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [[-3, 1, 2], [-1, 0, 1]] """

from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    # Write your code here
    sort = sorted(nums)
    n = len(nums)
    answer = []
    for i in range(n-2):
        if i >0 and sort[i]==sort[i-1]: #to avoid a duplicate triplet
            continue
        lowest= sort[i]+sort[i+1]+sort[i+2]
        if lowest > 0:
            break
        if sort[i]+sort[-1]+sort[-2]<0:
            continue

        lo, hi = i+1, n-1
        while lo < hi:
            total = sort[i] + sort[lo] + sort[hi]
            if total == 0:
                answer.append([sort[i],sort[lo],sort[hi]])
                lo+=1
                hi -=1
                while lo < hi and sort[lo] == sort[lo - 1]:
                    lo += 1
                while lo < hi and sort[hi] == sort[hi + 1]:
                    hi -= 1
            elif total>0:
                hi -=1
            else:
                lo+=1
    return answer
# O Complexity is O(n^2) where n is the length of the input array. The outer loop runs n times, and for each iteration, the inner while loop can run up to n times in the worst case. The space complexity is O(k) where k is the number of unique triplets found, as we store them in the answer list.