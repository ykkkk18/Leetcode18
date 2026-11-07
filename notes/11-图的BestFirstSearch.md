# 第 11 集：图 Graph 的 Best-First Search（最优优先搜索）

## 一、为什么需要它

- 第 10 集的 BFS（Breadth-First Search）只适用于**等权图（uniform cost）**，所有边的代价相同。
- **边权不同（non-uniform cost）**时，层数不再等于最短距离。这时要用 **Best-First Search**：**优先展开当前最优（cost 最小）的结点**。
- 怎样每次快速拿到"最优"的结点？用**堆**（第 6 集）。堆每次只给出堆顶，也就是最小的那个，正好满足需要。
- 这就是图中最有名的最短路径算法：**Dijkstra 算法**。

## 二、直观例子

起点 0，边 `0→3` 代价 3，`0→5` 代价 8，`3→5` 代价 2：
1. 展开 0：结点 3 暂定 cost 为 3，结点 5 暂定 cost 为 8。
2. 3 比 8 小，**先展开 3**：经过 3 到达 5 的代价是 3 + 2 = 5，比 8 小，把 5 更新为 5。
3. 最后展开 5，它的最短距离是 5。

就像转机：直飞 8 块钱，转一次机 3 + 2 = 5 块钱，转机更便宜。

## 三、模板：和 BFS 几乎一样，只是**队列换成堆**

1. 用所有起点初始化**最小堆**，每个起点带一个初始 cost，通常为 0；再用一个**哈希集合**记录**已展开**的结点。
2. 当堆不为空时：
   1. 弹出一个结点（堆顶 = 当前 cost 最小的结点）；
   2. **如果已经展开过，跳过**；否则标记为已展开，并记下它的 cost；
   3. （可选）如果是终点，直接返回；
   4. 所有邻居以 **"当前结点的 cost + 边的 cost"** 入堆。

### 和 BFS 的关键区别：查重的位置

- BFS 在**入队时**查重：邻居访问过就不入队。
- Best-First 在**弹出时**查重。原因是**同一个结点可能以不同的 cost 入堆多次**，比如 A 从 B 过来代价是 2，从 C 过来代价是 3，A 就会入堆两次。入堆时还不知道哪个 cost 最小，交给堆去排序。按照最优优先的原则，**A 第一次被弹出时一定带着最小的 cost**，之后再弹出的 A 直接跳过。所以一个结点**可以入堆多次，但只会被展开一次**。

复杂度：每个结点、每条边都要处理，再乘上堆操作的 log。空间 O(V)，也就是堆里的所有元素。

## 四、例 1：743. 网络延迟时间

n 个结点，`times[i] = (u, v, w)` 表示一条**有向边** u→v，传输时间为 w。从 k 发出信号，求所有结点都收到信号的最短时间。

- **转化**：信号同时向各条边扩散，像自来水管分叉后同时流出。最远的房子通水时，所有房子都已经通水了。所以答案就是**到"最远"结点的最短路径**。
- **建图**：邻接表里除了邻居，还要**多存一个 cost**，即 `u → [(v, w), ...]`。Java 要另外写一个类，Python 直接用元组。
- **主逻辑**：套模板，起点 cost 为 0。用 `dict` 同时充当"已展开集合"和"最短时间表"。这道题没有终点，要把整张图都展开完。
- **结果**：展开的结点数 ≠ n，说明有结点收不到信号，返回 -1；否则返回所有最短时间里的最大值。

## 五、例 2：787. K 站中转内最便宜的航班

在最多中转 k 次的前提下，求 src 到 dst 的最低票价。
- 例：`0→1`（100）、`1→2`（100）、`0→2`（500）。k = 1 时可以在 1 中转，答案是 **200**；k = 0 时只能直飞，答案是 **500**。

**多了一个维度：中转次数。**
- 堆里存三个值：`(价格, 城市, 剩余中转次数)`。
- 剩余次数小于 0 时，这是**终止状态**，不能再往外飞。如果这里恰好是终点，仍然可以返回。
- 这道题有**终点**，用上模板里的可选步骤：**第一次弹出终点时，它的价格一定是最便宜的**，直接返回。
- 题目保证没有重复航班和自环。视频据此去掉了 visited 查重。但同一个城市可能以不同的"剩余次数"多次入堆，最坏情况下状态会爆炸，导致超时。代码里加了一个剪枝：到同一个城市时，如果之前已经以**更低价格、更多剩余次数**展开过，就跳过。这是我补充的工程细节。
- 代码里还附了 **Bellman-Ford** 解法：循环 k+1 轮，每轮用上一轮的结果松弛所有边，面试时可以作为对比。

## 六、完整代码

