""" Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters. """
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expandfromcenter(left, right):
            while left>= 0 and right< len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        
        best = ""
        for i, _ in enumerate(s):
            odd = expandfromcenter(i, i)
            if len(odd)>len(best):
                best = odd
            even = expandfromcenter(i,i+1)
            if len(even)>len(best):
                best = even
        return best

    #O Complexity: O(n^2) where n is the length of the input string. 
    # The outer loop runs n times, and for each character, we may expand to the left and right up to n/2 times in the worst case.
    # The space complexity is O(1) since we are only using a few variables to keep track of the best palindrome found so far.