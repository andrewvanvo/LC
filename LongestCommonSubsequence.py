class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        matrix = [[0]*(m+1) for _ in range(n+1)]

        for r in range(1, n+1):
            for c in range(1,m+1):
                if text1[r-1] == text2[c-1]:
                    matrix[r][c] = matrix[r-1][c-1] + 1
                else:
                    matrix[r][c] = max(matrix[r-1][c], matrix[r][c-1])
        
        return matrix[-1][-1]
