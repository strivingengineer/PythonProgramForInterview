maintainer = 'strivingengineer'

'''
16. 3Sum Closest
Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104

Approach:
The approach is two use the help of Two Sum II and 3 Sum,
We first sort the input array so that duplicate numbers come together and 
we take take benefit of sorting by iterating over the array using two pointer which will save
memory. 

We take initial variable with result with sum of first three input element of array.
then we iterate over the array using two pointers & check if the sum of current three elements
& difference of target with currentsum and current result value if its less than then we update our result
variable.
'''


def threeSumClosest(nums, target):
    if len(nums) < 3:
        return
    nums.sort()
    result = nums[0] + nums[1] + nums[2]

    for i in range(len(nums)):

        j, k = i + 1, len(nums) - 1
        while j < k:
            currentSum = nums[i] + nums[j] + nums[k]
            if currentSum == target:
                return currentSum
            elif abs(currentSum - target) < abs(currentSum - result):  # to check closet value to target
                result = currentSum
            elif currentSum > target:
                k -= 1
            else:
                j += 1
    return result
