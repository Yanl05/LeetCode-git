class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        r = []
        path = []
        candidates.sort()
        self.getPath(candidates, target, path, r, 0)
        return r

    def getPath(self, candidates, target, path, r, start):
        if target == 0:
            r.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            self.getPath(candidates, target - candidates[i],
                         path + [candidates[i]], r, i + 1)
    #     candidates.sort()
    #     #print(candidates)
    #     self.result = []
    #     start = 0
    #     self.backtrack(candidates, target, start, [])
    #     return self.result
    # def backtrack(self, candidates, target, start, val):
    #     if target == 0 and val not in self.result:
    #         self.result.append(val[:])
    #     for i in range(start, len(candidates)):
    #         if target > 0:
    #             val.append(candidates[i])
    #         else:
    #             break
    #         self.backtrack(candidates, target - candidates[i], i + 1, val)
    #         val.pop()



print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))