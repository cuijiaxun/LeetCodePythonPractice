class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """Solution 1"""
        #24ms, 13.4mb
        num1 = nums
        num2 = {}
        for i in range(len(num1)):
            current = target - num1[i]

            if num1[i] in num2.keys():
                index_1 = i
                index_2 = num2[num1[i]].pop()
                break
                
            if current not in num2.keys():
                num2[current] = i

        return [index_1,index_2]
        """Solution2
        #36ms, 13.6mb
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
        """
