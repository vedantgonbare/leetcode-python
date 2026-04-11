# Problem: 118. Pascal's Triangle
# Link: https://leetcode.com/problems/pascals-triangle/
# Difficulty: Easy
# Approach: Build each row using sum of two elements from previous row
# Time Complexity: O(n^2)
# Space Complexity: O(n^2) - storing all rows

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        
        for i in range(1, numRows):
            prev = triangle[i-1]
            row = [1]
            for j in range(1, i):
                row.append(prev[j-1] + prev[j])
            row.append(1)
            triangle.append(row)
        
        return triangle