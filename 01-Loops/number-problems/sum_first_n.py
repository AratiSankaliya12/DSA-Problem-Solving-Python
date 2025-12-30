"""
Problem: Sum of first N numbers
Difficulty: Easy
Topic: Loops

Approach:
1. Initialize sum = 0
2. Loop from 1 to n
3. Add each number to sum

Time Complexity: O(n)
Space Complexity: O(1)
"""

n = int(input())
total = 0

for i in range(1, n + 1):
    total += i

print(total)
