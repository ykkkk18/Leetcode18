"""第 9 集：树的深度优先搜索 DFS —— 前中后序 + Bottom-up + Top-down"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build_tree(vals):
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q, i = deque([root]), 1
    while q and i < len(vals):
        node = q.popleft()
        for side in ("left", "right"):
            if i < len(vals) and vals[i] is not None:
                child = TreeNode(vals[i]); setattr(node, side, child); q.append(child)
            i += 1
    return root


# ========== 最简单的 DFS 模板 ==========
# base case -> 做事(do something) 和 递归子问题(recurse)，二者顺序决定了前/中/后序
def preorder(root, out):        # 先做事，再递归
    if not root:
        return
    out.append(root.val)
    preorder(root.left, out)
    preorder(root.right, out)


def inorder(root, out):         # 左 -> 做事 -> 右（只有二叉树才有中序）
    if not root:
        return
    inorder(root.left, out)
    out.append(root.val)
    inorder(root.right, out)


def postorder(root, out):       # 左 -> 右 -> 最后才做事
    if not root:
        return
    postorder(root.left, out)
    postorder(root.right, out)
    out.append(root.val)


# ========== Bottom-up DFS（最常见、最难）==========
# 1. base case
# 2. 向子问题要答案（递归的返回值）
# 3. 利用子问题的答案，构建当前问题的答案
# 4. （可选）额外操作，例如更新全局答案
# 5. 返回答案给父问题 —— 含义必须与第 2 步相同

# 104. 二叉树的最大深度（Bottom-up）
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:                                  # 1
        return 0
    left = max_depth(root.left)                   # 2
    right = max_depth(root.right)
    return max(left, right) + 1                   # 3 + 5：较深的一边 + 连到自己的一条边


# 124. 二叉树中的最大路径和（Hard）
# 递归函数返回：从当前结点往下、"不拐弯"的最大路径和（直上直下）
# 题目要的"人字形"路径只能在当前层拼出来 -> 用全局变量记录
def max_path_sum(root: Optional[TreeNode]) -> int:
    best = float("-inf")

    def dfs(node):
        nonlocal best
        if not node:                              # 1
            return 0
        left = max(dfs(node.left), 0)             # 2 负数只有坏处，不要它（当成 0）
        right = max(dfs(node.right), 0)
        best = max(best, left + right + node.val) # 4 在当前层拼出"人字形"，更新全局答案
        return max(left, right) + node.val        # 3+5 返回给父亲的只能是"直上直下"的一边

    dfs(root)
    return best


# 补充 236. 二叉树的最近公共祖先（讲者点名的经典 Bottom-up 题）
# 返回含义：这棵子树里找到的 p 或 q（或它们的 LCA），找不到返回 None
def lowest_common_ancestor(root, p, q):
    if not root or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:                            # p、q 分别在两边 -> 当前就是 LCA
        return root
    return left or right


# ========== Top-down DFS ==========
# 1. base case   2. 用父问题传下来的值做计算   3.（可选）额外操作   4. 把新值传给子问题继续递归

# 129. 求根节点到叶节点数字之和
def sum_numbers(root: Optional[TreeNode]) -> int:
    total = 0

    def dfs(node, num):
        nonlocal total
        num = num * 10 + node.val                 # 2 拼接数字：上面传下来的 * 10 + 自己
        if not node.left and not node.right:      # 1 base case 是叶子
            total += num                          # 3 到叶子才加入全局答案
            return
        if node.left:                             # 4 往下传
            dfs(node.left, num)
        if node.right:
            dfs(node.right, num)

    if root:
        dfs(root, 0)
    return total


# 补充 112. 路径总和（Top-down：把"剩余目标"往下传）
def has_path_sum(root, target):
    if not root:
        return False
    target -= root.val
    if not root.left and not root.right:
        return target == 0
    return has_path_sum(root.left, target) or has_path_sum(root.right, target)


if __name__ == "__main__":
    t = build_tree([6, 3, None, 1, 4, None, 2, None, 5])
    for name, f in (("前序", preorder), ("中序", inorder), ("后序", postorder)):
        out = []; f(t, out); print(f"{name} [6,3,null,1,4,null,2,null,5] ->", out)
    print("104 max_depth([3,9,20,null,null,15,7]) ->", max_depth(build_tree([3, 9, 20, None, None, 15, 7])))
    print("124 max_path_sum([-10,9,20,null,null,15,7]) ->", max_path_sum(build_tree([-10, 9, 20, None, None, 15, 7])))
    print("124 视频例子 max_path_sum([-25,20,10,15,7,null,null,5,3]) ->",
          max_path_sum(build_tree([-25, 20, 10, 15, 7, None, None, 5, 3])))
    print("129 sum_numbers([4,9,0,5,1]) ->", sum_numbers(build_tree([4, 9, 0, 5, 1])), "(495+491+40)")
    print("129 sum_numbers([1,2,3])     ->", sum_numbers(build_tree([1, 2, 3])), "(12+13)")
    r = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p, q = r.left, r.left.right.right                     # 5 和 4
    print("236 LCA(5, 4) in [3,5,1,6,2,0,8,null,null,7,4] ->", lowest_common_ancestor(r, p, q).val)
    print("236 LCA(5, 1) ->", lowest_common_ancestor(r, r.left, r.right).val)
    print("112 has_path_sum([5,4,8,11,null,13,4,7,2], 22) ->",
          has_path_sum(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2]), 22))
