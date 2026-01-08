"""
LeetCode #1920 - Build Array from Permutation
Difficulty: Easy

Approach:
1. For each index i, place nums[nums[i]] into a new array
2. Return the constructed array

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            ans.append(nums[nums[i]])

        return ans
