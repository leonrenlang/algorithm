""" 说明1：冒泡和选择工程上已经没有人用了，在数据量小的时候，插入排序还比较有用
    说明2：
        一般排序默认为从小到大排序
        实现的版本都是原地排序
 """


def insert_sort(lis: list) -> list:
    # 插入排序
    if not lis: return None
    for i in range(1, len(lis)):  # i指向每次要向前放的牌
        for j in reversed(range(0, i)):  # 依次遍历i-1 ... 0
            if lis[j + 1] < lis[j]:
                lis[j + 1], lis[j] = lis[j], lis[j + 1]
    return lis


def bubble_sort(lis: list) -> list:
    # 冒泡排序
    if not lis or len(lis) < 2:   return lis
    for i in range(1, len(lis)):  # 相当于规定了一次冒泡的范围[0,len(lis)-i)
        for j in range(len(lis) - i):
            if lis[j] > lis[j + 1]:  # 改成“<”则为从大到小
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    return lis


def select_sort(lis: list) -> list:
    # 选择排序
    if not lis or len(lis) < 2:   return lis
    for i in range(0, len(lis) - 1):  # 规定了一次选择的范围[i+1,len(lis)-1]
        min_idx = i
        for j in range(i + 1, len(lis)):
            min_idx = j if lis[j] < lis[min_idx] else min_idx
        lis[i], lis[min_idx] = lis[min_idx], lis[i]
    return lis


def correctSort(array):
    return sorted(array)


if __name__ == "__main__":
    import numpy as np

    lis = list(np.random.randint(1, 10000, (10,)))
    print(lis)
    select_sort(lis)
    print(lis)
