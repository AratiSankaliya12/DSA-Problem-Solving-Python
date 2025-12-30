"""
HackerRank - Loops
Difficulty: Easy
Link: https://www.hackerrank.com/challenges/python-loops/problem

Approach:
1. Read integer n
2. Loop from 0 to n-1
3. Print square of each number

Key Learning:
- for-loop with range
- Iterative computation

Time Complexity: O(n)
Space Complexity: O(1)
"""

n = int(input())

for i in range(n):
    print(i * i)
