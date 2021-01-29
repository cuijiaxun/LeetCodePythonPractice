class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={}
        for i in range(numCourses):
            graph[i] = set()
            
        for pair in prerequisites:
            graph[pair[0]].add(pair[1])
        
        taken = []
        for i in range(numCourses):
            if len(graph[i]) == 0:
                #Courses that have no prerequisites
                taken.append(i)
                
        while taken:
            take = taken.pop()
            for key in graph.keys():
                if take in graph[key]:
                    graph[key].remove(take)
                    if len(graph[key])==0:
                        taken.append(key)
                             
        for key in graph.keys():
            if len(graph[key])>0:
                return False
        
        return True
        
