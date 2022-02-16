#simple dfs solution
#track of the number of subtree with given sum

def countSubtreesWithSumX(root, x):
    res = [0]
    def magic(root):
        if not root: return 0
        val = magic(root.left) + root.data + magic(root.right)
        if val == x:
            res[0] += 1
        return val
    magic(root)
    return res[0]

#leetcode variation 
#508. Most Frequent Subtree Sum
#return the sums with most fequency
#dict to keep track of the frequency
#maxfreq to keep track of the max frequency

def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        maxfreq = [0]
        dic = dict()
        def magic(root):
            if not root: return 0
            val = magic(root.left) + root.val + magic(root.right)
            dic[val] = dic.get(val, 0) + 1
            maxfreq[0] = max(dic[val], maxfreq[0])
            return val
        magic(root)
        res = []
        for i in dic:
            if dic[i] == maxfreq[0]:
                res.append(i)
        return res