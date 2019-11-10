class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 1:
            return [[nums[0]]]
        
        ans = []
        for i in range(len(nums)):
            for l in self.permute(nums[:i] + nums[i+1:]):
                l.insert(0, nums[i])
                ans.append(l)
        return ans
        
