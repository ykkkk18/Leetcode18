# 第 12 集：图 Graph 的深度优先搜索 DFS

## 一、图上的 DFS

和树的 DFS 概念相同：**一口气扎到最深**，走到死路再**回溯**（借助调用栈），然后换另一条路继续扎到底。
和树的区别在于**图可能有环**，遇到已经访问过的结点要停下，否则会死循环。

## 二、图 DFS 模板

**主函数：**
1. 初始化一个哈希集合记录已访问结点。如果题目保证无环，可以省略。
2. 对每个入口结点调用 `dfs`。DFS 是递归，通常要单独写一个函数，参数里带着"状态"。

**`dfs(状态)`：**
- **A.** 校验当前结点：已访问、不合法或已经是答案时，直接 return，相当于 base case。
- **B.** 做点事（**前序** pre-order）。
- 对每个邻居：
  - **C.** 校验邻居：不合法就不递归。
  - 递归 `dfs(邻居)`。
- **D.** 做点事（**后序** post-order），比如收尾工作。

**A 和 C 二选一，也可以都做**：A 是"先进去，发现不合法再退出来"；C 是"先检查，不合法就不进去"。
**B 和 D 根据题意来选**：先做事再递归是前序，先递归再做事是后序。

**复杂度 O(n·k)**：DFS 一般只允许每个结点被访问常数次，k 是 B、D 两步的工作量。

> 重要：**DFS 一定要先定义好"状态"**，也就是递归函数的参数代表什么。

## 三、例 1：200. 岛屿数量

二维网格中，上下左右相连的 1 组成一座岛，求岛的数量。

- 每一片相连的 1 都是一张**独立的图**。
- 从左到右、从上到下扫描网格，**每遇到一个还没访问过的 1**：岛屿数加 1，然后以它为起点做一次遍历（BFS、DFS 都可以），把整座岛**染色**，也就是标记为已访问。
- 之后再扫到这座岛上的其他 1 时，因为已经染过色，就不会重复计数。
- **小技巧**：直接把访问过的 1 改成 0，代替哈希集合。0 本来就是不合法的结点，改完后外层循环的 `if == 1` 自然就跳过了。讲者说这个方法"比较恶心"，因为它修改了输入；代码里先复制一份再修改。
- **状态**就是当前位置 `(i, j)`。
- 时间 O(mn)：每个格子最多访问一次。

## 四、例 2：332. 重新安排行程（较难）

给定一组机票 `[from, to]`，从 JFK 出发，**每张机票必须用且只能用一次**，排出行程。有多种行程时，返回**字典序最小**的那个。

- **这是在"边"上的遍历**：每张机票就是一条边，用过就扔掉。
- **建图**：本题需要按字典序取邻居，所以用"城市 → **最小堆**"代替普通列表。从堆里弹出既能保证字典序，又能顺便**删除这条边**，保证每条边只走一次。
- **状态**：当前所在的城市。

### 为什么必须用后序，不能用前序？

- **前序**是到一个结点就先把它加进答案，再往后走。问题在于这时**还不知道后面的路能不能走通**。
  - 视频例子：`JFK→SFO`、`JFK→PVG`、`SFO→NRT`、`NRT→JFK`。按字典序先飞 PVG，就困在 PVG 了，没有机票可以离开。前序已经把 PVG 写进答案，无法挽回。
- **后序**是**先把后面所有可能性递归完，再处理当前结点**。递归时会把 SFO 和 PVG 两条路都走完，死胡同 PVG 会**最先**被加入答案。所以后序得到的是**倒序**的行程，最后整体反转一次即可：`JFK → SFO → NRT → JFK → PVG`。
- 还是那句话：**相信递归函数是对的**，它会把后面的路都处理好。

时间 O((V+E) log E)：每条边弹出一次，每次堆操作 O(log)。

## 五、完整代码

包括视频例题 200、332（附前序错误版的对比），补充练习：695 岛屿最大面积（用 A 方式校验，同时是 Bottom-up）、207 课程表（有向图找环，用三色标记 + 后序）。

