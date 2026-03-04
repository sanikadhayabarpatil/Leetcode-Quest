# 1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

nums = [2,4,6,8,10,89]
def runningSum(nums):
    n = len(nums)
    sum = []

    if n ==1:
        return nums
    
    else:
        for i in range(1,n):
            nums[i] = nums[i] + nums[i-1]
            sum = nums
    return sum

result= runningSum(nums)
print(result)

#explaination: if n == 1 we dont do anything we return the original array but if not, then we iterate starting from index 1. For each index we keep adding it with previous index until the nth index
# TC- O(n) SC- O(1)