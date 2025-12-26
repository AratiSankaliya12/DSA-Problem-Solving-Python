"""
HackerRank - Python If-Else
Difficulty: Easy
Link: https://www.hackerrank.com/challenges/py-if-else/problem

Approach:
1. Read integer input
2. Apply conditional rules
3. Print appropriate output

Key Learning:
- Conditional branching
- Order of conditions

Time Complexity: O(1)
Space Complexity: O(1)
"""

n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
