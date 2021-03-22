

# 题目描述
# 又到了吃午饭的时间，你和你的同伴刚刚研发出了最新的GSS-483型自动打饭机器人，现在你们正在对机器人进行功能测试。
# 为了简化问题，我们假设午饭一共有N个菜，对于第i个菜，你和你的同伴对其定义了一个好吃程度（或难吃程度，如果是负数的话……）A[i]，
# 由于一些技（经）术（费）限制，机器人一次只能接受一个指令：两个数L, R——表示机器人将会去打第L~R一共R-L+1个菜。
# 本着不浪费的原则，你们决定机器人打上来的菜，含着泪也要都吃完，于是你们希望机器人打的菜的好吃程度之和最大
# 然而，你善变的同伴希望对机器人进行多次测试（实际上可能是为了多吃到好吃的菜），他想知道机器人打M次菜能达到的最大的好吃程度之和
# 当然，打过一次的菜是不能再打的，而且你也可以对机器人输入-1, -1，表示一个菜也不打
# 输入描述:
# 第一行：N, M
#
# 第二行：A[1], A[2], ..., A[N]
# 输出描述:
# 一个数字S，表示M次打菜的最大好吃程度之和
# 示例1
# 输入
# 复制
# 7 2
# 1 2 3 -2 3 -10 3
# 输出
# 复制
# 10
# 说明
# [1 2 3 -2 3] -10 [3]
# 示例2
# 输入
# 复制
# 7 4
# 1 2 3 -2 3 -10 3
# 输出
# 复制
# 12
# 说明
# [1 2 3] -2 [3] -10 [3]
#
# 第四次给机器人-1, -1的指令
# 备注:
# N <= 10^5 = 100000
#
# |A[i]| <= 10^4 = 10000
#
# 10%数据M = 1
#
# 50%数据M <= 2
#
# 80%数据M <= 100
#
# 100%数据M <= 10^4 = 10000

# 参考:nowcoder.com/questionTerminal/824af5cb05794606b56657bb3fa91f49?answerType=1&f=discussion
# 思想:就是一个最大的m段字段和问题

