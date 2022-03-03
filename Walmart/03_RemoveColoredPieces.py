def winnerOfGame(self, colors: str) -> bool:
    A = 0
    B = 0
    temp = colors[0]
    count = 0
    for i in colors[1:]:
        if i == temp:
            count += 1
        else:
            if count:
                if temp == "A":
                    A += count -1
                else:
                    B += count -1
            count = 0
            temp = i
    if count:
        if temp == "A":
            A += count -1
        else:
            B += count -1
    print(A,B)
    
    if A > B:
        return True
    else:
        return False