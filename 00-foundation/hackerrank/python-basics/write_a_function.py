"""
HackerRank - Write a Function
Difficulty: Easy
Link: https://www.hackerrank.com/challenges/write-a-function/problem

Approach:
1. Check leap year conditions
2. Return True or False

Key Learning:
- Function writing
- Boolean logic
- Condition combinations

Time Complexity: O(1)
Space Complexity: O(1)
"""

def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
