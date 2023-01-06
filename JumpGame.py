class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        ptr = len(nums)- 1

        for i in range(n, -1,-1):
            if i + nums[i] >= ptr:
                ptr = i
        return True if ptr == 0 else False
