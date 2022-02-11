#firstly we store the position of the rotten oranges in a queue, 
# and the fresh in a regular list, we can use a set for better time efficency
# why do we need a deque?
# because we need to pop the rotten oranges from the queue, we cant pop the newly rotten oranges from the right
# which were appended in the same time 
# also there is no need to keep the rooten oranges in the queue, therefore we just pop them out form the right
# also this helps us know ki kab fresh oranges cant rot anymore 
# ie jab the rotten deque is empty and the fresh list is not empty


def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = []
        rotten = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.append((i,j))
                elif grid[i][j] == 2:
                    rotten.append((i,j))
                    
        mins = 0
        while fresh and rotten:
            mins += 1
            for i in range(len(rotten)):
                x,y = rotten.popleft()
                for pos in [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]:
                    if (pos) in fresh:
                        rotten.append((pos))
                        fresh.remove((pos))
                # print(fresh, rotten)    
        return mins if not fresh else -1