"""
Problem: Count even numbers from 1 to N
Difficulty: Easy
Topic: Loops

Approach:
1. Initialize counter
2. Loop from 1 to n
3. Check even condition
4. Increment counter

Time Complexity: O(n)
Space Complexity: O(1)
"""

n = int(input())
count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        count += 1

print(count)
