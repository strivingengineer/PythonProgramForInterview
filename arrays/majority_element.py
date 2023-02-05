maintainer = 'strivingengineer'

'''
Leetcode: 169. Majority Element
https://leetcode.com/problems/majority-element/description/

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 
Follow-up: Could you solve the problem in linear time and in O(1) space?

Approach 1: We can store every element in a hasmap with its count in one iteration.
In another iteration we can check if any value is having count greater than half of input list,
then return that element

Time: O(n)
Space: O(n)
'''

def majorityElement(nums):

    list_length = len(nums)//2
    count_value_dictionary = {}

    for i in nums:
        count_value_dictionary[i] = count_value_dictionary.get(i,0) + 1

    for k,v in count_value_dictionary.items():
        if v > list_length//2:
            return k

'''
Another approach will be using two variables one for count and another for majority_element,
then we iterate over the list once and check if count > 0 & current element is the element which we have stored
is majority_element then increase count value by 1 else decrease count value by 1. In the element which ever
element will be stored in the majority_element variable return it
'''

def majorityElement(nums):

    count, majority_element = 1, nums[0]

    for i in nums[1:]:
        if count ==0:
            count +=1
            majority_element = i
        elif i == majority_element:
            count +=1
        else:
            count -=1

    return majority_element

