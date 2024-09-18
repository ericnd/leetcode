class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
                
        for each in freq:
            if freq[each] > 1:
                return True
        
        return False