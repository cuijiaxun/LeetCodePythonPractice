class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = 0
        l,r = 0,0
        running_sum = 0
        while r <len(nums):
            running_sum += nums[r]
            while l <= r and running_sum >= s:
                running_sum -= nums[l]
                if res == 0:
                    res = r-l+1
                else:
                    res = min(res,r-l+1)
                l+=1
            r+=1
        return res

