"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #sort the list of intervals first by start time
        intervals.sort(key = lambda i : i.start)

        #loop through the sorted list, check two intervals at a time i1 & i2
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
            #if i1 end time > i2 start time, there's a conflict (start of second interval should be greater than end of first interval)
            if i1.end > i2.start:
                return False
        #else keep checking and return true if no conflicts
        return True
