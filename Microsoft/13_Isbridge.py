#keeping track of the visted nodes is very imp else we will keep on looping forever
#learn  dfs bfs on graphs
def isBridge(self, V, adj, c, d):
    #print(adj)
    if c != d:
        adj[c].remove(d)
        adj[d].remove(c)
    else:
        adj[c].remove(d)
        
    #print(adj)
    #start karna ha c se agar d tak pahoch gaya then its not a bridge
    #can reach = 0
    visited = set()
    def magic(root):
        if root == d:
            return 0
        res = 1
        visited.add(root)
        for i in adj[root]:
            if i not in visited:
                temp = magic(i)
                res = min(temp,res)
                #print(root, i, temp, adj)
        adj[root] = []
        visited.remove(root)
        return res
    return magic(c)