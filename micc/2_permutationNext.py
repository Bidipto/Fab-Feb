#we need the search the peak 
#case 1:the number before the first peak should be swapped with the next greater element at the right of the peak 
# case 2:if no greater ele is found, swap with the peak with left element
#lastly sort the elements after the peak 
#edge case 1: if all the element are sorted acendingly, swap last elements
#edge case 2: all ele are sortred dec, return sorted arr
#[1,3,5,4,2] -> [1,4,5,3,2]
        
nums = [0,9,8,7,6,5,4]

def nextPermutation(nums):
        #edge case1 
        if nums == sorted(nums):
            nums[-1],nums[-2] = nums[-2],nums[-1]
        elif nums == sorted(nums, reverse = True):
            nums = sorted(nums)
        else:
            #searching for the first peak(or maybe the first decline)
            for i in range(len(nums)-2, -1, -1):
                if nums[i] < nums[i + 1]:
                    peak = nums[i+1]
                    peakpos = i+1
                    peakprev = nums[i]
                    break
                #if its the last element just swap the last to, optimization thought we can remove the first edge case
            if i + 2 == len(nums):
                nums[-1],nums[-2] = nums[-2],nums[-1]
                return 
            #traversing the right of peak
            #both the cases are handeled by including the peak in the loop
            for i in range(len(nums) - 1, peakpos - 1, -1):
                if nums[i]>peakprev:
                    nums[i],nums[peakpos-1] = nums[peakpos - 1],nums[i]
                    break
            nums[peakpos:len(nums)] = sorted(nums[peakpos:len(nums)])

nextPermutation(nums)
print(nums)