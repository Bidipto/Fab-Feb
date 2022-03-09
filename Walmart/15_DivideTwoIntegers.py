def divide(self, dividend: int, divisor: int) -> int:
    neg = (dividend>0) == (divisor>0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    res = 0
    while dividend >= divisor:
        div = divisor
        temp = 1
        while dividend >= div:
            dividend -= div
            res += temp
            temp = temp<<1
            div = div<<1
    if not neg:
        res = -res
        
    return min( 2147483647, max(res,-2147483648)) 