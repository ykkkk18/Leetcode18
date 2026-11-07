# 第 10 集：图 Graph 的广度优先搜索 BFS

## 一、图和树的区别

| | 树 | 图 |
| --- | --- | --- |
| 环 | 无环 | **可能有环**，所以必须**查重** |
| 方向 | 只能从父到子 | 分**无向图**（来回都能走）和**有向图**（箭头方向才能走） |
| 入口 | 只有 root 一个 | **没有固定入口，可能有多个起点**；图没有 root 的概念 |

## 二、图的两种表示方法

图有两个规模参数：**V**（结点数）和 **E**（边数）。

| 表示 | 结构 | 优缺点 |
| --- | --- | --- |
| 邻接矩阵 | V×V 矩阵，`m[i][j] = 1` 表示 i、j 相连 | 一定要开 V² 的空间，边很少时大部分是 0，很浪费；而且**必须预先知道 V** |
| **邻接表**（最常用） | 每个结点 → 它的邻居列表 | 边少时省内存；用 `dict` 实现时**不需要预先知道结点数**，可以动态添加 |

实际题目中往往只给出一堆边，比如 `(0,4)`、`(1,2)`，并不知道一共有多少个结点，甚至可能有不和主体相连的孤立结点。所以最常用的是 **`dict` 形式的邻接表**：key 是结点，value 是它所有邻居组成的 list 或 set。

## 三、BFS 在图上的特点

- 像剥洋葱一样**一圈一圈往外扩展**，所以适合找**最短路径**：目标在第 5 层被扩展到，最短距离就是 5。
- 一个结点第一次被访问时就记下它的层数，之后从别的路径再次到达时，不会再更新。
- **前提：所有边的权重相同（uniform cost）。**如果权重不同，比如直达要 5，绕路是 1+2=3，绕路反而更近，"层数"就不等于最短距离了。这种情况留到第 11 集讲。

## 四、图 BFS 模板

1. **用所有起点初始化队列**，再用一个**哈希集合 `visited`** 记录访问过的结点，防止在环里死循环。
2. 当队列不为空时：
   1. 记下当前层大小 `size`；
   2. 对当前层的每个结点：取出它；（可选）如果是目标，直接返回；把**没访问过且合法**的邻居入队，并标记为已访问；
   3. 层数（也就是 cost）+ 1。

"合法"指的是不越界、不是障碍物等。比如矩阵左上角的格子，只有右边和下面两个邻居。

**二维矩阵小技巧**：预先存好四个方向 `[(0,1),(1,0),(0,-1),(-1,0)]`，循环一下就能拿到上下左右四个邻居。

**时间复杂度 O(V + E)**：每个结点、每条边各访问一次。

## 五、例 1：542. 01 矩阵

求每个格子到最近的 0 的距离。相邻格子的距离为 1，正好是等权图。

- **直接的思路**：对每个 1 单独做一次 BFS 找最近的 0。最坏情况每次都要扫遍整个矩阵，O((mn)²)。
- **反向思维**：**所有 0 同时作为起点**，只做**一次** BFS。第一层扩展到的 1 距离为 1，第二层扩展到的距离为 2……总共 O(mn)。这叫**多源 BFS**。
- 矩阵问题用一个**同样大小的布尔数组**代替哈希集合，标记访问状态。
- 所有 0 一开始就被标记成已访问，所以"没访问过"的格子一定是 1，只需要再判断是否越界。

## 六、例 2：127. 单词接龙（更常见的"隐式图"）

把 `hit` 每次只改一个字母变成 `cog`，中间的每个词都必须在字典里。求最短变换序列包含的**单词数**：`hit → hot → dot → dog → cog`，共 5 个。

