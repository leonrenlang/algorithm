# 问题：
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
# 示例 1:
# 输入: [1,2,3]
# 输出: 6
# 示例 2:
# 输入: [1,2,3,4]
# 输出: 24
# 注意:
# 给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
# 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。


# 思想：
# - 首先排序，结果只可能是如下两种情况中的较大值
# - 最小的两个负数，乘上一个整数， 三个正数相乘
def process(nums):
    if len(nums) < 3: return 0
    nums.sort()
    return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])
# 由于只需要用到前两个数和最后三个数，也可以线性遍历，找到这五个数
