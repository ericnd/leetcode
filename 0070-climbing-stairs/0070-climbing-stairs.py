class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        
        def climb(s):
            if s in dp:
                return dp[s]

            if s <= 3:
                return s
            
            dp[s] = climb(s - 1) + climb(s - 2)
            return climb(s - 1) + climb(s - 2)
        
        return climb(n)