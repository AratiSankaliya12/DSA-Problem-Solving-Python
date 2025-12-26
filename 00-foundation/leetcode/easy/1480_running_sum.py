"""
LeetCode #1480 - Running Sum of 1D Array
Difficulty: Easy
Link: https://leetcode.com/problems/running-sum-of-1d-array/

Approach:
1. Traverse the array from index 1
2. Add previous element to the current element
3. Modify the array in-place

Key Learning:
- In-place prefix sum
- Space optimization
- Loop-based cumulative logic

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
