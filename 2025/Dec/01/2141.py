class Solution(object):
    def maxRunTime(self, n, batteries):
        batteries.sort()
        s = sum(batteries)
        lo, hi = 0, s // n
        arr = batteries
        while lo < hi:
            mid = (lo + hi + 1) // 2
            need = n * mid
            curr = 0
            for x in arr:
                curr += x if x < mid else mid
                if curr >= need:
                    break
            if curr >= need:
                lo = mid
            else:
                hi = mid - 1
        return lo