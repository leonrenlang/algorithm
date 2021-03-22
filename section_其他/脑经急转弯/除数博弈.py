# 爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
#
# 最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：
#
# 选出任一 x，满足 0 < x < N 且 N % x == 0 。
# 用 N - x 替换黑板上的数字 N 。
# 如果玩家无法执行这些操作，就会输掉游戏。
#
# 只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

# 思想：
# - base case: 拿1一定输，拿2一定赢
# - 当爱丽丝拿到一个奇数时，奇数的因子也只能为奇数，减去一个奇数就是偶数，所以对手一定为偶数
# 对手拿到偶数，每次都选择减1，最终一定能保证自己拿到2，赢
def divisorGame(N: int) -> bool:
    return N % 2 == 0
