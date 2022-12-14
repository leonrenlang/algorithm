
# 包含min函数的栈
# 用一个辅助栈专门保存最小值
# 进的时候考虑是否要压入辅助栈，出的时候考虑是否要从辅助栈删除


class MinStack:
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

        

    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]
