class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals) == 0:
            return intervals
        begin, end = intervals[0]
        res = []
        for itv in intervals:
            b,e = itv
            if b > end:
                res.append([begin, end])
                begin, end = b,e
            elif e > end:
                end = e
        res.append([begin, end])
        return res
