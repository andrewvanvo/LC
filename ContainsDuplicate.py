class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for num in nums:
            if num in hm:
                return True
            hm[num] = num
        return False
        