```python
"""第 11 集：Best-First Search（Dijkstra）—— 边权不同的图上找最短路径：把队列换成堆"""
import heapq
from collections import defaultdict
from typing import List

# ================= Best-First Search 模板 =================
# 1. 用所有起点初始化最小堆，每个起点带初始 cost（通常 0）；visited 记录"已展开"的结点
# 2. while 堆非空：
#      a. 弹出 cost 最小的结点
#      b. 已展开过 -> 跳过；否则标记为已展开，记下它的 cost（此时一定是最优的）
#      c. (可选) 是终点就直接返回
#      d. 所有邻居以 "当前 cost + 边的 cost" 入堆
# 和普通 BFS 的区别：查重放在"弹出时"(b)，而不是"入堆时"。
#   同一个结点可能以不同 cost 入堆多次，但只有 cost 最小的那次会被展开。
# 时间 O((V+E) log V) 量级，空间 O(V+E)


# ---------- 743. 网络延迟时间 ----------
# 从 k 出发，信号传遍所有结点的时间 = 到"最远"结点的最短路径
def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)                    # u -> [(v, w)]  有向图，要多存一个 cost
    for u, v, w in times:
        graph[u].append((v, w))
    cost = {}                                    # 已展开的结点 -> 最短时间（兼做 visited）
    heap = [(0, k)]                              # (cost, node)：cost 放前面，堆按它排序
    while heap:
        t, node = heapq.heappop(heap)
        if node in cost:                         # 已展开过，跳过
            continue
        cost[node] = t                           # 第一次弹出时就是最短时间
        for nb, w in graph[node]:
            if nb not in cost:                   # 小优化：已展开的就不必再入堆
                heapq.heappush(heap, (t + w, nb))
    return max(cost.values()) if len(cost) == n else -1   # 有结点到不了 -> -1


# ---------- 787. K 站中转内最便宜的航班 ----------
# 多了一个维度：中转次数。堆里存 (price, city, 剩余可中转次数)
def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))
    heap = [(0, src, k)]                         # 视频里从 k 倒着减到 0，更直观
    best_stops = {}                              # 剪枝：到同一城市，剩余次数更少的状态不必再展开
    while heap:
        price, city, stops = heapq.heappop(heap)
        if city == dst:                          # 最先弹出的终点一定最便宜
            return price
        if stops < 0:                            # 中转次数用完了：终止状态，不能再飞
            continue
        if best_stops.get(city, -2) >= stops:
            continue
        best_stops[city] = stops
        for nb, w in graph[city]:
            heapq.heappush(heap, (price + w, nb, stops - 1))
    return -1


# 787 的另一种经典解法：Bellman-Ford，限制最多 k+1 条边（面试可作为对比）
def find_cheapest_price_bf(n, flights, src, dst, k):
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    for _ in range(k + 1):
        new = dist[:]                            # 只用上一轮的结果，保证边数不超
        for u, v, w in flights:
            if dist[u] + w < new[v]:
                new[v] = dist[u] + w
        dist = new
    return -1 if dist[dst] == INF else dist[dst]


# ---------- 推荐题 1631. 最小体力消耗路径（Best-First 在矩阵上，cost = 路径上最大高度差） ----------
def minimum_effort_path(heights: List[List[int]]) -> int:
    m, n = len(heights), len(heights[0])
    heap, done = [(0, 0, 0)], set()
    while heap:
        effort, i, j = heapq.heappop(heap)
        if (i, j) in done:
            continue
        done.add((i, j))
        if (i, j) == (m - 1, n - 1):
            return effort
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and (x, y) not in done:
                e = max(effort, abs(heights[x][y] - heights[i][j]))
                heapq.heappush(heap, (e, x, y))
    return 0


if __name__ == "__main__":
    print("743 network_delay_time([[2,1,1],[2,3,1],[3,4,1]], n=4, k=2) ->",
          network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
    print("743 有结点到不了 network_delay_time([[1,2,1]], n=2, k=2) ->",
          network_delay_time([[1, 2, 1]], 2, 2))
    print("    视频开头例子 0->3(3), 0->5(8), 3->5(2)：到 5 的最短时间 ->",
          network_delay_time([[0, 3, 3], [0, 5, 8], [3, 5, 2]], 3, 0))
    f = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    print("787 find_cheapest_price(0->2, k=1) ->", find_cheapest_price(3, f, 0, 2, 1),
          "| Bellman-Ford ->", find_cheapest_price_bf(3, f, 0, 2, 1))
    print("787 find_cheapest_price(0->2, k=0) ->", find_cheapest_price(3, f, 0, 2, 0),
          "| Bellman-Ford ->", find_cheapest_price_bf(3, f, 0, 2, 0))
    print("1631 minimum_effort_path([[1,2,2],[3,8,2],[5,3,5]]) ->",
          minimum_effort_path([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
```

运行 `python ep11_best_first_search.py` 的实际输出：

```text
743 network_delay_time([[2,1,1],[2,3,1],[3,4,1]], n=4, k=2) -> 2
743 有结点到不了 network_delay_time([[1,2,1]], n=2, k=2) -> -1
    视频开头例子 0->3(3), 0->5(8), 3->5(2)：到 5 的最短时间 -> 5
787 find_cheapest_price(0->2, k=1) -> 200 | Bellman-Ford -> 200
787 find_cheapest_price(0->2, k=0) -> 500 | Bellman-Ford -> 500
1631 minimum_effort_path([[1,2,2],[3,8,2],[5,3,5]]) -> 2
```

## 本集要点
- 边权相同 → BFS + 队列；**边权不同 → Best-First（Dijkstra）+ 最小堆**。
- 查重放在**弹出时**：结点可以多次入堆，但只展开一次，第一次弹出时的 cost 就是最优。
- 有终点的题，第一次弹出终点时就可以返回。
- 带限制条件（如中转次数）时，把限制条件也放进堆里的状态。