```python
"""第 12 集：图的深度优先搜索 DFS"""
import heapq
import sys
from collections import defaultdict
from typing import List

sys.setrecursionlimit(10000)

# ================= 图 DFS 模板 =================
# 主函数：初始化 visited（无环可省）；对每个入口调用 dfs
# dfs(状态, ...):
#   A. 校验当前结点：已访问 / 不合法 / 已是答案 -> return       （A 与 C 二选一或都做）
#   B. 做点事（前序 pre-order）
#   for 每个邻居:
#      C. 校验邻居：不合法就不递归
#      递归 dfs(邻居)
#   D. 做点事（后序 post-order）                                 （B 与 D 根据题意选）
# 复杂度 O(n * k)：每个结点访问常数次，k 是 B/D 的工作量

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# ---------- 200. 岛屿数量 ----------
# 每遇到一个没访问过的 '1'，就以它为起点做一次遍历，把整座岛"染色"（这里直接改成 '0'）
def num_islands(grid: List[List[str]]) -> int:
    grid = [row[:] for row in grid]              # 复制一份，避免改坏调用者的输入
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        grid[i][j] = "0"                         # 标记已访问（代替 hash set）
        for di, dj in DIRS:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":   # C. 先校验再递归
                dfs(x, y)

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                count += 1                       # 发现一座新岛
                dfs(i, j)                        # 把整座岛染掉
    return count


# 补充 695. 岛屿的最大面积（同一模板，dfs 返回面积 -> Bottom-up）
def max_area_of_island(grid: List[List[int]]) -> int:
    grid = [row[:] for row in grid]
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if not (0 <= i < m and 0 <= j < n) or grid[i][j] == 0:   # A. 先进来再校验
            return 0
        grid[i][j] = 0
        return 1 + sum(dfs(i + di, j + dj) for di, dj in DIRS)

    return max((dfs(i, j) for i in range(m) for j in range(n)), default=0)


# ---------- 332. 重新安排行程 ----------
# 每张机票（边）必须且只能用一次 -> 在"边"上遍历；用过的边直接从堆里删掉
# 必须用后序：先把后面所有可能性递归完，再把当前城市加入答案（最后整体反转）
def find_itinerary(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)                    # 城市 -> 最小堆（保证字典序最小）
    for src, dst in tickets:
        heapq.heappush(graph[src], dst)
    route = []

    def dfs(city):
        while graph[city]:
            nxt = heapq.heappop(graph[city])     # 弹出即删除这张机票
            dfs(nxt)
        route.append(city)                       # D. 后序：子路线都走完了才加自己

    dfs("JFK")
    return route[::-1]                           # 后序得到的是倒序


# 用"前序"会出什么问题：贪心先飞字典序小的，可能走进死胡同
def find_itinerary_preorder_wrong(tickets):
    graph = defaultdict(list)
    for s, d in tickets:
        heapq.heappush(graph[s], d)
    route, city = ["JFK"], "JFK"
    while graph[city]:
        city = heapq.heappop(graph[city])
        route.append(city)
    return route


# ---------- 补充 207. 课程表（有向图找环：DFS 三色标记） ----------
def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)
    state = [0] * num_courses                    # 0 未访问，1 正在当前路径上，2 已完成

    def dfs(u):
        if state[u] == 1:                        # 回到了当前路径上的结点 -> 有环
            return False
        if state[u] == 2:
            return True
        state[u] = 1
        if not all(dfs(v) for v in graph[u]):
            return False
        state[u] = 2                             # 后序：所有后继都没问题才算完成
        return True

    return all(dfs(c) for c in range(num_courses))


if __name__ == "__main__":
    g1 = [list("11110"), list("11010"), list("11000"), list("00000")]
    g2 = [list("11000"), list("11000"), list("00100"), list("00011")]
    print("200 num_islands(例1) ->", num_islands(g1), "| num_islands(例2) ->", num_islands(g2))
    print("695 max_area_of_island ->", max_area_of_island(
        [[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 1, 0, 0, 0]]))
    t1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print("332 find_itinerary(例1) ->", find_itinerary(t1))
    t2 = [["JFK", "SFO"], ["JFK", "PVG"], ["SFO", "NRT"], ["NRT", "JFK"]]   # 视频里的例子
    print("332 find_itinerary(视频例子) ->", find_itinerary(t2))
    print("    前序贪心（错误）    ->", find_itinerary_preorder_wrong(t2), "<- 先飞 PVG 就困住了")
    print("207 can_finish(2, [[1,0]]) ->", can_finish(2, [[1, 0]]),
          "| can_finish(2, [[1,0],[0,1]]) ->", can_finish(2, [[1, 0], [0, 1]]))
```

运行 `python ep12_graph_dfs.py` 的实际输出：

```text
200 num_islands(例1) -> 1 | num_islands(例2) -> 3
695 max_area_of_island -> 5
332 find_itinerary(例1) -> ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
332 find_itinerary(视频例子) -> ['JFK', 'SFO', 'NRT', 'JFK', 'PVG']
    前序贪心（错误）    -> ['JFK', 'PVG'] <- 先飞 PVG 就困住了
207 can_finish(2, [[1,0]]) -> True | can_finish(2, [[1,0],[0,1]]) -> False
```

## 本集要点
- 图 DFS 模板：A/C 校验二选一，B/D 前序、后序根据题意选。
- 先定义好**状态**：网格题是 `(i, j)`，行程题是当前城市。
- "连通块计数"的套路：遇到一个没访问过的起点就计数加 1，再把整个连通块染色。
- **需要先知道后面所有可能性**时用后序，比如 332 题；"每条边只用一次"时在边上遍历，用过就删。
- 讲者建议多做题，培养对"前序还是后序""校验放在递归前还是递归后"的感觉。
