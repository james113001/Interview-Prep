""" Longest Substring With Unique Characters
Medium
Given a string, determine the length of its longest substring that consists only of unique characters.

Example:
Input: s = 'abcba'
Output: 3
Explanation: Substring "abc" is the longest substring of length 3 that contains unique characters ("cba" also fits this description). """
def longest_substring_with_unique_chars(s: str) -> int:
    seen = set()
    best = 0
    left = 0
    for right in range(len(s)):
        #first check if character is already in the window
        while s[right] in seen:
            #update left until duplicate is gone
            seen.remove(s[left])
            left +=1
        #add next character in window
        seen.add(s[right])
        # take cumulative best length
        best = max(best, right - left +1)
    return best
# O Complexity: O(n) where n is the length of the input string. We traverse the string once with two pointers,
# and the space complexity is O(k) where k is the size of the character set (in this case, lowercase English letters).
