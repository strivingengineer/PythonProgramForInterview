maintainer = 'strivingengineer'
'''
Lintcode 920 · Meeting Rooms (Since its premium on Leetcode)
https://www.lintcode.com/problem/920/description
Description
Given an array of meeting time intervals consisting of start
and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
(0,8),(8,10) is not conflict at 8

Example1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict

Example2
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict

Approach: We can sort the input list of intervals on start time and then iterate over the list by comparing
the lastend to current start if it overlap, return False else return True in the end
Time/Space: O(nlogn)/O(1)
'''

# Lint code solution since its not using list directly
def can_attend_meetings(intervals):
    if not intervals:
        return True
    intervals.sort(key=lambda x: x.start)
    lastend = intervals[0].end
    for i in range(1, len(intervals)):
        s, e = intervals[i].start, intervals[i].end
        if s < lastend:
            return False
        else:
            lastend = e

    return True

# Leetcode solution
def can_attend_meetings(intervals) -> bool:
    if not intervals:
        return True
    intervals.sort(key=lambda x: x[0])
    lastend = intervals[0][1]
    for start, end in intervals[1:]:
        if start < lastend:
            return False
        else:
            lastend = end
    return True

