""" Leetcode Quest : Data Structure and Algorithms
                Topic: Array I

Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
 
Constraints:
•	1 <= nums.length <= 105
•	nums[i] is either 0 or 1.

"""
## Solution :

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                current_count += 1
                # update max count
                if current_count > max_count:
                    max_count = current_count

            else:
                current_count = 0

        return max_count

"""
Explainantion:
create two variables to keep count of max consecutive 1s: max_count, current_count 
if i is 1 we increment current count and if max count is less than current count, max = current 
else i is not equal to one so current count is 0 and so max has no updates
we return max_count as our output 
"""