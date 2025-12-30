"""
HackerRank - Print Function
Difficulty: Easy
Link: https://www.hackerrank.com/challenges/python-print/problem

Approach:
1. Read integer n
2. Loop from 1 to n
3. Print numbers without space or newline

Key Learning:
- Loop-based output formatting
- Understanding end parameter in print

Time Complexity: O(n)
Space Complexity: O(1)
"""

n = int(input())

for i in range(1, n + 1):
    print(i, end="")
