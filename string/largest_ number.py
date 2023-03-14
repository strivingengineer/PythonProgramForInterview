import functools

maintainer = 'strivingengineer'
'''
Leetcode 179. Largest Number
https://leetcode.com/problems/largest-number/description/
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 109

Approach: We can sort the input number and then join it to return the largest number.
Time/Space: O(nlogn)/O(n)
'''

#using inbuilt sort function
def largestNumber(nums):
    nums = [str(num) for num in nums]
    nums.sort(key=lambda x: x * 10, reverse=True)
    return str(int(''.join(nums)))

#using custom compare function O(nlogn)/O(1)
def largestNumber1(nums):
    nums = [str(num) for num in nums]

    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0

    nums.sort(key=functools.cmp_to_key(compare))
    return str(int(''.join(nums)))

