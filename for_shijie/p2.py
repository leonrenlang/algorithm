# 第二题
def process(n, m, step, matrix):
    # 动态规划
    dp = [[False] * m for _ in range(n)]
    dp[0][0] = True
    for i in range(n):
        for j in range(m):
            flag = False
            if 0 <= i - step <= n - 1 and matrix[i - step][j] == True:
                flag = True
            if 0 <= j - step <= m - 1 and matrix[i][j - step] == True:
                flag = True
            dp[i][j] = flag

    # print(dp[-1][-1])
    # 改成这个
    if dp[-1][-1]:
        print(1)
    else:
        print(0)
    # 改成上述这个

step = int(input())
n, m = [int(item) for item in input().split(' ')]
matrix = []
for _ in range(n):
    matrix.append([int(item) for item in input().split(' ')])
process(n, m, step, matrix)
