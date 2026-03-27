from algs4.graph import Graph
from algs4.stack import Stack

class Cycle:
    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        self.edge_to = [-1 for _ in range(G.V)]
        self.cycle = None
        self.has_cycle = False

        for s in range(G.V):
            if not self.marked[s] and self.cycle is None:
                self.dfs(G, s, s)

    def dfs(self, G, v, u):
        self.marked[v] = True
        
        for w in G.adj[v]:
            if self.cycle is not None:
                return
                
            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(G, w, v)
            elif w != u:
                self.has_cycle = True
                self.cycle = Stack()
                x = v
                while x != w:
                    self.cycle.push(x)
                    x = self.edge_to[x]
                    
                self.cycle.push(w)
                self.cycle.push(v)