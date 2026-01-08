"""
LeetCode #1929 - Concatenation of Array
Difficulty: Easy

Approach:
1. Concatenate array with itself
2. Return the new array

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
