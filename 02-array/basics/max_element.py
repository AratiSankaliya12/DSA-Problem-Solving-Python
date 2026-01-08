"""
Problem: Find maximum element in array
Difficulty: Easy
Topic: Arrays (Basics)

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [3, 7, 2, 9, 4]
max_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num

print(max_val)
