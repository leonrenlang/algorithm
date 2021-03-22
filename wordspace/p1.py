class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def process(node_info):

    def build_tree(node_info, idx):
        head = TreeNode(node_info[idx][0])
        if node_info[idx][1] != -1:
            head.left = build_tree(node_info, idx=node_info[idx][1])
        if node_info[idx][2] != -1:
            head.right = build_tree(node_info, idx=node_info[idx][2])
        return head

    def biggest_cur(node, before, res):
        if not node: return
        tmp = before ^ node.val
        if tmp > res[0]:
            res[0] = tmp
        biggest_cur(node.left, tmp, res)
        biggest_cur(node.right, tmp, res)

    def traverse_tree(head):
        if not head: return None

        biggest_cur(head, 0, res)
        traverse_tree(head.left)
        traverse_tree(head.right)
        return res[0]

    head = build_tree(node_info, 1)
    res = [0]
    traverse_tree(head)
    print(res[0])


if __name__ == '__main__':
    n = int(input())
    dic = {}
    for _ in range(n):
        node_info = [int(item) for item in input().split(' ')]
        dic[node_info[0]] = node_info[1:]
    process(dic)
