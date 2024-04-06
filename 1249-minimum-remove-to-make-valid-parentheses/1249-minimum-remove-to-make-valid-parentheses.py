class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = list(s)
        q = deque()
        for i, c in enumerate(res):
            if c == "(":
                q.append(i)
            elif c == ")":
                if q:
                    q.pop()
                else:
                    res[i] = ''
        while q:
            res[q.pop()] = ''

        return "".join(res)
            
                
        
            
        