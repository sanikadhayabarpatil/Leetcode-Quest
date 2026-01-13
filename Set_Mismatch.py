
"""
 Leetcode Quest : Data Structure and Algorithms
                Topic: Array II

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]

Constraints:
2 <= nums.length <= 104
1 <= nums[i] <= 104

## 💡 Approach (In-Place Index Marking)

Instead of using extra space like a hashmap, we can **modify the array itself** to detect duplicates and missing numbers.

### Key Insight:
- Each value `v` should be located at index `v - 1`
- Use the **sign of elements** to mark whether a number has been seen

---

### 🪜 Step-by-Step Logic

1. Iterate through the array
2. For each number `num`:
   - Compute its index → `abs(num) - 1`
   - If the value at that index is **positive**, negate it (mark as visited)
   - If already **negative**, the number is the duplicate
3. Iterate again to find the index with a **positive value**
   - That index + 1 is the missing number

---
"""
## 🧪 Python Implementation

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1
        missing = -1
        
        # Step 1: Detect duplicate
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicate = abs(num)
            else:
                nums[index] = -nums[index]
        
        # Step 2: Detect missing number
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
        
        return [duplicate, missing]

## TIME COMPLEXITY : O(n) SPACE COMPLEXITY :O(1)