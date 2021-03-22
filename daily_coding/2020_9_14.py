# 给定一个二叉树，返回它的中序遍历


class Solution:
    def inorderTraversal(self, root):
        if not root: return []
        stack = []
        res = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                # 使用栈每个数据会被经过两次，在出去的时候访问
                res.append(tmp.val)
                root = tmp.right  # 该节点被弹出时，说明该节点的左子树已经遍历完了
        return res
