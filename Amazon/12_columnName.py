#original problem
def convertToTitle(self, column: int) -> str:
        def magic(n):
            return chr(n + 64)
        
        res = ""
        while column:
            remainder = column % 26
            if remainder == 0:
                remainder = 26
            res = magic(remainder) + res
            column = (column - remainder)//26
        return res


#leetcode version of the inverse of the above
def titleToNumber(self, column: str) -> int:
        def magic(s):
            return ord(s) - ord('A') + 1
        res = 0
        for i in range(len(column)):
            res = res * 26 + magic(str(column[i]))
        return res