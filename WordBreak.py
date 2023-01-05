class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        bank = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for start in range(len(s)):
            if dp[start] == False:
                continue
            for end in range(start+1, len(s)+1):
                if s[start:end] in bank:
                    dp[end] = True
        return dp[-1]