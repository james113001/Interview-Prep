""" Substring Anagrams
Medium
Given two strings, s and t , both consisting of lowercase English letters, return the number of substrings in s that are anagrams of t.

An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once.

Example:
Input: s = 'caabab', t = 'aba'
Output: 2
Explanation: There is an anagram of t starting at index 1 ("caabab") and another starting at index 2 ("caabab") """
from collections import Counter
def substring_anagrams(s: str, t: str) -> int:
    length = len(s)
    interval = len(t)
    if interval> length or interval==0:
        return 0

    t_count=Counter(t)
    substring_count=Counter(s[:interval])

    count = 0
    #check if first window is anagram
    if substring_count == t_count:
        count+=1 

    for i in range(interval, length):
        substring_count[s[i]] += 1 #add right character in counter
        substring_count[s[i - interval]] -=1 #remove left character count
        #remove key (left character) if count is 0
        if substring_count[s[i-interval]] == 0:
            del substring_count[s[i-interval]] 


        if substring_count == t_count:
            count +=1
    return count