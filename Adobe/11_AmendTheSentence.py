def amendSentence(self, s):
        res = ""
        for i in s:
            if not res and i.isupper():
                res += i.lower()
            elif i.isupper():
                res += " "
                res += i.lower()
            else:
                res += i
        return res