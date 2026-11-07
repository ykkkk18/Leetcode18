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
