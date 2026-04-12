# Problem: 136. Single Number
# Link: https://leetcode.com/problems/single-number/
# Difficulty: Easy
# Approach: XOR - duplicates cancel out (a^a=0), single number remains
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result