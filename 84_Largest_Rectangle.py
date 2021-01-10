class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [[-1,-1]]
        
        for i in range(len(heights)):
            height = heights[i]
            if height>= stack[-1][1]:
                max_area = max(max_area, height)
            if height< stack[-1][1]:
                while height<=stack[-1][1]:
                    top = stack.pop()
                    area = (i-stack[-1][0]-1)*top[1]
                    max_area = max(area,max_area)
                    current = top
            stack.append([i,height])
        while stack[-1][0] != -1:
            top=stack.pop()
            area = top[1] *(len(heights)-1-stack[-1][0])
            max_area = max(area,max_area)
        
        return max_area
