class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = 0
        dp = [1]*len(nums)
        for n in range(len(nums)):
            for i in range(n):
                if nums[n] > nums[i]:
                    dp[n] = max(dp[n], dp[i] + 1)
        return max(dp)



