class Solution:
    def makeGood(self, s: str) -> str:
        
        # iterate through each char in the string
        # if the current char is equal to the lower or upper of the next remove it and the next
        # start again?
        
        def check_good(q):
            if len(q) <= 1:
                return True
            i = 0
            while i + 1 < len(q):
                if (q[i] == q[i + 1].upper() or q[i] == q[i + 1].lower()) and q[i] != q[i + 1]:
                    return False
                i += 1
            return True
        
        def goodify(q):
            i = 0
            while i + 1 < len(q):
                if (q[i] == q[i + 1].upper() or q[i] == q[i + 1].lower()) and q[i] != q[i + 1]:
                    del q[i]
                    del q[i]
                i += 1
            
    
        ls = list(s)
        
        while check_good(ls) == False:
            goodify(ls)
        

        return "".join(ls)
        