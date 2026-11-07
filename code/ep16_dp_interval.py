"""第 16 集：二维 DP 进阶 —— 一维数组、二维状态 (i, j) 表示子数组区间"""
import sys
from typing import List

sys.setrecursionlimit(10000)


# ---------- 877. 石子游戏 ----------
# 只能从两头拿 -> 剩下的一定是连续区间 [i, j]，一个指针表示不了，需要 (i, j)
# 状态：dp(i, j) = 面对 piles[i..j] 时，当前玩家能拿到的"最大相对分"（我的分 - 对手的分）
# 递推：拿头 piles[i] - dp(i+1, j)；拿尾 piles[j] - dp(i, j-1)，取较大值
def stone_game(piles: List[int]) -> bool:
    n = len(piles)
    memo = [[None] * n for _ in range(n)]

    def dfs(i, j):
        if i > j:                                # 空区间：双方都 0 分
            return 0
        if i == j:                               # 只剩一堆：直接拿走
            return piles[i]
        if memo[i][j] is None:
            memo[i][j] = max(piles[i] - dfs(i + 1, j),
                             piles[j] - dfs(i, j - 1))
        return memo[i][j]

    return dfs(0, n - 1) > 0                     # 相对分 > 0 才算赢（= 0 是平手）


# 正向填表：按区间长度从小到大填（沿对角线斜着填）
def stone_game_table(piles: List[int]) -> bool:
    n = len(piles)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = piles[i]                      # 长度 1：base case（对角线）
    for length in range(2, n + 1):               # 外层：区间长度
        for i in range(0, n - length + 1):       # 内层：左端点，给右端点留出空间
            j = i + length - 1                   # 右端点由 i 和 length 算出
            dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
    return dp[0][n - 1] > 0


# 推荐题 486. 预测赢家：同一个模型，平手也算玩家 1 赢
def predict_the_winner(nums: List[int]) -> bool:
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = nums[i]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
    return dp[0][n - 1] >= 0


# ---------- 5. 最长回文子串 ----------
# 状态：dp(i, j) = s[i..j] 是否是回文（注意：不是"最长回文"，要绕一个弯）
# 递推：s[i] == s[j] 且 dp(i+1, j-1) -> True
# 陷阱：只看 dp(i+1, j-1) 会漏掉 [i, j-1] 和 [i+1, j] 这两个长度 -1 的子区间里的答案
#      所以还要递归这两个，并用全局变量记录最长的回文
def longest_palindrome(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    memo = [[None] * n for _ in range(n)]
    best = [0, 0]                                # 最长回文的 [i, j]

    def dfs(i, j):
        if i >= j:                               # 单字符 / 空串：都是回文
            if i == j and best[1] - best[0] < 0:
                best[:] = [i, j]
            return True
        if memo[i][j] is not None:
            return memo[i][j]
        res = False
        if s[i] == s[j] and dfs(i + 1, j - 1):
            res = True
            if j - i > best[1] - best[0]:
                best[:] = [i, j]
        else:                                    # 当前不是回文，才需要看两个"少一个字符"的子区间
            dfs(i + 1, j)
            dfs(i, j - 1)
        memo[i][j] = res
        return res

    dfs(0, n - 1)
    return s[best[0]:best[1] + 1]


# 正向填表版：同样按长度从小到大
def longest_palindrome_table(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    dp = [[False] * n for _ in range(n)]
    lo, hi = 0, 0
    for i in range(n):
        dp[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = s[i] == s[j] and (length == 2 or dp[i + 1][j - 1])
            if dp[i][j] and length > hi - lo + 1:
                lo, hi = i, j
    return s[lo:hi + 1]


# ---------- 推荐题 516. 最长回文子序列（区间 DP） ----------
def longest_palindrome_subseq(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]


if __name__ == "__main__":
    for p in ([5, 3, 4, 5], [3, 7, 2, 3], [1, 5, 2]):
        print(f"877 stone_game({p}) ->", stone_game(p), "| 填表版 ->", stone_game_table(p))
    print("486 predict_the_winner([1,5,233,7]) ->", predict_the_winner([1, 5, 233, 7]),
          "| [1,5,2] ->", predict_the_winner([1, 5, 2]))
    for s in ("babad", "cbbd", "a", "forgeeksskeegfor"):
        print(f"5   longest_palindrome({s!r}) ->", repr(longest_palindrome(s)),
              "| 填表版 ->", repr(longest_palindrome_table(s)))
    print("516 longest_palindrome_subseq('bbbab') ->", longest_palindrome_subseq("bbbab"))
