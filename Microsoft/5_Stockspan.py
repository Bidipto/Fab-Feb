#implementation of monotonic stack
#we have to return the max consecutive days were the stock price was less then or equal to the current price
#we can use a stack to keep track of the max consecutive days

prices = [80, 80, 60, 70, 60, 75, 85]

def calculateSpan(prices):
    #declaring empty stack
    stack = []
    
    for price in prices:
        # counter to store the number of consequtive element with equal or less value
        counter = 1
        while stack and stack[-1][0] <= price:
            counter += stack.pop()[1]
        stack.append((price, counter))
        print(counter, end=" ")

calculateSpan(prices)