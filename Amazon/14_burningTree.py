# step one we convert the tree to a graph and add parent node for each child
# we then start bfs from the the target, and increment the time by one
# remainder we start from time -1 because when we reach the last node we remove it form 
# the burning queue and it increments the time by one
# watch striver video for ref

def minTime(self, root,Target):
        #making parent dict
        p = {}
        queue = deque()
        queue.append(root)
        while (queue):
            for i in range(len(queue)):
                parent = queue.popleft()
                if parent.left:
                    p[parent.left] = parent
                    queue.append(parent.left)
                if parent.right:
                    p[parent.right] = parent
                    queue.append(parent.right)
                if parent.data == Target:
                    target = parent
        mins = -1
        seen = set()
        burning = deque()
        burning.append(target)
        while burning:
            mins += 1
            for i in range(len(burning)):
                burningnode = burning.popleft()
                if burningnode.left and burningnode.left not in seen:
                    burning.append(burningnode.left)
                    seen.add(burningnode.left)
                if burningnode.right and burningnode.right not in seen:
                    burning.append(burningnode.right)
                    seen.add(burningnode.right)
                if burningnode in p.keys() and p[burningnode] not in seen:
                    burning.append(p[burningnode])
                    seen.add(p[burningnode])
        return mins