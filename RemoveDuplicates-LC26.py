# 26. Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Consider the number of unique elements in nums to be k. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


nums = [2,4,4,6,8,8,8,10,89,90,90,90,90]

def removeDuplicates(nums):
    n = len(nums)
    start = 0
    for i in range (1,n):
        if nums[i] != nums[start]:
            start +=1
            nums[start] = nums[i]
    return start + 1

result = removeDuplicates(nums)
print(result)