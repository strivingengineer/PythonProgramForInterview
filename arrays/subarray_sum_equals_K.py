maintainer = 'strivingengineer'
'''
Leetcode 560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/description/
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
Approach: We can precompute the values of current sum and then check if different between current sum and 
target present in the hashmap if yes add its value to answer and in the end return answer
Time/Space Complexity: O(n)/O(n)
'''


def subarraySum(nums, k):
    if not nums:
        return -1
    ans = 0
    tempSum = 0
    compute = {0: 1}  # to handle if compute[i] is equal to k.
    for i in nums:
        tempSum += i
        if tempSum - k in compute:
            ans += compute[tempSum - k]
        compute[tempSum] = compute.get(tempSum, 0) + 1

    return ans
