""" Next Lexicographical Sequence
Medium
Given a string of lowercase English letters, rearrange the characters to form a new string representing the next immediate sequence in lexicographical (alphabetical) order. If the given string is already last in lexicographical order among all possible arrangements, return the arrangement that's first in lexicographical order.

Example 1:
Input: s = 'abcd'
Output: 'abdc'
Explanation: "abdc" is the next sequence in lexicographical order after rearranging "abcd".

Example 2:
Input: s = 'dcba'
Output: 'abcd'
Explanation: Since "dcba" is the last sequence in lexicographical order, we return the first sequence: "abcd".

Constraints:
The string contains at least one character. 
"""
#not really a two pointer problem - better known as next-permutation,
#worth studying 4-step approach
#find pivot, find swap target, swap, reverse everything to right of pivot
def next_lexicographical_sequence(s: str) -> str:
    l = list(s)
    n = len(s)
    i=n-2
    #example bdcba -> cabbd
    #find rightmost letter that breaks descending order after it (i=0)
    while i >= 0 and l[i] >= l[i+1]:
        i-=1
    
    #already last in lexicographical order
    if i==-1:
        return ''.join(reversed(l))
    
    #find next smallest lexicographical letter to the right of i
    j = n-1
    while l[j]<= l[i]:
        j-=1
    
    #switch letters
    #example cdbba
    l[i],l[j] = l[j],l[i]

    l[i+1:] = reversed(l[i+1:])
    return ''.join(l)
# O Complexity is O(n) where n is the length of the input string. We traverse the string to find the pivot 
# and the swap target, and then reverse a portion of the string. The space complexity is O(n) as we convert 
# the string to a list for manipulation.