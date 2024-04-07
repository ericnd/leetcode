class Solution:
    def checkValidString(self, s: str) -> bool:
        balance = 0
        for char in s:
            if char in "(*":
                balance += 1 
            else:
                balance -= 1  
            if balance < 0:
                return False  

        if balance == 0:
            return True

        balance = 0
        for char in reversed(s):
            if char in "*)":
                balance += 1 
            else:
                balance -= 1  
            if balance < 0:
                return False 

        return True
        