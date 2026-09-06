""" Happy Number
Medium
In number theory, a happy number is defined as a number that, when repeatedly subjected to the process of squaring its digits and summing those squares, eventually leads to 1. An unhappy number will never reach 1 during this process, and will get stuck in an infinite loop.

Given an integer, determine if it's a happy number.

Example:
Input: n = 23
Output: True
Explanation: 
2^2 + 3^2 = 13 ⇒ 
1^2 + 3^2 = 10 ⇒    
1 """
def happy_number(n: int) -> bool:
    def next_n(x):
        return sum(int(d) ** 2 for d in str(x))

# main difference in approach as a two pointer is checking for a specific value (1)
    slow, fast = n, next_n(n)
    while fast != 1 and slow != fast: 
        slow = next_n(slow)
        fast = next_n(next_n(fast))
    return fast == 1
#if n == 1:
#   return True
# slow = fast = n
# while True:
#     slow = next_n(slow)
#     fast = next_n(next_n(fast))
#     if fast == 1 or slow == fast:
#         break
# return fast == 1
#O(n) time O(1) space