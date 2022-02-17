#watch neetcode alien dict video for better understanding
#https://www.youtube.com/watch?v=6kTZYvNNyps

def findOrder(self,arr , N, alphabets):
        adj = {chr(i):set() for i in range(97, 97 + alphabets)}
        #adj list
        #we find the first change in letter, therefore we have a connection,
        # ie the order of precedence
        for i in range(N-1):
            word1 = arr[i]
            word2 = arr[i+1]
            l1 = len(word1)
            l2 = len(word2)
            minnlen = min(l1, l2)
            if l1 == l2 and word1 == word2:
                continue
            for j in range(minnlen):
                if word1[j] != word2[j]:
                    #print(word1[j],word2[j],word1,word2)
                    adj[word1[j]].add(word2[j])
                    break
        # print(adj)
        res = []
        visited = set()
        cycle = set()
        
        def magic(root):
            if root in visited:
                return True
            if root in cycle:
                return False
            
            cycle.add(root)
            
            for i in adj[root]:
                if not magic(i):
                    return False
            
            res.append(root)
            visited.add(root)
            cycle.remove(root)
            return True
        
        for i in adj:
            if not magic(i):
                return ''
        
        
        a = ''.join(reversed(res))
        #print(a)
        return a