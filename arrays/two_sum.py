maintainer = 'strivingengineer'

'''

Leetcode 1. Two Sum
Link to problem: https://leetcode.com/problems/two-sum/

leetcode.com two-sum problem
Given an array of integers nums and an integer target, return 
indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and 
you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

Solution:

The problem can be solved by multiple ways one approach can be with the use 
of two nested loop with index pointers i , j respectively 
and iterate over the array by checking if i!=j & element at index i + element 
at index j is equal to target element, then return [i,j].

Time/ Space complexity: O(n*n) / O(1)

'''


def two_sum(arr, target):

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] + arr[j] == target:
                return [i, j]

    return -1


'''
A Better approach will be using sorting and then iterating of the array 
using two pointers from left and right using a while loop.
Only part we need to take care is since we have to return the indexes of
elements whose sum equal to target, so we have to sort the element indexes somewhere,
then sort the array.
'''

def two_sum(arr, target):
    newarr = []
    for index, value in enumerate(arr):
        newarr.append([index, value])
# sorting the elements in array based on its value using a lamda     function
    newarr.sort(key=lambda element: element[1])

    start, end = 0, len(newarr)-1

    while start <= end:
        currentSum = newarr[start][1] + newarr[end][1]
        if currentSum == target:
            return [newarr[start][0], newarr[end][0]]
        elif t > target:
            end -= 1
        else:
            start += 1

    return -1


'''
Time/Space complexity: O(nlogn)/O(n)

O(n) for iterating over elements first then O(nlogn) for sorting and then O(n) for 
iteration to check if solution exists .

O(n) + O(nlogn) + O(n) = O(nlogn) for time

O(n) for space to store the indexes of elements

Another approach to solve the problem will be to use a HashMap to sort the indexes 
of element and return the indexes based on value present in it. 
Using HashMap we can solve the problem in O(n) space and O(n) time complexity
'''

def two_sum(arr, target):
    res = {}
    for i in range(len(arr)):
        k = target - arr[i]
        if k in res:
            return [res[k], i]
        res[arr[i]] = i
    return -1

'''
Now you know three ways to solve the two sum problem , which is very famous problem for screening rounds.
'''
