from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max((count[n] + count[n+1] for n in count if n+1 in count), default=0)