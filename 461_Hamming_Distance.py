class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        Dh = 0
        while x!=0 or y!=0:
            if x%2 != y%2:
                Dh +=1
            x = x//2
            y = y//2
        
        return Dh
