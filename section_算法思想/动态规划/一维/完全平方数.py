# 问题：给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。
# # 你需要让组成和的完全平方数的个数最少。


# 思想
# - 设定dp[i]为组成和为i的最少完全平方数的个数
# - dp[i] = min(dp[i - k * k] + 1)
# 时间复杂度：O(n*sqrt(n))  空间复杂度O(n)
def numSquares(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = i
        j = 1
        while i - j * j >= 0:  # 注意可以取等于号
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[n]


