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
