class Solution:
    def twoSum(self, nums, target):
        hm = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hm:
                return [i, hm[diff]]
            else:
                hm[num] = i
                 