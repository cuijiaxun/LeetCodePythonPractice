class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for i in range(len(nums))]
        right = [1 for i in range(len(nums))]
        end = len(nums)-1
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
            right[end-i] = right[end-i+1]*nums[end-i+1]
        res = []
        for i in range(len(nums)):
            res.append(left[i]*right[i])
        
        return res