- **看出这是图**：每个单词是一个结点，**只差一个字母的两个单词是邻居**。这是无向图，因为把那个字母改回去就能变回来。题目没说是图，但它本质是图上的最短路径问题。这类题才是**最常见**的图题。
- **建图**：枚举所有单词对，判断是否只差一个字母，O(n²) 对。
- **细节**：
  - 终点不在字典里，直接返回 0。
  - 起点可以不在字典里。不在的话要加进去建图，否则起点没有任何邻居，一开始就"死"了。
  - `cost` 从 **1** 开始，因为数的是结点数，结点数 = 边数 + 1；返回 0 表示无解。
- 然后直接套模板：起点入队，遇到终点就返回 `cost`。

> 补充：代码中还提供了 `ladder_length_fast`，用"通配符分桶"建图。比如 `hot` 放进 `*ot`、`h*t`、`ho*` 三个桶，同一个桶里的单词互为邻居。不用比较所有单词对，单词多时快得多，面试时可以作为优化思路提出来。

## 七、完整代码

包括图的两种表示、542、127，以及推荐题 994 腐烂的橘子。994 是多源 BFS，和 542 是同一个套路。

```python
"""第 10 集：图的广度优先搜索 BFS（等权图上的最短路径）"""
from collections import defaultdict, deque
from typing import List

# ---------- 图的表示 ----------
# 邻接矩阵：V x V，matrix[i][j] = 1 表示 i、j 相连。边少时浪费空间
# 邻接表：  node -> 邻居列表。不知道结点总数时用 dict（会自动扩容）
EDGES = [(0, 1), (0, 4), (1, 4), (1, 2), (1, 3), (2, 3), (3, 4)]


def adjacency_matrix(n, edges):
    m = [[0] * n for _ in range(n)]
    for a, b in edges:
        m[a][b] = m[b][a] = 1             # 无向图：两个方向都连
    return m


def adjacency_list(edges):
    g = defaultdict(list)
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)
    return dict(g)


# ================= 图 BFS 模板 =================
# 1. 用【所有】起点初始化队列，并用 visited 记录访问过的结点（图可能有环，必须查重）
# 2. while 队列非空：
#      a. 记下当前层大小 size
#      b. 逐个取出结点；(可选) 若是目标则直接返回
#         把【没访问过且合法】的邻居入队，并立刻标记 visited
#      c. 层数 / cost + 1
# 注意：只适用于每条边权重相同（uniform cost）的图
# 复杂度 O(V + E)

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]   # 二维矩阵的上下左右四个邻居


# ---------- 542. 01 矩阵：每个格子到最近的 0 的距离 ----------
# 反向思维：不是每个 1 各做一次 BFS（O((mn)^2)），而是所有 0 同时作为起点做一次 BFS（O(mn)）
def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    res = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]   # 二维矩阵用布尔数组代替 hash set
    q = deque()
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:                   # 所有 0 都是起点
                q.append((i, j))
                visited[i][j] = True
    cost = 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if mat[i][j] == 1:
                res[i][j] = cost                 # 第一次被扩展到时的层数就是最近距离
            for di, dj in DIRS:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    q.append((x, y))
                    visited[x][y] = True
        cost += 1
    return res


# ---------- 127. 单词接龙 ----------
# 隐式图：两个单词只差一个字母就是邻居（无向图）
def one_change_away(a: str, b: str) -> bool:
    return sum(x != y for x, y in zip(a, b)) == 1


def construct_graph(words: List[str]):
    g = defaultdict(list)
    for i in range(len(words)):                  # 枚举每一对单词：O(n^2 * L)
        for j in range(i + 1, len(words)):
            if one_change_away(words[i], words[j]):
                g[words[i]].append(words[j])
                g[words[j]].append(words[i])
    return g


def ladder_length(begin: str, end: str, word_list: List[str]) -> int:
    words = list(word_list)
    if end not in words:
        return 0
    if begin not in words:                       # 起点可以不在字典里，加进去方便建图
        words.append(begin)
    g = construct_graph(words)
    visited, q = {begin}, deque([begin])
    cost = 1                                     # 题目数的是单词个数 = 边数 + 1
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur == end:                       # 可选步骤：找到终点直接返回
                return cost
            for nb in g.get(cur, []):
                if nb not in visited:
                    visited.add(nb)
                    q.append(nb)
        cost += 1
    return 0


# 更快的建图方式（面试加分）：通配符分桶  "hot" -> "*ot","h*t","ho*"，O(n * L^2)
def ladder_length_fast(begin, end, word_list):
    words = set(word_list)
    if end not in words:
        return 0
    buckets = defaultdict(list)
    for w in words | {begin}:
        for i in range(len(w)):
            buckets[w[:i] + "*" + w[i + 1:]].append(w)
    visited, q, cost = {begin}, deque([begin]), 1
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur == end:
                return cost
            for i in range(len(cur)):
                for nb in buckets[cur[:i] + "*" + cur[i + 1:]]:
                    if nb not in visited:
                        visited.add(nb); q.append(nb)
        cost += 1
    return 0


# ---------- 推荐题 994. 腐烂的橘子（多源 BFS，和 542 同一个套路） ----------
def oranges_rotting(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    q = deque((i, j) for i in range(m) for j in range(n) if grid[i][j] == 2)
    fresh = sum(row.count(1) for row in grid)
    minutes = 0
    while q and fresh:
        for _ in range(len(q)):
            i, j = q.popleft()
            for di, dj in DIRS:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2               # 直接改原数组充当 visited
                    fresh -= 1
                    q.append((x, y))
        minutes += 1
    return -1 if fresh else minutes


if __name__ == "__main__":
    print("邻接矩阵:")
    for row in adjacency_matrix(5, EDGES):
        print("   ", row)
    print("邻接表:", adjacency_list(EDGES))
    for mat in ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [1, 1, 1]]):
        print("542 update_matrix", mat, "->", update_matrix(mat))
    wl = ["hot", "dot", "dog", "lot", "log", "cog"]
    print("127 ladder_length('hit','cog',", wl, ") ->", ladder_length("hit", "cog", wl))
    print("127 ladder_length_fast 同一输入 ->", ladder_length_fast("hit", "cog", wl))
    print("127 字典里没有 'cog' ->", ladder_length("hit", "cog", wl[:-1]))
    print("994 oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) ->", oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
```

