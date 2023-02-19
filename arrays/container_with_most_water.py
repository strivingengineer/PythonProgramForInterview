maintainer = 'strivingengineer'
'''
Leetcode-11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/description/

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104

Approach 1: We can use two nested loops to compare the max area for each one entry in array to all other entries present
but is not a optimal solution.
Time/Space: O(n^2)/O(1)
'''

def maxArea(height): # Time Limit exceed in Leetcode
    maxarea = 0

    for i in range(len(height)):
        for j in range(i, len(height)):
            area = min(height[i], height[j]) * (j - i)
            maxarea = max(area, maxarea)

    return maxarea


'''
Better approach will be with the help of two pointers and iterate over the list once by comparing the calculated
area with max area till now and return max area
Time/Space Complexity: O(n)/O(1)
'''

def maxArea(height):
    maxWater = 0
    left, right = 0, len(height) - 1
    while left <= right:
        area = min(height[left], height[right]) * (right - left)
        maxWater = max(maxWater, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxWater
