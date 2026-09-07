""" LLongest Chain of Consecutive Numbers
Medium
Find the longest chain of consecutive numbers in an*array. Two numbers are consecutive if they have a difference of 1.

Example:
Input: nums = [1, 6, 2, 5, 8, 7, 10, 3]
Output: 4
Explanation: The longest chain of consecutive numbers is 5, 6, 7, 8.
 """
from typing import List

def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    numsset = set(nums)
    best = 0
    for i in numsset:
        #starting only on beginnings of chains
        if i-1 not in numsset:
            curr = i
            length = 1
            while curr+1 in numsset:
                length+=1
                curr +=1
            best = max(best, length)
    return best