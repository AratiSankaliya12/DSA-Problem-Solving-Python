"""
Problem: Reverse a number
Difficulty: Easy
Topic: Loops

Approach:
1. Extract last digit using modulo
2. Build reversed number
3. Remove last digit using division

Time Complexity: O(d)
Space Complexity: O(1)
"""

n = int(input())
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print(reverse)
