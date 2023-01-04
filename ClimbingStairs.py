class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        left = 1
        right = 2
        for i in range(2,n):
            tmp = left + right
            left = right
            right = tmp 

        return tmp 