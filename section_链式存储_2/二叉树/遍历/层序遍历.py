class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 用队列且需要对层进行操作
def levelorder_print(root):
    if not root: return None
    queue = [root]
    while queue:
        size = len(queue)
        for _ in range(size):
            item = queue.pop(0)
            print(item.value)
            if item.left: queue.append(item.left)
            if item.right: queue.append(item.right)


# 要求最终结果的形式： [[第一层节点的值], [第二层节点的值]...]
def levelOrder(root):
    if not root: return []
    res = []
    queue = [root]
    while queue:
        size = len(queue)
        cur_layer_value = []
        for _ in range(size):
            tmp = queue.pop(0)
            cur_layer_value.append(tmp.val)
            if tmp.left: queue.append(tmp.left)
            if tmp.right: queue.append(tmp.right)
        res.append(cur_layer_value)
    return res


# 问题：给定一个二叉树，返回其节点值自底向上的层次遍历。
# 最终结果的形式应该是： [[第n层节点的值], [第n-1层节点的值]...]
def levelOrder2(root):
    if not root: return []
    res = []
    queue = [root]
    while queue:
        size = len(queue)
        cur_layer_value = []
        for _ in range(size):
            tmp = queue.pop(0)
            cur_layer_value.append(tmp.val)
            if tmp.left: queue.append(tmp.left)
            if tmp.right: queue.append(tmp.right)
        res.insert(0, cur_layer_value)
    return res


# 问题:锯齿形遍历
def traversal_zigzag(root):
    if not root: return []
    queue = [root]
    res = []
    while queue:
        size = len(queue)
        cur_val = []
        for _ in range(size):
            tmp = queue.pop(0)
            cur_val.append(tmp.val)
            if tmp.left: queue.append(tmp.left)
            if tmp.right: queue.append(tmp.right)
        res.append(cur_val)
    for i in range(len(res)):
        if i % 2 != 0:
            res[i].reverse()
    return res


if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    head.left.left.left = TreeNode(8)
    head.left.left.right = TreeNode(9)
    head.left.right.left = TreeNode(10)
    head.left.right.right = TreeNode(11)
    head.right.left.left = TreeNode(12)
    head.right.left.right = TreeNode(13)
    head.right.right.left = TreeNode(14)
    head.right.right.right = TreeNode(15)
    res = levelOrder(head)
    print(res)
