class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        # Sort scores in descending order
        sorted_scores = sorted(score, reverse=True)
        
        # Store rank of each score
        rank_map = {}
        
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)
        
        # Build answer using original order
        answer = []
        
        for s in score:
            answer.append(rank_map[s])
        
        return answer