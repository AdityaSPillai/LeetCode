class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap={i:[] for i in range(numCourses)}
        visit=set()
        for c,p in prerequisites:
            hmap[c].append(p)
        
        def dfs(c):
            if c in visit:
                return False
            if hmap[c]==[]:
                return True
            
            visit.add(c)
            for p in hmap[c]:
                if not dfs(p):
                    return False
            visit.remove(c)
            hmap[c]=[]
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True