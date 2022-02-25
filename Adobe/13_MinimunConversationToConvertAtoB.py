nums = [3, 4, 4, 1, 5]
nums1 = [4, 7, 9, 10]
M = len(nums)
N = len(nums1)
def minInsAndDel(nums, nums1, M, N):
    dp = [-1] * len(nums)
    dp[-1] = 1
    #loops starts from the second last element
    res = 0
    for i in range(len(nums)-2, -1, -1):
        temp = 1
        for j in range(i + 1, len(nums)):
            # print(i,dp[j])
            if nums[j]>nums[i] and nums[i] in nums1:
                print(nums[j], nums1)
                temp = max(temp,1 + dp[j])
        #print(dp,i,temp)
        dp[i] = temp
        res = max(res,temp)
    print(res)
    return M + N - (2*res)

print(minInsAndDel(nums,nums1,M,N))