class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        placeIdx = 0
        for num in nums:
            if num != 0:
                nums[placeIdx] = num
                placeIdx += 1
        
        for i in range(placeIdx, len(nums)):
            nums[i] = 0
