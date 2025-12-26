"""
Problem: Positive, Negative or Zero
Difficulty: Easy
Topic: Logical Thinking

Approach:
1. Read number
2. Compare with zero
3. Print result

Time Complexity: O(1)
Space Complexity: O(1)
"""

n = int(input())

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
