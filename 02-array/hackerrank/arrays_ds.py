"""
HackerRank - Arrays - DS
Difficulty: Easy
Link: https://www.hackerrank.com/challenges/arrays-ds/problem

Time Complexity: O(n)
Space Complexity: O(1)
"""

n = int(input())
arr = list(map(int, input().split()))

print(*arr[::-1])
