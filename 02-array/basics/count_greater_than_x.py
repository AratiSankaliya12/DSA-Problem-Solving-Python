"""
Problem: Count elements greater than X
Difficulty: Easy
Topic: Arrays (Basics)

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [1, 5, 7, 2, 9]
x = 4
count = 0

for num in arr:
    if num > x:
        count += 1

print(count)
