# Problem: 108. Convert Sorted Array to Binary Search Tree
# Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Difficulty: Easy
# Approach: Recursion - pick middle as root, recurse on left and right halves
# Time Complexity: O(n)
# Space Complexity: O(log n) - recursion call stack

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root