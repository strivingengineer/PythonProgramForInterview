maintainer = 'strivingengineer'

'''
Leetcode 56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], merge 
all overlapping intervals, and return an array of the non-overlapping 
intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

The approach is to sort the input list and then iterate over it. First we store first value from input list to result 
and  then iterate over the list by checking the current index item in list with the end of last result element and 
if they overlap then we modify the end value of last result element to max of current index item & end of last result 
element. If values dont overlap we end current index item in list in result.
Time : O(nlogn) + O(n) ~ O(nlogn)
Space: if we count result store then O(n) else O(1)
'''

def merge_intervals(intervals):
    intervals.sort()
    res =[intervals[0]]

    for i in range(1, len(intervals)):
        start,end = res[-1]

        if intervals[i][0] <= end:
            res[-1][1] = max(intervals[i][1], end)
        else:
            res.append(intervals[i])
    return res