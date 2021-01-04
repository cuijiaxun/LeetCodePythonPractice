import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.w_sum = []
        self.sum = 0
        for i in range(len(w)):
            self.sum += w[i]
            self.w_sum.append(self.sum)

    def pickIndex(self) -> int:
        if len(self.w) ==1: return 0
        choice = random.randint(0, self.sum-1)
        index = self.binSearch(self.w_sum, choice, 0, len(self.w)-1)
        #print(choice, index)
        return index
    
    def binSearch(self, array, target, low, high):
        if low == 0:
            if array[low]> target: return 0
        if high-low <=1:
            return high
        while high-low>1:
            mid = (low+high)//2
            if array[mid]<=target:
                low = mid 
            else:
                high = mid
        return high
