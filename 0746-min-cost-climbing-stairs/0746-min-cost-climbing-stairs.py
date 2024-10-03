class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * (len(cost) + 1)
        
        def climb(i, cost, dp):
            if i >= len(cost):
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            oneStep = cost[i] + climb(i + 1, cost, dp)
            twoStep = cost[i] + climb(i + 2, cost, dp)
            
            dp[i] = min(oneStep, twoStep)
            
            return dp[i]
        
        return min(climb(0, cost, dp), climb(1, cost, dp))
        
        
            
        