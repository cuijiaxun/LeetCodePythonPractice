class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) ==0: return 0
        suffix = nums[0]
        max_suffix = suffix
        for i in range(1, len(nums)):
            suffix = max(nums[i], suffix+nums[i])
            max_suffix = max(max_suffix, suffix)
        return max_suffix
