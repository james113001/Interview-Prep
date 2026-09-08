""" Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters. """
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        lo, hi = 0, len(s)-1
        l= list(s)
        while lo<hi:
            if l[lo] not in vowels:
                lo+=1
                continue
            if l[hi] not in vowels:
                hi-=1
                continue
            l[lo], l[hi] = l[hi], l[lo]
            lo+=1
            hi-=1
        return ''.join(l)
# O Complexity: O(n) where n is the length of the input string. 
# We traverse the string once with two pointers, and the space complexity is O(n) as we convert 
# the string to a list for manipulation.