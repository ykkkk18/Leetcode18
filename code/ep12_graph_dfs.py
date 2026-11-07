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
