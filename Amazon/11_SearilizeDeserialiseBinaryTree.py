#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/submissions/

#the idea is to convert a tree to a list and then convert the list to a tree
#comma seperated string is used to seperate the values in the list, but a list can also be used
#pre order dfs use kiya ha lekin level order traversal aslo works just fine, great work me


class Codec:

    def serialize(self, root):
        res = []
        def magic(root):
            if not root:
                res.append("N")
            else:
                res.append(str(root.val))
                magic(root.left)
                magic(root.right)
                
        magic(root)
        return ",".join(res)

    def deserialize(self, data):
        nums = data.split(',')
        self.i = 0
        def magic():
            if nums[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(nums[self.i]))
            self.i += 1
            node.left = magic()
            node.right = magic()
            return node
        return magic()