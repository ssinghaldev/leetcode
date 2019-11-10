class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Writing Boyer-Moore algorithm
        count = 0
        ele = None
        
        for num in nums:
            if count == 0:
                ele = num
                count += 1
            elif ele != num:
                count -= 1
            elif ele == num:
                count += 1
            
        
        return ele
