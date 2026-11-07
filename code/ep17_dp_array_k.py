"""第 17 集：二维 DP 高级 —— 一维数组 + k（状态 = 前 n 个元素 + k）"""
import sys
from functools import lru_cache
from typing import List

sys.setrecursionlimit(10000)


# ---------- 410. 分割数组的最大值 ----------
# 状态：dp(m, n) = 把前 n 个数分成 m 组时，"各组和的最大值"的最小可能值
# 递推（类似 139 单词拆分：切一刀，右边不再分，左边递归）：
#   在位置 k 切一刀：左边前 k 个数分成 m-1 组 -> dp(m-1, k)；右边 nums[k..n-1] 自成一组
#   本切法的答案 = max(dp(m-1, k), sum(nums[k:n]))；所有切法取最小
# 用前缀和 O(1) 求区间和（参考 303. 区域和检索）
def split_array(nums: List[int], m: int) -> int:
    n = len(nums)
    prefix = [0] * (n + 1)
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x
    INF = float("inf")

    @lru_cache(maxsize=None)
    def dfs(m, n):
        if m > n:                                # n 个数分不出 m 组：不合法
            return INF
        if m == 1:                               # 只分一组：就是总和
            return prefix[n]
        res = INF
        for k in range(1, n):                    # 必须切一刀，左右都要非空
            left = dfs(m - 1, k)
            if left == INF:
                continue
            right = prefix[n] - prefix[k]
            res = min(res, max(left, right))
        return res

    return dfs(m, n)


# 正向填表版（第一行的 base case 本身就是前缀和）
def split_array_table(nums: List[int], m: int) -> int:
    n, INF = len(nums), float("inf")
    dp = [[INF] * (n + 1) for _ in range(m + 1)]
    for j in range(1, n + 1):
        dp[1][j] = dp[1][j - 1] + nums[j - 1] if j > 1 else nums[0]
    for i in range(2, m + 1):                    # 组数
        for j in range(i, n + 1):                # j >= i 保证合法
            for k in range(i - 1, j):            # 切点
                right = dp[1][j] - dp[1][k]
                dp[i][j] = min(dp[i][j], max(dp[i - 1][k], right))
    return dp[m][n]


# ---------- 188. 买卖股票的最佳时机 IV ----------
# 状态：dp(k, n) = 用前 n 天的价格、最多 k 笔交易能赚的最多钱
# 递推：
#   不在第 n 天做交易：继承 dp(k, n-1)              （因为是"最多"k 笔，可以不做）
#   在第 i 天买、第 n 天卖：dp(k-1, i) + prices[n-1] - prices[i-1]，枚举所有 i
def max_profit(k: int, prices: List[int]) -> int:
    n = len(prices)
    if n < 2:
        return 0
    if k >= n // 2:                              # 相当于不限次数：122 题的贪心，赚每一段上涨
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))

    @lru_cache(maxsize=None)
    def dfs(k, n):
        if k == 0 or n <= 1:                     # 没有交易次数 / 不足两天：赚不到钱
            return 0
        res = dfs(k, n - 1)                      # 第 n 天不交易
        for i in range(1, n):                    # 第 i 天买，第 n 天卖
            res = max(res, dfs(k - 1, i) + prices[n - 1] - prices[i - 1])
        return res

    return dfs(k, n)


# 正向填表 O(k * n^2)，再加讲者提到的"滚动优化"版 O(k * n)
def max_profit_table(k, prices):
    n = len(prices)
    if n < 2:
        return 0
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for t in range(1, k + 1):
        for j in range(2, n + 1):
            dp[t][j] = dp[t][j - 1]
            for x in range(1, j):
                dp[t][j] = max(dp[t][j], dp[t - 1][x] + prices[j - 1] - prices[x - 1])
    return dp[k][n]


def max_profit_fast(k, prices):
    n = len(prices)
    if n < 2:
        return 0
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for t in range(1, k + 1):
        best = -float("inf")                     # max(dp[t-1][x] - prices[x-1])，边走边更新
        for j in range(2, n + 1):
            best = max(best, dp[t - 1][j - 1] - prices[j - 2])
            dp[t][j] = max(dp[t][j - 1], best + prices[j - 1])
    return dp[k][n]


if __name__ == "__main__":
    for nums, m in (([7, 2, 5, 10, 8], 2), ([1, 2, 3, 4, 5], 2), ([7, 4, 2, 5, 8], 4)):
        print(f"410 split_array({nums}, m={m}) ->", split_array(nums, m), "| 填表版 ->", split_array_table(nums, m))
    for k, p in ((2, [2, 4, 1]), (2, [3, 2, 6, 5, 0, 3]), (3, [3, 2, 6, 5]), (100, [1, 3, 2, 8])):
        print(f"188 max_profit(k={k}, {p}) ->", max_profit(k, p),
              "| 填表版 ->", max_profit_table(min(k, len(p)), p), "| O(kn) 版 ->", max_profit_fast(min(k, len(p)), p))
