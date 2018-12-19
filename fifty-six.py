# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        lenint = len(intervals)
        if lenint < 2:
            return intervals
        intervals = sorted(intervals, key=lambda startone: startone.start)
        res =[]
        for i in range(1, lenint):
            last = intervals[i-1]
            now = intervals[i]
            if now.start <= last.end:
                now.end = max(intervals[i].end, last.end)
                now.start = last.start
            else:
                res.append(intervals[i-1])
        res.append(intervals[i])
        return res
        # for i in range(1, len(intervals)):
        #     end1 = intervals[i-1][1]
        #     start2 = intervals[i][0]
        #     if start2 < end1:
        #         intervals[i - 1][1] = intervals[i][1]
        #         intervals[i][0] = intervals[i-1][0]
        # tmp = intervals[0]
        # for i in range(1, len(intervals)-1):
        #     if intervals[i] == tmp:
        #         del intervals[i]
        #     tmp = intervals[i]
        # return intervals



intervals = []
solution = Solution()
for item in ([[1,3],[2,6],[8,10],[15,18]]):
    tmp = Interval(item[0], item[1])
    intervals.append(tmp)

# print(intervals[1].start)
print(solution.merge(intervals))