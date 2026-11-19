"""
LeetCode 150: Evaluate Reverse Polish Notation
Companies: Amazon, Google, LinkedIn, Microsoft, Uber
Time Complexity: O(N) - Each token is processed once in O(1) time.
Space Complexity: O(N) - Stack holds operand integers during evaluation.
Intuition: Push numbers onto a stack; when an operator (`+`, `-`, `*`, `/`) appears, pop the top two operands, apply the operator, and push the result back.
Why Efficient: Postfix notation eliminates parentheses and operator precedence rules, allowing single-pass evaluation with a stack in O(N) time.
"""
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]
