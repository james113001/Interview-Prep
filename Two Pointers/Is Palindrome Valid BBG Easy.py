""" Is Palindrome Valid
Easy
A palindrome is a sequence of characters that reads the same forward and backward.

Given a string, determine if it's a palindrome after removing all non-alphanumeric characters. A character is alphanumeric if it's either a letter or a number.

Example 1:
Input: s = 'a dog! a panic in a pagoda.'
Output: True
Example 2:
Input: s = 'abc123'
Output: False
Constraints:
The string may include a combination of lowercase English letters, numbers, spaces, and punctuations. """

def is_palindrome_valid(s: str) -> bool:
    # Write your code here
    l=[]
    for i in s:
        if i.isalnum():
            l.append(i) 
    lo, hi = 0, len(l) -1
    while lo<hi:
        hi-=1
        if l[lo]!=l[hi]:
            return False
        lo+=1
    return True
# O Complexity is O(n) where n is the length of the input string. We traverse the string once to filter out 
# non-alphanumeric characters and then use two pointers to check for palindrome properties. 
# The space complexity is O(n) for storing the filtered characters in a list.