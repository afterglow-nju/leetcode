class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if i=='B' and stack[-1]=='A':
                    stack.pop()
                elif i=='D' and stack[-1]=='C':
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack)
    
    
from collections import defaultdict
# Graph class using adjacency list representation
class Graph:
    def __init__(self, V,E):
        self.V = V  # Number of vertices
        self.graph = E  # Default dictionary to store graph
    
    def dfs(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited)
    
    def find_candidate(self):
        visited = [False] * self.V
        
        # To store last finished vertex (or potential candidate)
        candidate = 0
        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited)
                candidate = i
        
        return candidate
    
    # Check if the candidate can reach all vertices
    def check_candidate(self, candidate):
        visited = [False] * self.V
        self.dfs(candidate, visited)
        return all(visited)
    
    def find_vertex(self):
        # Step 1: Find the last finished vertex (candidate)
        candidate = self.find_candidate()
        
        # Step 2: Check if this candidate can reach all other vertices
        if self.check_candidate(candidate):
            return candidate
        else:
            return -1


if __name__ == "__main__":
    #input is vertex set V and edge set E represented in adjacency list
    g = Graph(V,E)
    result = g.find_vertex()
    if result != -1:
        print(f"Vertex {result} can reach all other vertices.")
    else:
        print("No vertex can reach all other vertices.")
    