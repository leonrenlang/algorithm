# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
# 例如：
# 输入: 原始二叉搜索树:
#               5
#             /   \
#            2     13
#
# 输出: 转换为累加树:
#              18
#             /   \
#           20     13
#


class Solution(object):
    def convertBST(self, root):
        def process(node):
            if not node: return
            process(node.right)
            node.val += self.last
            self.last = node.val
            process(node.left)

        self.last = 0
        process(root)
        return root
