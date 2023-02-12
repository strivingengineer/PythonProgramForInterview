maintainer = 'strivingengineer'
'''
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)

Approach 1: We can use two list to store the product of element to the left of current product
and another to the right of current element and then store the product of these two list 
in result array and return it
Solution: O(n) Space and O(n) time.
'''


def productExceptSelf(nums):
    result = [1] * len(nums)
    left = [1] * len(nums)
    right = [1] * len(nums)

    for i in range(1, len(nums)):
        left[i] = left[i - 1] * nums[i - 1]

    for i in range(len(nums) - 2, -1, -1):
        right[i] *= right[i + 1] * nums[i + 1]

    for i in range(len(nums)):
        result[i] = left[i] * right[i]

    return result

'''
Another approach will be using two variables in place of storing complete list of left and right products
of elements since we need to take care about these values and do the computation in result array.
Time: O(n) , space O(1) since we are not counting result array as space
'''

def productExceptSelf(nums):
    result = [1] * len(nums)
    pre = 1
    for i in range(len(nums)):
        result[i] = pre
        pre *= nums[i]
    post = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= post
        post *= nums[i]
    return result
