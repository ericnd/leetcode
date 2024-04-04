class Solution:
    def maxDepth(self, s: str) -> int:
        nesting = 0
        max_nesting = 0

        for c in s:
            if c == '(':
                nesting += 1
            if c == ')':
                nesting -= 1
            max_nesting = max(nesting, max_nesting)
        
        return max_nesting
            

        
        

        