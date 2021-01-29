class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = {}
        for n in nums:
            visited[n] = False
        return self.permutation(len(nums), [], nums,res,visited)  
    
    def permutation (self,len_nums, middle, nums, res, visited):
        if len(middle) == len_nums:
            res.append(deepcopy(middle))
            middle = []
            return res
        for num in nums:
            if not visited[num]:
                visited[num] = True
                middle.append(num)
                self.permutation(len_nums, middle, nums, res, visited)
                middle.pop()
                visited[num] = False
        
        return res
