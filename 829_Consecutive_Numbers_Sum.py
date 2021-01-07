class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 0      
        upper_limit = int(sqrt(2*N+1))
        for n in range(upper_limit):
            number = n + 1
            divide = N//number
            if number %2 == 1:
                if number * divide == N:
                    res += 1
            else:
                if number * divide + number//2 == N:
                    res += 1
        return res
