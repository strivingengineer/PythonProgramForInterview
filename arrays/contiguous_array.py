maintainer = 'strivingengineer'
'''
Leetcode 525. Contiguous Array
https://leetcode.com/problems/contiguous-array/description/
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.

Approach: Since we know that array will only have 0 or 1 so we can use -1 for 0 and 1 for 1 and add it to current sum
variable & check if current sum exists in our map, if yes then we know that till current index the number of 0 & 1
are same.
Time/Space: O(n)/O(n)
'''


def findMaxLength(nums):
    ans = 0
    res = {0: -1}
    sum = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            sum += -1   # using -1 in place of 0 so that we know if current sum already exists or not
        elif nums[i] == 1:
            sum += 1
        if sum in res:
            ans = max(ans, i - res[sum])
        else:
            res[sum] = i

    return ans

