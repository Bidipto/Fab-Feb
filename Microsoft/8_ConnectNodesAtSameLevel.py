def connect(self, root):
        #level order traversal
        queue = deque([root])
        connection = deque()
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                # print(node.left, i)
                if node.left:
                    queue.append(node.left)
                    connection.append(node.left)
                if node.right:
                    queue.append(node.right)
                    connection.append(node.right)
            if connection:
                temp = connection.popleft()
                while connection:
                    rnext = connection.popleft()
                    temp.nextRight = rnext
                    temp = temp.nextRight