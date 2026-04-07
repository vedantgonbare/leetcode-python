# Problem: 26. Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy
# Approach: Two pointers - k tracks position for next unique element
# Time Complexity: O(n)
# Space Complexity: O(1) - in-place

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k