""" Valid Parenthesis Expression
Easy
Given a string representing an expression of parentheses containing the characters '(', ')', '[', ']', '{', or '}', determine if the expression forms a valid sequence of parentheses.

A sequence of parentheses is valid if every opening parenthesis has a corresponding closing parenthesis, and no closing parenthesis appears before its matching opening parenthesis.

Example 1:
Input: s = '([]{})'
Output: True
Example 2:
Input: s = '([]{)}'
Output: False
Explanation: The '(' parenthesis is closed before its nested '{' parenthesis is closed. """
def valid_parenthesis_expression(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    opening_brackets = set(pairs.values())   # to make lookup faster 

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in pairs:
            # if stack is empty or the top of the stack does not match the corresponding opening bracket, return False
            if not stack or stack[-1]!= pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0
# O Complexity: O(n) where n is the length of the input string.