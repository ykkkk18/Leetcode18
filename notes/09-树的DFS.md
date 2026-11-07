# 第 9 集：树 Tree 的深度优先搜索 DFS

> DFS 是树里最重要的算法，图里也一样。

## 一、DFS vs BFS

| | BFS | DFS |
| --- | --- | --- |
| 形式 | 迭代（队列） | **递归**（调用栈） |
| 方向 | 水平：一层一层地走 | 垂直：一口气扎到底，没路了再回头 |
| 时间 | O(n) | O(n)：二叉树每个结点严格来说被访问 3 次（下来时、左边回来、右边回来），常数可以忽略 |
| 空间 | 和**宽度**有关，越往下层越宽，越吃内存 | 和**高度**有关，平衡树只需 O(log n)，**更省内存** |

## 二、最简单的 DFS 模板

1. **base case**：防止无限递归。
2. **做事（do something）** 和 **递归子问题（recurse）**：两者的**先后顺序不固定**。

只递归不做事没有意义，而"做事"放在哪里，就决定了遍历顺序：

| 遍历 | 顺序 | 树 `[6,3,null,1,4,null,2,null,5]` 的结果 |
| --- | --- | --- |
| 前序 preorder | **先做事**，再递归左、右 | 6 3 1 2 4 5 |
| 中序 inorder | 左 → **做事** → 右（只有二叉树才有） | 1 2 3 4 5 6（二叉搜索树的中序遍历是有序的） |
| 后序 postorder | 左 → 右 → **最后做事** | 2 1 5 4 3 6（根最后输出） |

**依然最重要的一点：相信你的递归函数是对的。**

## 三、Bottom-up DFS：从下往上传值（最常见，也最难）

利用**子问题传上来的值**构建当前问题的答案，再返回给父问题，所以**一定有返回值**。

**五步：**
1. base case
2. **向子问题要答案**：子问题的答案就是递归函数的返回值
3. **利用子问题的答案构建当前问题的答案**
4. （可选）额外操作，比如更新全局答案
5. **返回答案给父问题**：含义**必须和第 2 步相同**，因为"父亲向我要答案"就是"我向孩子要答案"

> 讲者建议：想递归时，找一个**中间状态**的结点来推，不要盯着 base case 想。

### 例 1：104. 最大深度（Bottom-up）
站在中间结点上：左子树告诉我它深 2 层，右子树告诉我它深 1 层。我取较深的一边，再加上连到自己的这一层，返回 `max(left, right) + 1`。

### 例 2：124. 二叉树中的最大路径和（Hard，"其实一点都不难"）
- 题目要的路径可以是**"人字形"**：从左边上来、经过一个顶点、再从右边下去。
- **递归函数的定义只能是"直上直下"的路径**，即从子树根往下、不拐弯的最大和。原因是如果返回人字形，父结点接上去就不再是一条合法路径了：路径到达顶点后已经拐弯往下，不能再往上走。
- 所以人字形**只能在当前层拼出来**：`left + right + node.val`，用来更新**全局最大值**（第 4 步）；返回给父结点的是 `max(left, right) + node.val`（第 5 步，和第 2 步含义一致）。
- **负数只有坏处**：`left`、`right` 如果是负的，就当成 0，等于不要这一边。
- 按转写还原视频中的树 `[-25,20,10,15,7,null,null,5,3]`：在结点 20 处拼出 `5+15+20+7 = 47`；返回给父结点的是 `20+15+5 = 40`；根是 -25，接上只会变小，所以答案是 47。

### 推荐：236. 最近公共祖先
讲者说这道题是"很多初学者最头疼的 DFS 题"，也是 Bottom-up 的经典题。递归返回的含义是：这棵子树里找到的 p 或 q（或者它们的公共祖先）。左右两边都找到了，当前结点就是答案。

## 四、Top-down DFS：从上往下传值（相对简单）

通过**参数**把值往下传，递归函数一般**没有返回值**，通常在 base case 处更新全局答案。

**四步：**
1. base case
2. 利用父问题传下来的值做计算
3. （可选）额外操作
4. 把新值通过参数传给子问题，继续递归

### 例 3：129. 求根到叶子的数字之和
- 树 `[4,9,0,5,1]` 中，路径组成的数字是 495、491、40，总和为 1026。
- 在结点 9 处：上面传下来 4，拼接成 `4*10 + 9 = 49`，再往下传。
- **base case 是叶子**，不是空结点：到了叶子才能把完整的数字加进全局和。中间结点不能加，因为后面还有数字。

## 五、完整代码

```python
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
```

运行 `python ep09_tree_dfs.py` 的实际输出：

```text
前序 [6,3,null,1,4,null,2,null,5] -> [6, 3, 1, 2, 4, 5]
中序 [6,3,null,1,4,null,2,null,5] -> [1, 2, 3, 4, 5, 6]
后序 [6,3,null,1,4,null,2,null,5] -> [2, 1, 5, 4, 3, 6]
104 max_depth([3,9,20,null,null,15,7]) -> 3
124 max_path_sum([-10,9,20,null,null,15,7]) -> 42
124 视频例子 max_path_sum([-25,20,10,15,7,null,null,5,3]) -> 47
129 sum_numbers([4,9,0,5,1]) -> 1026 (495+491+40)
129 sum_numbers([1,2,3])     -> 25 (12+13)
236 LCA(5, 4) in [3,5,1,6,2,0,8,null,null,7,4] -> 5
236 LCA(5, 1) -> 3
112 has_path_sum([5,4,8,11,null,13,4,7,2], 22) -> True
```

## 本集要点
- DFS 用递归，"做事"放的位置决定前序、中序还是后序；DFS 比 BFS 省内存。
- **Bottom-up 五步**：base case → 向子问题要答案 → 构建当前答案 → （更新全局）→ 返回，第 2 步和第 5 步含义必须一致。
- 题目要的答案和递归返回值不一样时（如 124 题），用**全局变量**记录答案。
- **Top-down**：值通过参数往下传，在叶子处汇总。
