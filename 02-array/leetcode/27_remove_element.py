"""
LeetCode #27 - Remove Element
Difficulty: Easy

Approach:
1. Traverse array
2. Copy non-target elements forward
3. Return new length

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0

        for num in nums:
            if num != val:
                nums[index] = num
                index += 1

        return index
