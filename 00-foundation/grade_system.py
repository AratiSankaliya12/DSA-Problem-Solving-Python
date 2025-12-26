"""
Problem: Grade System
Difficulty: Easy
Topic: Logical Thinking

Approach:
1. Read marks
2. Check grade range
3. Print grade

Time Complexity: O(1)
Space Complexity: O(1)
"""

marks = int(input())

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")
