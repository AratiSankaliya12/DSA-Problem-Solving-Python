"""
LeetCode #26 - Remove Duplicates from Sorted Array
Difficulty: Easy

Approach:
1. Use two pointers:
   - i → read pointer
   - k → write pointer (next unique position)
2. Traverse from index 1
3. Copy unique elements forward in-place
4. Return count of unique elements

Key Learning:
- Two-pointer technique
- In-place array modification
- Sorted array property usage

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
