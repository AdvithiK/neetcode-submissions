"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #sort by start time & another by end time
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])


        res, count = 0,0
        #start and end pointers
        s,e = 0,0

        while s < len(intervals):
            #increment start and add to count of rooms needed
            if start[s] < end[e]:
                s += 1
                count += 1
            
            #if pos at end array > post at start array, increment end
            #decrease count of rooms needed
            else:
                e += 1
                count -= 1
            #update res to be the maximum between itself and count
            res = max(res, count)
        return res



        