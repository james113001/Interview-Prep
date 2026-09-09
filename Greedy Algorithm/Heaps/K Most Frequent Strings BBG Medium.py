""" K Most Frequent Strings
Medium
Find the k most frequently occurring strings in an array, and return them sorted by frequency in descending order. If two strings have the same frequency, sort them in lexicographical order.

Example:
Input: strs = ['go', 'coding', 'byte', 'byte', 'go', 'interview', 'go'], k = 2
Output: ['go', 'byte']
Explanation: The strings "go" and "byte" appear the most frequently, with frequencies of 3 and 2, respectively.

Constraints:
k ≤ n, where n denotes the length of the array. """
from typing import List
from collections import Counter

def k_most_frequent_strings(strs: List[str], k: int) -> List[str]:
    # need efficient counts of words
    counts = Counter(strs)
    #sort by increasing negative counts (highest f first) and lexicographical order
    ranked = sorted(counts.keys(), key = lambda x: (-counts[x],x))
    return ranked[:k]
# O Complexity: O(n log n) where n is the number of unique strings in the input array.
