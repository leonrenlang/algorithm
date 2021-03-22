# 第三题第一张图片
def process(s, n):
    L = len(s)
    matrix = [[0] * n for _ in range(L)]
    p1, p2 = 0, n - 1
    row = 0
    idx = 0
    while idx < L:
        if p1 < p2:
            matrix[row][p1] = s[idx]
            idx += 1
            matrix[row][p2] = s[idx]
            idx += 1
        elif p1 == p2:
            matrix[row][p1] = s[idx]
            idx += 1
        elif p1 > p2:
            matrix[row][p2] = s[idx]
            idx += 1
            matrix[row][p1] = s[idx]
            idx += 1
        p1 = (p1 + 1) if p1 < (n - 1) else 1
        p2 = (p2 - 1) if p2 > 0 else n - 2
        row += 1

# 第三题第二张图片
    res = ''
    for i in range(n):
        tmp = ''
        for j in range(L):
            if matrix[j][i] != 0:
                tmp += matrix[j][i]
        res += tmp
    print(res)
s, n = input().split(',')
n = int(n)
process(s, 3)
