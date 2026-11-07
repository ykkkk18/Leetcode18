"""第 13 集：搜索 Search 与动态规划 DP 入门 —— DP = Search + 记忆化"""
import time
from functools import lru_cache
from typing import List


# ================= Top-down DFS 搜索模板 =================
# 1. 定义状态（每个子问题都能用一个状态描述）  2. 初始化初始状态  3. 调用 dfs
# dfs(状态):
#   a. base case
#   b. for 每个子问题：更新到下一个状态 -> 递归 -> 恢复状态（restore！）

# ---------- 78. 子集 ----------
# 状态 = (index, 当前子集)；每个元素两条分支：要 / 不要；搜索树有 2^n 个叶子
def subsets(nums: List[int]) -> List[List[int]]:
    res = []

    def dfs(index, cur):
        if index == len(nums):                   # base case：走到叶子，就是一个子集
            res.append(cur[:])                   # 必须复制！cur 会被继续修改
            return
        cur.append(nums[index])                  # 分支 1：要
        dfs(index + 1, cur)
        cur.pop()                                # 恢复状态，再走另一条分支
        dfs(index + 1, cur)                      # 分支 2：不要

    dfs(0, [])
    return res


# 补充 46. 全排列（同样是没有重复子问题的纯搜索）
def permute(nums: List[int]) -> List[List[int]]:
    res, used = [], [False] * len(nums)

    def dfs(cur):
        if len(cur) == len(nums):
            res.append(cur[:]); return
        for i, x in enumerate(nums):
            if not used[i]:
                used[i] = True; cur.append(x)
                dfs(cur)
                cur.pop(); used[i] = False       # 恢复状态

    dfs([])
    return res


# ================= Bottom-up DFS + 记忆化 = DP =================
# 1. 定义状态  2. 初始化 memo  3. return dfs(最终状态)  —— 我们要的是"顶层"答案
# dfs(状态):
#   a. base case
#   b. 若 memo 里已有 -> 直接返回          （DP 才有）
#   c. 向所有子问题要答案，构建当前答案（transition rule 递推规则）
#   d. 存入 memo                           （DP 才有）
#   e. 返回

# ---------- 补充 70. 爬楼梯：对比"纯搜索"和"搜索 + 记忆化" ----------
def climb_search(n):                             # 子问题大量重复：O(2^n)
    if n <= 1:
        return 1
    return climb_search(n - 1) + climb_search(n - 2)


def climb_dp(n, memo=None):                      # 每个状态只算一次：O(n)
    memo = {} if memo is None else memo
    if n <= 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = climb_dp(n - 1, memo) + climb_dp(n - 2, memo)
    return memo[n]


# ---------- 139. 单词拆分 ----------
# 状态（1D）：dp(i) = word[0:i] 能否被字典里的词拼出来
# 递推：存在 j < i，使 dp(j) 为真 且 word[j:i] 在字典里
def word_break(s: str, word_dict: List[str]) -> bool:
    words = set(word_dict)                       # 转成 set，O(1) 查找
    memo = [None] * (len(s) + 1)

    def dfs(i):
        if i == 0:                               # 空串：认为可以拆分
            return True
        if memo[i] is not None:
            return memo[i]
        memo[i] = False
        for j in range(i):                       # 子问题 j 一定比 i 小
            if s[j:i] in words and dfs(j):       # 先查右半边，不在字典里就不用递归
                memo[i] = True
                break
        return memo[i]

    return dfs(len(s))                           # 丢进去的是最终状态 n


# 同一题的写法 2：用 lru_cache 自动记忆化
def word_break_cache(s, word_dict):
    words = set(word_dict)

    @lru_cache(maxsize=None)
    def dfs(i):
        return i == 0 or any(s[j:i] in words and dfs(j) for j in range(i))

    return dfs(len(s))


if __name__ == "__main__":
    print("78  subsets([1,3,4]) ->", subsets([1, 3, 4]))
    print("    subsets([1,3,4,7]) 个数 ->", len(subsets([1, 3, 4, 7])), "(= 2^4)")
    print("46  permute([1,2,3]) ->", permute([1, 2, 3]))
    t = time.perf_counter(); a = climb_search(30); t1 = time.perf_counter() - t
    t = time.perf_counter(); b = climb_dp(30); t2 = time.perf_counter() - t
    print(f"70  爬 30 级楼梯：纯搜索 {a}（{t1:.3f}s）| 记忆化 {b}（{t2:.6f}s）")
    for s, d in (("leetcode", ["leet", "code"]), ("applepenapple", ["apple", "pen"]),
                 ("catsandog", ["cats", "dog", "sand", "and", "cat"])):
        print(f"139 word_break({s!r}, {d}) ->", word_break(s, d), "| lru_cache 版 ->", word_break_cache(s, d))
