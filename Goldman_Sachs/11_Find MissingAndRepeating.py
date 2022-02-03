#naive approach will be sorting the array and then
# searching for the missing and repeating number
arr = [13,33, 43, 16, 25, 19, 23, 31, 29, 35, 10, 2, 32, 11, 47, 15, 34, 46, 30, 26, 41, 18, 5, 17, 37, 39, 6, 4, 20, 27, 9, 3, 8, 40, 24, 44, 14, 36, 7, 38, 12, 1, 42, 12, 28, 22, 45]
# a better meathond is we will negate all the elements present at the elements index(we are loop on it)
# thefore the element which is double will negate the value in its index twice
for i in range(len(arr)):
    if arr[abs(arr[i])-1]>0:
        arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
    else:
        print("the repeating element",abs(arr[i]))

#since there is a element missing the lets say 4 is missing in the given array therefore the element
#present at that index will not be negative therefore the index of the positive element will be the missing element
for i in range(len(arr)):
    if arr[i]>0:
        print("The missing element is",i+1)