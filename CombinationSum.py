#exponential DFS recursive

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0,[],0)
        return res

#DP solution

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]

        for c in candidates:
            for t in range(1, target + 1):
                if c > t:
                    continue
                if c == t:
                    dp[t].append([c])
                else:
                    for l in dp[t-c]:
                        dp[t].append(l + [c])
        return dp[-1]