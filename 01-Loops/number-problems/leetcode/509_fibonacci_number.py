"""
LeetCode #509 - Fibonacci Number
Difficulty: Easy
Link: https://leetcode.com/problems/fibonacci-number/

Approach:
1. Handle base cases (0 and 1)
2. Use loop to build Fibonacci iteratively
3. Update previous two values

Key Learning:
- Iterative DP thinking
- Loop-based state update

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b

        return b
