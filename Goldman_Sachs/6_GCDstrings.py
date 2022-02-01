class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = math.gcd(len(str1), len(str2))
        if str1+str2 != str2+str1:
            return ""
        if str1[:gcd] == str2[:gcd]:
            return str1[:gcd]
        else:
            return ""