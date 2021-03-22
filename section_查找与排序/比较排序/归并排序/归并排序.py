# 归并排序, 原地排序,归并可以帮助理解递归复杂度算法(主方法)
# 为什么归并比一般O(n2)快，因为右边全部排好序之后，左边就只要和一个比较，会有更少浪费掉的比较，所以就快。


# 思想，将数组均分为两部分，分别处理后，两个有序数组合并
# 如果数组的长度为2，划分后再合并相当于排序
# 如果数组长度小于等于1，停止递归
def merge_sort(lis):
    def merge(lis, L, mid, R):
        tmp = []
        p1, p2 = L, mid + 1
        while p1 <= mid and p2 <= R:
            if lis[p1] < lis[p2]:
                tmp.append(lis[p1])
                p1 += 1
            else:
                tmp.append(lis[p2])
                p2 += 1
        tmp += lis[p1:mid + 1]
        tmp += lis[p2:R + 1]
        lis[L:R + 1] = tmp  # 就是一个单纯的赋值行为，不涉及到对象引用的变换

    def process(lis, L, R):
        # 给定一个数组与一个范围，将范围内数据排序
        if L >= R: return None
        mid = (L + R) // 2  # 将数组划分为两个部分[L, mid] [mid, R]
        process(lis, L, mid)
        process(lis, mid + 1, R)
        merge(lis, L, mid, R)

    process(lis, 0, len(lis) - 1)
    return lis


if __name__ == "__main__":
    lis = [5, 325, 123, 1231, 34234, 234, 234, 234, 2, 523, 545, 53]
    print(lis)
    # print(reverse_pairs(lis))
    # print(lis)
