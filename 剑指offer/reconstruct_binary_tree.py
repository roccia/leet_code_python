"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class ConstructBst:
    def reconstruct(self, pre_order, in_order):
        self.build(pre_order, 0, len(pre_order) - 1, in_order, 0, len(in_order) - 1)

    def build(self, pre_order, pre_start, pre_end, in_order, in_start, in_end):
        if pre_start > pre_end:
            return None

        root = pre_order[pre_start]
        index = in_start
        while index <= in_end and in_order(index) != root:
            index += 1
        if index > in_end:
            return 'error'

        new_tree = TreeNode(root)
        new_tree.left = self.build(pre_order, pre_start + 1, pre_end + index - in_start,
                                   in_order, in_start, index - 1)
        new_tree.right = self.build(pre_order, pre_start + index - in_start + 1,
                                    pre_end, in_order, index + 1, in_end)
        return new_tree
