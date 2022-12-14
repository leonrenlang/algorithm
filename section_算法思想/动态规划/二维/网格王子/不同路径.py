# 问题：一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？

def uniquePaths(m: int, n: int) -> int:
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for i in range(m):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]
