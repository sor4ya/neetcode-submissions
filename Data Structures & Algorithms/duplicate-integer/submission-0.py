class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # o(n) time o(n) space
        # use hashmap - counter
        # possible to just o(1) space? while maintaining o(n) time? 
        seen = set()
    
        for num in nums: 
            if num in seen:
                return True
            else:
                seen.add(num)

        return False

        


        