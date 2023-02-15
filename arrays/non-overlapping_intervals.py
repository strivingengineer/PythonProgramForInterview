maintainer = 'strivingengineer'
'''
Leetcode 435. Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/description/
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest 
of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104

Approach: We should first sort the input intervals based on start time, then store the previous interval end
in a variable and iterate over the input intervals & check if start of current interval is not greater then 
previous interval end then increase the count for result, else update previous interval end to current
interval end.
Time/Space: O(nlogn)/O(1) 
'''

def eraseOverlapIntervals(intervals):
    intervals.sort()
    result = 0
    preEnd = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= preEnd:
            preEnd = end
        else:
            result += 1
            preEnd = min(end, preEnd)

    return result

