""" You are given an array of equal-length strings words. Assume that the length of each string is n.

Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.

For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
All the strings in words have the same difference integer array, except one. You should find that string.

Return the string in words that has different difference integer array.

 

Example 1:

Input: words = ["adc","wzy","abc"]
Output: "abc"
Explanation: 
- The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
- The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
- The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1]. 
The odd array out is [1, 1], so we return the corresponding string, "abc".
Example 2:

Input: words = ["aaa","bob","ccc","ddd"]
Output: "bob"
Explanation: All the integer arrays are [0, 0] except for "bob", which corresponds to [13, -13].
 

Constraints:

3 <= words.length <= 100
n == words[i].length
2 <= n <= 20
words[i] consists of lowercase English letters. """
#Pattern: Hash Map Grouping by Signature
# - Transform each element → canonical/normalized form (must be hashable → tuple, not list)
# - Bucket elements in a dict keyed by that form
# - Answer falls out of group sizes (singleton, majority, duplicates, etc.)

# Related: LC 49 (Group Anagrams), LC 249 (Group Shifted Strings), LC 2451 (Odd String Difference)

# Key Python tools: setdefault(key, []).append(x)  OR  collections.defaultdict(list)
class Solution:
    def oddString(self, words: List[str]) -> str:
        def difference(word: str):
            # makes tuple of difference array
            # create tuple bc it's immutable and can work as dict key. Lists can't
            return tuple(  ord(word[i+1]) - ord(word[i]) for i in range(len(word)-1)  )
        
        # dictionary of difference arrays with their words
        diffs={}
        for word in words:
            diff = difference(word)
            # this is a common pattern for grouping items by a key in Python. 
            # It creates a new list for each unique key if it doesn't exist, and appends the current 
            # word to the list for that key.
            diffs.setdefault(diff, []).append(word)
        
        for d, wordlist in diffs.items():
            if len(wordlist) == 1:
                return wordlist[0]
# O Complexity: O(n * m) where n is the number of words and m is the length of each word.