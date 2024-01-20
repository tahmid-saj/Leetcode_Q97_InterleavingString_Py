class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        # return self.recursive(s1, s2, s3, 0, 0, "")
    
        # dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        # return self.recursiveTopDown(s1, s2, s3, 0, 0, "", dp)

        # dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
        # return self.recursiveTopDown2(s1, s2, s3, 0, 0, 0, dp)

        # dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        # return self.bottomUp(s1, s2, s3, dp)

        dpOptimized = [False for _ in range(len(s2) + 1)]
        return self.bottomUpLinearSpace(s1, s2, s3, dpOptimized)

    def recursive(self, s1, s2, s3, index1, index2, curr):
        if curr == s3 and index1 == len(s1) and index2 == len(s2): return True

        if index1 + 1 <= len(s1) and self.recursive(s1, s2, s3, index1 + 1, index2, curr + s1[index1]): return True
        if index2 + 1 <= len(s2) and self.recursive(s1, s2, s3, index1, index2 + 1, curr + s2[index2]): return True

        return False
    
    def recursiveTopDown(self, s1, s2, s3, index1, index2, curr, dp):
        if curr == s3 and index1 == len(s1) and index2 == len(s2): return True

        if index1 + 1 <= len(s1):
            if dp[index1][index2] == False:
                dp[index1][index2] = self.recursiveTopDown(s1, s2, s3, index1 + 1, index2, curr + s1[index1], dp)
            if dp[index1][index2] == True: return True
        if index2 + 1 <= len(s2):
            if dp[index1][index2] == False:
                dp[index1][index2] = self.recursiveTopDown(s1, s2, s3, index1, index2 + 1, curr + s2[index2], dp)
            if dp[index1][index2] == True: return True
        
        return False

    def recursiveTopDown2(self, s1, s2, s3, i, j, k, dp):
        if i == len(s1): return s2[j:] == s3[k:]
        if j == len(s2): return s1[i:] == s3[k:]
        if dp[i][j] >= 0: return True if dp[i][j] == 1 else False

        res = False
        if (s3[k] == s1[i] and self.recursiveTopDown2(s1, s2, s3, i + 1, j, k + 1, dp)) or \
            (s3[k] == s2[j] and self.recursiveTopDown2(s1, s2, s3, i, j + 1, k + 1, dp)):
            res = True

        dp[i][j] = 1 if res == True else 0

        return res
    
    def bottomUp(self, s1, s2, s3, dp):

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0: 
                    dp[i][j] = True
                elif i == 0: 
                    dp[i][j] = dp[i][j - 1] and (s2[j - 1] == s3[i + j - 1])
                elif j == 0: 
                    dp[i][j] = dp[i - 1][j] and (s1[i - 1] == s3[i + j - 1])
                else: 
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[len(s1)][len(s2)]
    
    def bottomUpLinearSpace(self, s1, s2, s3, dp):

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and (s2[j - 1] == s3[i + j - 1])
                elif j == 0:
                    dp[j] = dp[j] and (s1[i - 1] == s3[i + j - 1])
                else:
                    dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[len(s2)]
