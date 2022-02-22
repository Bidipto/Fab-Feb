N = 3
def AllParenthesis(N):
        res = []
        
        def magic(curr, openn, close):
            if not openn:
                res.append(curr + [")" for i in range(close)])
                if not close:
                    res.append(curr)
                return
            
            if openn == close:
                magic(curr + ["("], openn - 1, close)
            else:
                magic(curr + ["("], openn - 1, close)
                magic(curr + [")"], openn, close - 1)
        
        magic([], N, N)
        return res

print(AllParenthesis(N))