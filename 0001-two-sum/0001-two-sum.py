class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, val in enumerate(nums):
            comp = target - val
            if comp in seen:
                return [i, seen[comp]]
            seen[val] = i
        
        
            