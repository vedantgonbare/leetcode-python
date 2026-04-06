# Problem: 9. Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy
# Approach: Convert to string, check if it equals its reverse
# Time Complexity: O(n) - n is number of digits
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]