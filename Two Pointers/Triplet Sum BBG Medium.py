""" Triplet Sum
Medium
Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0 . The solution must not contain duplicate triplets (e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates). If no such triplets are found, return an empty array.

Each triplet can be arranged in any order, and the output can be returned in any order.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [[-3, 1, 2], [-1, 0, 1]] """

from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    # turn into two pointer problem by sorting the array and using a for loop to iterate 
    # through the first number in the triplet, and then using two pointers to find the other 
    # two numbers that sum to zero with the first number.
    sort = sorted(nums)
    n = len(nums)
    answer = []
    # i is the first number in the triplet, lo is the second number, and hi is the third number
    for i in range(n-2):
        if i >0 and sort[i]==sort[i-1]: #to avoid a duplicate triplet
            continue

        #early stopping conditions to avoid unnecessary iterations
        lowest= sort[i]+sort[i+1]+sort[i+2]
        if lowest > 0:
            break

        highest= sort[i]+sort[-1]+sort[-2]
        if highest < 0:
            continue

        #two pointer approach 
        lo, hi = i+1, n-1
        while lo < hi:
            total = sort[i] + sort[lo] + sort[hi]
            if total == 0:
                answer.append([sort[i],sort[lo],sort[hi]])
                lo+=1
                hi -=1

                # logic again to avoid duplicates
                while lo < hi and sort[lo] == sort[lo - 1]:
                    lo += 1
                while lo < hi and sort[hi] == sort[hi + 1]:
                    hi -= 1
                # end of logic to avoid duplicates

            elif total>0:
                hi -=1
            else:
                lo+=1
    return answer
# O Complexity is O(n^2) where n is the length of the input array. 
# The outer loop runs n times, and for each iteration, the inner while loop can run up to n times 
# in the worst case. The space complexity is O(k) where k is the number of unique triplets found, 
# as we store them in the answer list.