"""
LeetCode #1480 - Running Sum of 1D Array
Difficulty: Easy

Approach:
1. Traverse array from index 1
2. Add previous element to current element
3. Modify array in-place

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
