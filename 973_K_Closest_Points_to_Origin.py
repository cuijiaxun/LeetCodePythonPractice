class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap=[]
        i=0
        while i<len(points):
            while i<K:
                dist = -(points[i][0]**2+points[i][1]**2)
                heappush(heap, (dist, points[i]))
                i+=1
            if i<len(points):
                dist = -(points[i][0]**2+points[i][1]**2)
                if heap[0][0]<dist:
                    heappop(heap)
                    heappush(heap, (dist, points[i]))
            i+=1
        res=[]
        while heap:
            top = heappop(heap)
            res.append(top[1])
        
        return res
