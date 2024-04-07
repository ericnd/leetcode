class Solution:
    def checkValidString(self, s: str) -> bool:
                # First pass: Treat '*' as '('
        balance = 0
        for char in s:
            if char in "(*":
                balance += 1  # Treat '(' and '*' as opening brackets
            else:
                balance -= 1  # Treat ')' as closing bracket
            if balance < 0:
                return False  # More closing brackets than opening

        # If balance is 0 here, it means the string might be valid, but we need to check the other way around
        if balance == 0:
            return True

        # Second pass: Treat '*' as ')'
        balance = 0
        for char in reversed(s):
            if char in "*)":
                balance += 1  # Treat ')' and '*' as closing brackets
            else:
                balance -= 1  # Treat '(' as opening bracket
            if balance < 0:
                return False  # More opening brackets than closing

        return True
        