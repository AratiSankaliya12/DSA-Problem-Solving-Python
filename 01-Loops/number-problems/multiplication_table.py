"""
Problem: Multiplication table of a number
Difficulty: Easy
Topic: Loops

Approach:
1. Read input n
2. Loop from 1 to 10
3. Print n * i

Time Complexity: O(1)
Space Complexity: O(1)
"""

n = int(input())

for i in range(1, 11):
    print(n * i)
