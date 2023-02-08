maintainer = 'strivingengineer'

'''
Leetcode- 15. 3Sum
https://leetcode.com/problems/3sum/description/

Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the
triplets does not matter.
 
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105

Approach: This can be solved using Two SUM II problem help.
To avoid the case to use same number twice in solution we first sort the input list so that duplicate numbers appears
together. 
We iterate over list and check if current value in not same as previous value then we do processing with the help of
Two Sum II logic using two pointers since list is already sorted.

Once we get the solution, we increase the left pointers until we get a new value to avoid using same values twice.
'''


def threeSum(nums):
    res = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:  # check > 0 to avoid i-1 case and avoid using same values twice
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            threesum = nums[i] + nums[l] + nums[r]
            if threesum > 0:
                r -= 1
            elif threesum < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1

                while nums[l] == nums[l - 1] and l < r:  # using this loop to avoid using same values twice
                    l += 1

    return res
