"""第 8 集：树的广度优先搜索 BFS —— 一套模板按层展开"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build_tree(vals):
    """按 LeetCode 的层序写法建树：[3,9,20,None,None,15,7]"""
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q, i = deque([root]), 1
    while q and i < len(vals):
        node = q.popleft()
        for side in ("left", "right"):
            if i < len(vals) and vals[i] is not None:
                child = TreeNode(vals[i])
                setattr(node, side, child)
                q.append(child)
            i += 1
    return root


# ================= BFS 模板 =================
# 1. 用所有入口初始化队列（树只有一个入口：root）
# 2. while 队列非空：
#      a. 先记下当前层的结点数 size（之后加入的是下一层，不能算进来）
#      b. 依次取出 size 个结点，按题意处理
#      c. 展开：把孩子按题目要求的顺序加入队列
#      d. 层数 + 1

# 102. 二叉树的层序遍历
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    if not root:
        return res
    q = deque([root])
    while q:
        size = len(q)                       # 当前层的"大盒子"个数
        level = []
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left:                   # 从左到右：先左后右
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res


# 104. 二叉树的最大深度：BFS 一共展开了几层
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    depth, q = 0, deque([root])
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1                          # 每做完一层，深度 + 1
    return depth


# 199. 二叉树的右视图：每层最右边的结点
# 按"先右后左"入队，每层队首就是最右边的结点
def right_side_view(root: Optional[TreeNode]) -> List[int]:
    res = []
    if not root:
        return res
    q = deque([root])
    while q:
        res.append(q[0].val)                # 当前层第一个 = 最右
        for _ in range(len(q)):
            node = q.popleft()
            if node.right:                  # in order：先右再左
                q.append(node.right)
            if node.left:
                q.append(node.left)
    return res


# 补充 103. 锯齿形层序遍历：层号决定方向
def zigzag_level_order(root):
    res = []
    for i, level in enumerate(level_order(root)):
        res.append(level if i % 2 == 0 else level[::-1])
    return res


# 补充 111. 二叉树的最小深度：BFS 遇到的第一个叶子就是答案（比 DFS 更快停下）
def min_depth(root):
    if not root:
        return 0
    q, depth = deque([root]), 1
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1
    return depth


# 不分层的版本：去掉 for 循环，就只是"从上到下、从左到右"的顺序
def bfs_order(root):
    out, q = [], deque([root] if root else [])
    while q:
        node = q.popleft()
        out.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return out


if __name__ == "__main__":
    t = build_tree([3, 9, 20, None, None, 15, 7])
    print("树 [3,9,20,null,null,15,7]")
    print("102 level_order    ->", level_order(t))
    print("    bfs_order(不分层) ->", bfs_order(t))
    print("104 max_depth      ->", max_depth(t))
    print("103 zigzag         ->", zigzag_level_order(t))
    print("111 min_depth      ->", min_depth(t))
    print("199 right_side_view([1,2,3,null,5,null,4]) ->", right_side_view(build_tree([1, 2, 3, None, 5, None, 4])))
    print("199 right_side_view([1,2,3,null,5])        ->", right_side_view(build_tree([1, 2, 3, None, 5])))
