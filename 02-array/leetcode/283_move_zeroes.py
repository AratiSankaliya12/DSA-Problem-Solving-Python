"""
LeetCode #283 - Move Zeroes
Difficulty: Easy

Approach:
1. Use two pointers:
   - i → write pointer (position for next non-zero)
   - j → read pointer (iterate through array)
2. When a non-zero element is found, swap it with position i
3. Increment write pointer

Key Learning:
- Two-pointer technique
- In-place array modification
- Maintaining relative order of elements

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
      
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
