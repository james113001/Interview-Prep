""" Triangle Numbers
Medium
Consider a triangle composed of numbers where the top of the triangle is 1. Each subsequent number in the triangle is equal to the sum of three numbers above it: its top-left number, its top number, and its top-right number. If any of these three numbers don't exist, assume they are equal to 0.

Given a value representing a row of this triangle, return the position of the first even number in this row. Assume that the first number in each row is at position 1.

Example:

Input: n = 4
Output: 3
Constraints:
n will be at least 3. """

def triangle_numbers(n: int) -> int:
    # Write your code here
    if n == 1:
        return None
    if n %2 != 0:
        return 2
    if (n-1)%4 == 1:
        return 4 if n >=6 else None
    if (n-1)%4 == 3:
        return 3

# o
# ooo 2---
# oeoeo3
# ooeoeoo4---
# oeeeoeeeo5
# oooe 6--- repeats pattern from row 2

#O Complexity: O(1) since we are using a mathematical approach to determine the position of the first even number 
# in the triangle row without generating the entire triangle. The space complexity is also O(1) as we are not 
# using any additional data structures.