运行 `python ep10_graph_bfs.py` 的实际输出：

```text
邻接矩阵:
    [0, 1, 0, 0, 1]
    [1, 0, 1, 1, 1]
    [0, 1, 0, 1, 0]
    [0, 1, 1, 0, 1]
    [1, 1, 0, 1, 0]
邻接表: {0: [1, 4], 1: [0, 4, 2, 3], 4: [0, 1, 3], 2: [1, 3], 3: [1, 2, 4]}
542 update_matrix [[0, 0, 0], [0, 1, 0], [0, 0, 0]] -> [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
542 update_matrix [[0, 0, 0], [0, 1, 0], [1, 1, 1]] -> [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
127 ladder_length('hit','cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'] ) -> 5
127 ladder_length_fast 同一输入 -> 5
127 字典里没有 'cog' -> 0
994 oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) -> 4
```

## 推荐练习（视频结尾列出的等权 BFS 题）
934 最短的桥、310 最小高度树、1091 二进制矩阵中的最短路径、994 腐烂的橘子、863 二叉树中所有距离为 K 的结点、317 离建筑物最近的距离。

## 本集要点
- 图可能有环、有多个入口，所以要**把所有起点入队**并用 `visited` 查重。
- 最常用的表示是 `dict` 形式的邻接表。
- 等权图上，BFS 的层数就是最短距离；**多源 BFS**（所有起点同时出发）能把 O((mn)²) 降到 O(mn)。
- 很多题是**隐式图**，要自己发现"结点是什么、邻居是什么"，然后套模板。
