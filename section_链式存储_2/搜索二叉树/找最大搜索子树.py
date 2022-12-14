


# 问题：# 给定一棵二叉树的头结点head,已知其中所有节点的值都不一样，
# 找到含有节点最多的搜索二叉子树，并返回这棵子树的头结点。


# 分析：
# 以节点node为头的树中，最大的搜索二叉子树只可能来自以下两种情况：
# - 来自node左子树上的最大搜索二叉子树是以node左孩子为头的，并且来自node右子树上的
# 最大搜索二叉子树是以node右孩子为头的，node左子树上的最大搜索二叉子树的最大值
# 小于node的节点值，node右子树上的最大搜索二叉子树的最小值大于node的节点值，那么
# 以节点node为头的整棵树都是搜索二叉树
# - 如果不满足第一种情况，说明以节点node为头的树整体不能连成搜索二叉树。这种情况下
# 以node为头的树上的最大搜索二叉子树是来自node的左子树上的最大搜索二叉子树和来自
# node的右子树上的最大搜索二叉子树之间，节点数较多的那个。

# 思路：
# - 遍历过程是后序遍历
# - 遍历到当前cur时，先遍历cur的左子树收集4个信息，分别时左子树上，最大搜索二叉子树的
# 头节点、节点数、树上最小值和书上最大值。同理，获取右子树上这四个信息。
# - 根据步骤2收集的信息，判断是否满足第一种情况，如果满足就返回cur节点。如果满足第二种
# 情况，就返回左子树和右子树格子的最大搜索二叉树中，节点数较多的那个数的头节点


