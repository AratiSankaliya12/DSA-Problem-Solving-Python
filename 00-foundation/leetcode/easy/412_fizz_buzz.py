"""
LeetCode #412 - Fizz Buzz
Difficulty: Easy
Link: https://leetcode.com/problems/fizz-buzz/

Approach:
1. Iterate from 1 to n
2. Check divisibility by 3 and 5
3. Append appropriate string or number

Key Learning:
- Order of conditions matters
- Logical branching

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def fizzBuzz(self, n: int):
        result = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(i)

        return result
