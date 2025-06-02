class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # cases 
        # 1 if out of bound 0 
        # 2 if text1[] == text2[] memo
        # if text1[] != text2[]
        # return length
        # memoization
        memo = {}

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                # add a 1 each time they match
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
            elif dfs(i + 1, j) > dfs(i, j + 1):
                memo[(i, j)] = dfs(i + 1, j)
            else:
                memo[(i, j)] = dfs(i, j + 1)
            # print(text1[i])
            # print(memo)
            return memo[(i, j)]

        return dfs(0, 0)