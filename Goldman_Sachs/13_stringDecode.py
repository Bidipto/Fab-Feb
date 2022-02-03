from collections import deque
s = "10[a3[b]]"
# using a two stack approach where we store number in the number stack and we are storing the alplabets 
# in the alpabet stack 
# case 1 when we get a opening parenthesis we append it to the apla stack anf then  we append 
# the corresspoding multiplier in the aplabet stack
# case 2 when we get a close parenthesis we pop all the elements of the stack util the open parenthesis
# and then multiply the the string with the multipler
# In case of no multiplier we append a 1 to the number stack 

class Solution:
    def decodedString(self, s):
        number = []
        alphabet = []
        res = ""
        i = 0

        while i<len(s):
            res = ""
            temp = deque()
            #first we check if its a number
            if s[i] >= '0' and s[i]<='9':
                #if the number is a double digit or more
                if i > 0 and s[i-1] >= '0' and s[i-1]<='9':
                    number[-1] = (number[-1]*10) + int(s[i])
                #when the number is single digit
                else:
                    number.append(int(s[i]))
            elif s[i] == '[':
                alphabet.append(s[i])
                #if there is not multiplier we will append a one
                if i > 0 and ord(s[i-1]) - ord('0')>9:
                    number.append(1)
            elif s[i] == ']':
                while alphabet[-1] != '[':
                    temp.appendleft(alphabet.pop())
                #removing the [
                alphabet.pop()
                multiply = number.pop()
                temp = temp*multiply
                res = "".join([i for i in temp])
                alphabet.append(res)
            elif ord(s[i]) - ord('0')>9:
                #when its a alplaber
                alphabet.append(s[i])
            i = i+1
        return alphabet.pop()
ob = Solution()
print(ob.decodedString(s))               
                    


       