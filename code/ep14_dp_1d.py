"""第 14 集：一维动态规划 1D DP —— 推荐写成 Bottom-up DFS + 记忆化"""
from typing import List


# ---------- 96. 不同的二叉搜索树 ----------
# 关键观察：只和区间"大小"有关（[2,3] 和 [1,2] 能组成的 BST 个数一样）
# 状态：dp(n) = 用 n 个结点能组成多少种 BST
# 递推：根取 i（1..n），左子树 i-1 个结点，右子树 n-i 个结点，两边组合数相乘
def num_trees(n: int) -> int:
    memo = [None] * (n + 1)

    def dfs(n):
        if n <= 1:                               # 空树 / 单结点：1 种
            return 1
        if memo[n] is not None:
            return memo[n]
        res = 0
        for i in range(1, n + 1):
            left = dfs(i - 1)                    # i 已经用作根，左边是 i-1 个
            right = dfs(n - i)
            res += left * right                  # 左右任意两两组合
        memo[n] = res
        return res

    return dfs(n)


# 同一题的"正向填表"写法：先填 base case，从小到大填到 n（代码短，但不如 DFS 好理解）
def num_trees_table(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for size in range(2, n + 1):                 # size 就是 DFS 版里的 n
        for root in range(1, size + 1):          # root 就是 DFS 版里的 i
            dp[size] += dp[root - 1] * dp[size - root]
    return dp[n]


# ---------- 91. 解码方法 ----------
# 状态：dp(n) = 前 n 个字符有多少种解码方式
# 递推：只需回头看两个子问题
#   最后 1 个字符 x 合法（不是 '0'）     -> + dp(n-1)
#   最后 2 个字符 yx 合法（10 ~ 26）     -> + dp(n-2)
def num_decodings(s: str) -> int:
    memo = [None] * (len(s) + 1)

    def dfs(n):
        if n == 0:                               # 空串：1 种
            return 1
        if n == 1:                               # 单个字符：'0' 无法解码
            return 0 if s[0] == "0" else 1
        if memo[n] is not None:
            return memo[n]
        res = 0
        if s[n - 1] != "0":
            res += dfs(n - 1)
        if 10 <= int(s[n - 2:n]) <= 26:
            res += dfs(n - 2)
        memo[n] = res
        return res

    return dfs(len(s))


def num_decodings_table(s: str) -> int:          # 正向填表版
    n = len(s)
    if n == 0 or s[0] == "0":
        return 0
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        if s[i - 1] != "0":
            dp[i] += dp[i - 1]
        if 10 <= int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]
    return dp[n]


# ---------- 推荐题 198. 打家劫舍（1D 经典） ----------
# dp(i) = 前 i 间房最多偷多少：不偷第 i 间 -> dp(i-1)；偷 -> dp(i-2) + nums[i-1]
def rob(nums: List[int]) -> int:
    memo = {}

    def dfs(i):
        if i <= 0:
            return 0
        if i not in memo:
            memo[i] = max(dfs(i - 1), dfs(i - 2) + nums[i - 1])
        return memo[i]

    return dfs(len(nums))


# ---------- 推荐题 322. 零钱兑换（1D，求最小值） ----------
def coin_change(coins: List[int], amount: int) -> int:
    INF = float("inf")
    memo = {}

    def dfs(a):
        if a == 0:
            return 0
        if a < 0:
            return INF
        if a not in memo:
            memo[a] = min(dfs(a - c) + 1 for c in coins)
        return memo[a]

    ans = dfs(amount)
    return -1 if ans == INF else ans


# ---------- 推荐题 140. 单词拆分 II：不是求数值，而是列出所有方案 ----------
# 逻辑和 139 一样，只是 memo 里存的从 True/False 变成"所有拆法的列表"
def word_break_ii(s: str, word_dict: List[str]) -> List[str]:
    words, memo = set(word_dict), {}

    def dfs(i):                                  # s[0:i] 的所有拆法
        if i == 0:
            return [""]
        if i not in memo:
            res = []
            for j in range(i):
                w = s[j:i]
                if w in words:
                    for prefix in dfs(j):
                        res.append((prefix + " " + w).strip())
            memo[i] = res
        return memo[i]

    return dfs(len(s))


if __name__ == "__main__":
    print("96  num_trees(n=1..6)       ->", [num_trees(n) for n in range(1, 7)])
    print("96  num_trees_table(n=1..6) ->", [num_trees_table(n) for n in range(1, 7)])
    for s in ("12", "226", "06", "10", "27", "2101"):
        print(f"91  num_decodings({s!r}) ->", num_decodings(s), "| 填表版 ->", num_decodings_table(s))
    print("198 rob([2,7,9,3,1]) ->", rob([2, 7, 9, 3, 1]))
    print("322 coin_change([1,2,5], 11) ->", coin_change([1, 2, 5], 11), "| coin_change([2], 3) ->", coin_change([2], 3))
    print("140 word_break_ii('catsanddog', [cat,cats,and,sand,dog]) ->",
          word_break_ii("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
