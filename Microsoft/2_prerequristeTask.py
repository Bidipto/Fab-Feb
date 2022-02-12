N = 4
prerequisites = [[1,0],[0,1],[2,1],[3,2]]

def isPossible(N,prerequisites):
    # creating a adj list, with a dict
    adj = { i:[] for i in range(N) }
    for task, pre in prerequisites:
        adj[pre].append(task)
    print(adj)
    # creating a visited set to keep track of visited nodes in the current dfs
    visited = set()

    def magic(curr):
        # if we have already visited the node, then we get a cycle therefore its not possible
        if curr in visited:
            return False
        # if the list is empty, therefore therefore there is no prerequisites for the current task or 
        # we have already visited the node, then we can return true
        if not adj[curr]:
            return True
        visited.add(curr)
        # DFS on all the prerequisites of the current task
        for i in adj[curr]:
            # returning false if a cycle is detected
            if not magic(i):
                return False
        visited.remove(curr)
        #since no cycle is detected, we can return true and 
        # set the prerequisites of the current task to a empty list
        #indicating that the current task is completed and is possible
        adj[curr] = []
        return True

    for i in adj.keys():
        if not magic(i):
            return False
    return True

print(isPossible(N,prerequisites))