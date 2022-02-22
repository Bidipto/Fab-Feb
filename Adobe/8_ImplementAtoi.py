
def atoi(self,string):
    res = 0
    falg = 1
    for i in string:
        if i == "-" and not res:
            flag = -1
        elif i == "+" and not res:
            continue
        elif i.isnumeric():
            res = res*10 + int(i)
        else:
            return -1
    return flag * res