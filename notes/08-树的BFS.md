# 第 8 集：树 Tree 的广度优先搜索 BFS

> 学习顺序：树比图简单，BFS 比 DFS 简单，所以先学树的 BFS，循序渐进。

## 一、树的基本概念

- 和链表一样，是由引用串起来的数据，内存不一定连续。区别在于链表一个结点只连一个，树的一个结点可以连多个。
- **父结点 parent / 子结点 child** 是相对的概念：12 是 7 的父结点，同时又是 2 的子结点。
- 树可以看作一种特殊的**无环无向图**，只有**一个入口：root**。
- **99% 的题目是没有父指针的二叉树**，所以只能从上往下走。

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
```

把 `left`/`right` 换成一个 `next`，就变成了链表。所以链表是"退化"的树。

## 二、BFS 是什么

**按"层"进行搜索。**对树来说就是第 1 层（root）、第 2 层、第 3 层……对图来说更像洋葱，一圈一圈往外剥。凡是**和层数相关**的树题，都适合用 BFS。

## 三、BFS 通用模板（几乎每道题都能套）

1. **用所有入口初始化队列。**树只有 root 一个入口，以后遇到图时，要把所有起点都放进去。
2. **当队列不为空时：**
   1. **先记下当前层的结点数 `size`**（视频里的 currSize）。
   2. 对当前层的每个结点：
      - 取出结点，按题意处理（比如加入答案）；
      - **展开**它：把孩子**按题目要求的顺序**加入队列；
   3. 层数 + 1。

### 为什么要先记 size？

讲者用"盒子"比喻：取出一个大盒子时，要把里面的小盒子（孩子）放进队列。如果不先记下 `size`，队列长度会随着放入小盒子而**动态变化**，就把下一层的小盒子也当成当前层处理了。**当前层只处理当前层的大盒子。**

### 为什么用队列？

队列先进先出：先进队的先展开，正好保证从左到右、一层一层地处理。Python 用 `collections.deque`，`popleft()` 是 O(1)。

## 四、例题

### 102. 二叉树的层序遍历
标准模板。每层收集一个 `level` 列表，孩子按"先左后右"入队。

如果**去掉 `for size` 那层循环**，就没有"层"的概念了，得到的只是从上到下、从左到右的一个序列，代码中的 `bfs_order` 演示了这一点。

### 104. 二叉树的最大深度
最后展开的那一层就是最深的一层。**把"层"数字化**：每处理完一层 `depth += 1`，最后的 `depth` 就是答案。

### 199. 二叉树的右视图
站在树的右边往左看，看到的是**每一层最右边的结点**。
- 技巧：**先右后左**入队，这样每层队首就是最右边的结点。
- 也可以先左后右入队，取每层**最后一个**结点。
- 这正是模板里"按题目要求的顺序"的含义：从左到右还是从右到左，由题目决定。

## 五、完整代码

包括视频例题 102、104、199，补充练习：103 锯齿形层序遍历、111 最小深度。BFS 遇到第一个叶子就能停下，比 DFS 更快，这正好体现了 BFS 的优势。

```python
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
```

运行 `python ep08_tree_bfs.py` 的实际输出：

```text
树 [3,9,20,null,null,15,7]
102 level_order    -> [[3], [9, 20], [15, 7]]
    bfs_order(不分层) -> [3, 9, 20, 15, 7]
104 max_depth      -> 3
103 zigzag         -> [[3], [20, 9], [15, 7]]
111 min_depth      -> 2
199 right_side_view([1,2,3,null,5,null,4]) -> [1, 3, 4]
199 right_side_view([1,2,3,null,5])        -> [1, 3, 5]
```

## 六、复杂度
每个结点入队、出队各一次：时间 O(n)；队列最多同时容纳一层的结点：空间 O(w)，w 是最宽那层的宽度。

## 本集要点
- 树是只有一个入口的无环图；绝大多数题是没有父指针的二叉树。
- **BFS 模板**：队列初始化 → 记下 size → 逐个取出、处理、按顺序展开 → 层数 + 1。
- 和层数有关的题优先考虑 BFS；改变入队顺序就能解决"从右往左"类问题。
- 下一集讲 DFS：这些题也都能用 DFS 解，但 DFS 的变化更多。
