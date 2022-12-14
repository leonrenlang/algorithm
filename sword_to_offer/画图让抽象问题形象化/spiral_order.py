

#顺时针打印矩阵
# 解题思路：将矩阵第一行的元素添加到res列表里，删除第一行
# （也就是matrix中的第一个列表），然后逆时针旋转（这里通过转置+倒序实现）
# ，新的matrix的第一行即为接下来要打印的元素。


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            # list(zip(*matrix))就是顺时针旋转
            matrix = list(zip(*matrix))[::-1]
        return res

