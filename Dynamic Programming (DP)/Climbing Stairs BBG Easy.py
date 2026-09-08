""" Climbing Stairs
Easy
Determine the number of distinct ways to climb a staircase of n steps by taking either 1 or 2 steps at a time.

Example:

Input: n = 4
Output: 5 """
from functools import lru_cache

#cache hashable arguments to avoid recomputation of the same subproblems, O(n) time and O(n) space
@lru_cache(maxsize=None)
def climbing_stairs(n: int) -> int:
    # 1 way to climb 1 stair, 2 ways to climb 2 stairs (1+1 or 2)
    if n <= 2:
        return n
    return climbing_stairs(n-1) + climbing_stairs(n-2)


#no recursion, O(n) time and O(1) space
def climbing_stairs(n):
    if n <= 2:
        return n
    ways_back2, ways_back1 = 1, 2

    #to n+1 so that the last iteration is for n, and ways_back1 will be the answer
    for _ in range(3, n + 1):
         #for any given position, you want to know how many steps it takes to get to one step before or two (bc each j needs one more step which is part of the same way)
        #if you're two back, then you can take one step forward to get to one back, hence ways_back2+ways_back1 ends up ways_back1
        #this is to update for the next step position, so ways_back1 will become ways_back2
        ways_back2, ways_back1 = ways_back1, ways_back2 + ways_back1
    return ways_back1