"""
HackerRank - Arrays - DS
Difficulty: Easy
Link: https://www.hackerrank.com/challenges/arrays-ds/problem

Approach:
1. Use two pointers (left and right)
2. Swap elements while left < right
3. Reverse the array in-place
4. Return the reversed array

Key Learning:
- Two-pointer technique
- In-place array reversal
- Index-based manipulation

Time Complexity: O(n)
Space Complexity: O(1)
"""

def reverseArray(a):
    l = 0
    r = len(a) - 1

    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

    return a
