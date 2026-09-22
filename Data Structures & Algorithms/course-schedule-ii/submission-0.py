class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = {i:[] for i in range(numCourses)}
        indegree = [0]*numCourses
        count = 0 
        queue = []
        res = []

        for (u,v) in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        
        
        for i in range(numCourses):
            if indegree[i] == 0:
                res.append(i)
                queue.append(i)

        while queue:
            temp = queue.pop(0)
            count+=1
            for neighbor in graph[temp]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    res.append(neighbor)
                    queue.append(neighbor)
        
        if count == numCourses:
            return res
        return []
        