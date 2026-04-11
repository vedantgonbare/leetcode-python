# Problem: 119. Pascal's Triangle II
# Link: https://leetcode.com/problems/pascals-triangle-ii/
# Difficulty: Easy
# Approach: Single row, update in-place right to left to avoid overwriting
# Time Complexity: O(n^2)
# Space Complexity: O(n) - only store one row

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        
        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j-1]
            row.append(1)
        
        return row