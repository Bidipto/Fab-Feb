def construct(self, grid):
    root = Node(True,True,None,None,None,None)
    s =set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            s.add(grid[i][j])
    if len(s) == 1:
        root.val = grid[0][0]
    else:
        root.isLeaf = False
        n = len(grid)
        root.topLeft = self.construct([nums[:n//2] for nums in grid[:n//2]])
        root.topRight = self.construct([nums[n//2:] for nums in grid[:n//2]])
        root.bottomLeft = self.construct([nums[:n//2] for nums in grid[n//2:]])
        root.bottomRight = self.construct([nums[n//2:] for nums in grid[n//2:]])
    return root