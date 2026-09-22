class UnionFind:
    def __init__(self,n):
        self.id = list(range(n))
    
    def find(self,u):
        if self.id[u] == u:
            return u
        return self.find(self.id[u])
    
    def union(self,u,v):
        parent_v = self.find(v)
        parent_u = self.find(u)
        if parent_v!=parent_u:
            self.id[parent_v]=parent_u
            return True
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for u,v in edges:
            if not uf.union(u-1,v-1):
                return [u,v]