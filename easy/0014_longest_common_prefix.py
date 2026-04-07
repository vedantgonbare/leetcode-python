# Problem: 14. Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy
# Approach: Take first string as prefix, shrink it until all strings start with it
# Time Complexity: O(n * m) - n strings, m is length of shortest string
# Space Complexity: O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix