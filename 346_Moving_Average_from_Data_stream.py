from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.len = 0
        self.window = deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.window) >= self.size:
            old = self.window.popleft()
            self.sum -= old
            self.len -= 1
        self.sum += val
        self.len += 1
        self.window.append(val)
        return self.sum/self.len
             
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
