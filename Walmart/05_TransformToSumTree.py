def toSumTree(self, root) :
    def magic(root):
        if not root:
            return 0
        
        value = root.data   
        root.data = magic(root.left) + magic(root.right)
        return value + root.data
    temp = magic(root)