class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 不能有回路
        g=defaultdict(list)
        visit=[False] * numCourses
        has=[False] * numCourses
        def build_graph(edge):
            for i in edge:
                g[i[0]].append(i[1])

        parent=set()
        def dfs(node):
            
            visit[node]=True 
            parent.add(node)
            for i in g[node]:
                if not visit[i]:
                    if not dfs(i):
                        return False
                elif i in parent:
                    return False
            parent.remove(node) 
            return True

            
        build_graph(prerequisites)
        
        for i in range(numCourses):
            if not visit[i]:
                if not dfs(i):
                    #print(i)
                    return False
        return True
                