maintainer = 'strivingengineer'
'''
Leetcode 189. Rotate Array
https://leetcode.com/problems/rotate-array/description/
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Follow up:
Try to come up with as many solutions as you can.
There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

Approach 1: Ineffective but acceptable in leetcode.
We pop from rear and insert that value at 0 index.
Time: O(k*n)/O(n)
'''


def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """

    k = k % len(nums)
    for i in range(k):
        nums.insert(0, nums.pop())

'''
Another approach is make a copy of array the rotate the k elements
Time/Space Complexity: O(n)/O(n)
'''

def rotate(nums, k):
    k = k % len(nums)
    newarray = nums.copy()
    for i in range(len(nums)):
        nums[(i + k) % len(nums)] = newarray[i]

'''
Another approach is using reversing the array, then reversing first k-1 elements and then again reversing k to last of 
list elements
Time/Space complexity: O(n)/O(1)
'''

def rotate(nums, k):
    k = k % len(nums)
    left, right = 0, len(nums) - 1

    while left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    # to rotate first k elements to correct positions
    left1, right1 = 0, k - 1
    while left1 <= right1:
        nums[left1], nums[right1] = nums[right1], nums[left1]
        left1 += 1
        right1 -= 1
    # to rotate remaining elements to correct positions
    left2, right2 = k, len(nums) - 1
    while left2 < right2:
        nums[left2], nums[right2] = nums[right2], nums[left2]
        left2 += 1
        right2 -= 1

