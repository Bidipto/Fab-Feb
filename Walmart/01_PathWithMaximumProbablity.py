#Dijkstra's Algorithm
def maxProbability(self, n: int, edges: List[List[int]], problst: List[float], start: int, end: int) -> float:
        #building adj list
        adj = defaultdict(list)
        for (u,v), prob in zip(edges, problst):
            adj[u].append((v, prob))
            adj[v].append((u, prob))

        #res array storing all the resultant probablities   
        res = [0.0] * n
        #initializing res to 1.0
        res[start] = 1.0
        
        #minheap(maxheap bass negated) to store the nodes with the highest probablity and visiting them first
        heap = [(-res[start],start)]
        while heap:
            prob,v = heapq.heappop(heap)
            if v == end:
                return -prob
            for u,nextprob in adj.get(v, []):
                #incermneting the probablity only if we do better
                if -prob*nextprob > res[u]:
                    res[u] = -prob*nextprob
                    heapq.heappush(heap, (-res[u],u))
        return res[end]