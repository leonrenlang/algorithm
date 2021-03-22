import random


# 快速排序
# 快排是实际工程当中使用最多的算法，因为其常数项最小
# 快排空间复杂度O(logn),用于记录划分点


# 思想：对数组进行划分，得到划分点，递归的划分左半部分和右半部分
# 如果数组长度等于2，则划分等价于排序
# 数组长度小于等于1，停止递归
def quick_sort(arr):
    def partition(arr, L, R):
        # 对数组进行partition操作，返回划分值的索引
        random_int = random.randint(L, R)  # 加上这两行就变成了随机快排了, 随机从[L,R]中选取一个值
        arr[random_int], arr[R] = arr[R], arr[random_int]  # 就与数据无关
        pivot = arr[R]
        small = L
        for i in range(L, R):
            if arr[i] < pivot:
                arr[i], arr[small] = arr[small], arr[i]
                small += 1
        arr[small], arr[R] = arr[R], arr[small]
        return small

    def process(arr, L, R):
        # 给定数组与一个范围[L,R]，将范围内数据排序
        if L >= R: return None  # 如果需要排序的范围长度小于2，那么就不用排序了
        index = partition(arr, L, R)  # 如果选定范围内仅有两个元素，则partition等价于排序
        process(arr, L, index - 1)
        process(arr, index + 1, R)

    process(arr, 0, len(arr) - 1)
    return arr
