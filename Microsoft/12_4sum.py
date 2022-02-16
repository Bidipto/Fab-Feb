#3sum with a added look for the fourth element

def fourSum(self, nums, target):
    nums.sort()
    result=[]
    for j in range(len(nums)-3):
        if j>0 and nums[j]==nums[j-1]:
            continue
        for i in range(j+1, len(nums)-2):
            if i>j+1 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while right>left:
                curr=nums[j]+nums[i]+nums[left]+nums[right]
                #print(curr,nums[j],nums[i],nums[left],nums[right])
                if curr>target:
                    right-=1
                elif curr<target:
                    left+=1
                else:
                    result.append([nums[j], nums[i], nums[left], nums[right]])
                    while right>left and nums[left]==nums[left+1]:
                        left+=1
                    while right>left and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
    return result