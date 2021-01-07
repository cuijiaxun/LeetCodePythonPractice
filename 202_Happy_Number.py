class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        sum = 0
        while True:
            while n > 0:
                sum += (n%10)**2
                n = n//10
            if sum == 1:
                return True
            if sum in seen:
                return False
            seen.add(sum)
            n = sum
            sum = 0
