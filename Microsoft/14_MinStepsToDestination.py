#basically idea yeh ha ki target agar bina koi negative num ha ho raha ha toh its the easiest way
#else agar zada ho ja raha ha asa koi number ha jo hum add kar rahe ha instead of subtracting
# let the nume be k therefore the num will be (k*2) zada, toh hume wohi nikal na ha ki kab total sum
# target se k*2 zada ho raha ha, its easier cause we have to find the min, qki
# the first instance when the diff between the sum and target is divisible by 2 is the answer 
# a little tricky question but its a good one

def minSteps(self, target):
    s = 0
    i = 0
    while s<target:
        s += i
        i += 1
    while (s - target )%2 == 1:
        s += i
        i += 1
        
    return i-1 