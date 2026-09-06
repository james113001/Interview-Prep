""" Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters. """

class Solution:
    def firstUniqChar(self, s: str) -> int:
        #first pass to get counts of each character
        counts={}
        for char in s:
            #get returns the value for the key if it exists, otherwise 0
            counts[char] = counts.get(char, 0) +1

        #first index where count is 1
        for i, char in enumerate(s):
            if counts[char] == 1:
                return i
        return -1
# O Complexity: O(n) where n is the length of the input string.