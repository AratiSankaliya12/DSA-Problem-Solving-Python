"""
LeetCode #231 - Power of Two
Difficulty: Easy
Link: https://leetcode.com/problems/power-of-two/

Approach:
1. If n <= 0, return False
2. Repeatedly divide n by 2 using loop
3. Check if final value becomes 1

Key Learning:
- While loop control
- Loop termination conditions

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 2 == 0:
            n //= 2

        return n == 1
