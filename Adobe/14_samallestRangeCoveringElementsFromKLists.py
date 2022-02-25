def smallestRange(self, arr: List[List[int]]) -> List[int]:
        k = len(arr)
        res = []
        s = set()
        #i is the index of the list and j is the element
        for i in range(len(arr)):
            for j in arr[i]:
                res.append([j,i])
        
        #res is the sorted list of all the elements
        res.sort()
        minn = res[0][0]
        maxx = math.inf
        stack = deque()
        
        i = 0
        # print(res)
        #inital stack containin all k element
        while i < len(res):
            element,key = res[i]
            if len(s) < k:
                if key not in s:
                    s.add(key)
                stack.append([element,key])
                maxx = element
            else:
                break
            i += 1
        
        
        # print(stack, s)
        i += 1
        ans = [stack[0][0], stack[-1][0]]
        gap = abs(stack[-1][0] - stack[0][0])

        # Making the dictionary of elements in the stack
        dic = dict()
        for element,key in stack:
            dic[key] = dic.get(key,0) + 1
            
        #inital stack ko piche se chota
        while dic[stack[0][1]] > 1:
                element2,key2 = stack.popleft()
                dic[key2] -= 1
                # print(stack,dic,element2)
        #updating the gap
        if abs(stack[-1][0] - stack[0][0])<gap:
            gap = abs(stack[-1][0] - stack[0][0])
            ans = [stack[0][0], stack[-1][0]]
        # print(ans)
        #loop covering the res array
        while i<len(res):
            #print(dic)
            element,key = res[i]
            stack.append([element,key])
            dic[key] += 1
            # print(stack,dic)
            while dic[stack[0][1]] > 1:
                element2,key2 = stack.popleft()
                dic[key2] -= 1
                #print(stack,dic,element2)
            if abs(stack[-1][0] - stack[0][0])<gap:
                gap = abs(stack[-1][0] - stack[0][0])
                ans = [stack[0][0], stack[-1][0]]
            i = i + 1
        
        # print(gap)
                
        return ans