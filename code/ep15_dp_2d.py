"""第 15 集：二维动态规划 2D DP 入门 —— 二维矩阵 / 两个一维数组"""
import sys
from typing import List

sys.setrecursionlimit(10000)

# 2D DP 常见的四种输入：
#   1. 一个二维数组       -> 状态 (row, col)                 （本集）
#   2. 两个一维数组       -> 状态 (i, j)，各管一个数组       （本集）
#   3. 一个一维数组 + k   -> 状态 (i, k)                     （第 16 集）
#   4. 一个一维数组       -> 状态 (i, j) 表示子数组 [i..j]   （第 16/17 集）


# ---------- 63. 不同路径 II ----------
# 状态：dp(i, j) = 从 (0,0) 走到 (i,j) 的路径数；只能往右/往下 -> 只能从上边或左边来
def unique_paths_with_obstacles(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    memo = [[None] * n for _ in range(m)]

    def dfs(i, j):
        if i < 0 or j < 0 or grid[i][j] == 1:   # 出界 / 障碍：0 条路
            return 0
        if i == 0 and j == 0:                    # 起点：1 条路
            return 1
        if memo[i][j] is None:
            memo[i][j] = dfs(i - 1, j) + dfs(i, j - 1)   # 上边 + 左边
        return memo[i][j]

    return dfs(m - 1, n - 1)


# 正向填表（带 padding：多开一行一列 0，省去越界判断，但下标整体错一位）
def unique_paths_with_obstacles_table(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if grid[i - 1][j - 1] == 1:
                dp[i][j] = 0
            elif i == 1 and j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m][n]


# ---------- 1143. 最长公共子序列 ----------
# 状态：dp(i, j) = text1[0..i] 和 text2[0..j] 的 LCS 长度
# 只需回头看一个字符：
#   最后两个字符相等  -> dp(i-1, j-1) + 1
#   不相等            -> max(dp(i-1, j), dp(i, j-1))   丢掉其中一个，继承更好的答案
def longest_common_subsequence(a: str, b: str) -> int:
    memo = [[None] * len(b) for _ in range(len(a))]

    def dfs(i, j):
        if i < 0 or j < 0:                       # 有一个是空串：LCS 为 0
            return 0
        if memo[i][j] is None:
            if a[i] == b[j]:
                memo[i][j] = dfs(i - 1, j - 1) + 1
            else:
                memo[i][j] = max(dfs(i - 1, j), dfs(i, j - 1))
        return memo[i][j]

    return dfs(len(a) - 1, len(b) - 1)


# 正向填表：DFS 向"左、上、左上"要答案 -> 填表顺序就是从左到右、从上到下
def longest_common_subsequence_table(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


# ---------- 视频推荐：最长公共子数组（718. 最长重复子数组）----------
# 子数组必须连续：不相等时直接归零，答案取整张表的最大值
def find_length(a: List[int], b: List[int]) -> int:
    m, n, best = len(a), len(b), 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                best = max(best, dp[i][j])
    return best


# ---------- 补充 72. 编辑距离（两个一维数组的 2D DP 经典） ----------
def min_distance(a: str, b: str) -> int:
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])  # 删 / 插 / 替换
    return dp[m][n]


if __name__ == "__main__":
    g = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print("63   unique_paths_with_obstacles([[0,0,0],[0,1,0],[0,0,0]]) ->",
          unique_paths_with_obstacles(g), "| 填表版 ->", unique_paths_with_obstacles_table(g))
    g2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]]
    print("63   4x4、(3,1) 是障碍 ->", unique_paths_with_obstacles(g2), "| 填表版 ->", unique_paths_with_obstacles_table(g2))
    for a, b in (("abcde", "ace"), ("abc", "abc"), ("abc", "def"), ("ac", "ca")):
        print(f"1143 LCS({a!r}, {b!r}) ->", longest_common_subsequence(a, b),
              "| 填表版 ->", longest_common_subsequence_table(a, b))
    print("718  find_length([1,2,3,2,1], [3,2,1,4,7]) ->", find_length([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    print("72   min_distance('horse', 'ros') ->", min_distance("horse", "ros"))
