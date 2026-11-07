"""第 18 集：回溯 Backtracking —— Top-down DFS + 状态回溯（记录 -> 递归 -> 回溯）"""
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


# ================= 回溯模板 =================
# backtrack(state):
#   1. base case（通常在叶子：把当前状态的【副本】加入答案）
#   2. for 每条分支 / 每种可能性:
#        a. 记录 / 修改当前状态 -> 下一个状态
#        b. backtrack(下一个状态)
#        c. 回溯：把状态恢复成本层的样子（否则 A 分支的状态会污染 B 分支）

# ---------- 视频开头的例子：所有根到叶子的路径 ----------
def all_root_to_leaf(root: TreeNode) -> List[List[int]]:
    res, path = [], []

    def backtrack(node):
        path.append(node.val)                    # 记录
        if not node.left and not node.right:     # 叶子
            res.append(path[:])
        for child in (node.left, node.right):
            if child:
                backtrack(child)                 # 递归
        path.pop()                               # 回溯

    if root:
        backtrack(root)
    return res


# 反例：忘了回溯，状态会被带进下一个分支
def all_root_to_leaf_wrong(root):
    res, path = [], []

    def dfs(node):
        path.append(node.val)
        if not node.left and not node.right:
            res.append(path[:])
        for child in (node.left, node.right):
            if child:
                dfs(child)
        # 没有 path.pop()

    dfs(root)
    return res


# ---------- 46. 全排列（元素不重复） ----------
# 状态 = (数组当前的排列, index)；index 之前的位置已经固定
# 第 index 个位置依次尝试 [index, n) 里的每个元素：直接 swap 到 index 上，省去额外 buffer
def permute(nums: List[int]) -> List[List[int]]:
    nums, res = nums[:], []

    def backtrack(index):
        if index == len(nums):                   # 最后一个位置也定好了
            res.append(nums[:])                  # 必须复制：nums 还会被继续交换
            return
        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]   # 选 nums[i] 放到 index
            backtrack(index + 1)
            nums[index], nums[i] = nums[i], nums[index]   # 换回来：回溯
    backtrack(0)
    return res


# ---------- 47. 全排列 II（有重复元素） ----------
# 在同一层里，同一个值只尝试一次：用 set 查重，剪掉重复分支
def permute_unique(nums: List[int]) -> List[List[int]]:
    nums, res = nums[:], []

    def backtrack(index):
        if index == len(nums):
            res.append(nums[:])
            return
        used = set()                             # 本层用过的值
        for i in range(index, len(nums)):
            if nums[i] in used:                  # 同样的值放在 index 上，后面搜出来的结果完全一样
                continue
            used.add(nums[i])
            nums[index], nums[i] = nums[i], nums[index]
            backtrack(index + 1)
            nums[index], nums[i] = nums[i], nums[index]
    backtrack(0)
    return res


# ---------- 补充 39. 组合总和（回溯 + 剪枝） ----------
def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    candidates = sorted(candidates)
    res, path = [], []

    def backtrack(start, remain):
        if remain == 0:
            res.append(path[:]); return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:           # 已排序：后面的更大，直接剪枝
                break
            path.append(candidates[i])
            backtrack(i, remain - candidates[i]) # 同一个数可重复使用，所以还是从 i 开始
            path.pop()

    backtrack(0, target)
    return res


# ---------- 补充 51. N 皇后（回溯经典） ----------
def solve_n_queens(n: int) -> List[List[str]]:
    res, cols, d1, d2 = [], set(), set(), set()
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board]); return
        for c in range(n):
            if c in cols or r - c in d1 or r + c in d2:
                continue
            board[r][c] = "Q"; cols.add(c); d1.add(r - c); d2.add(r + c)
            backtrack(r + 1)
            board[r][c] = "."; cols.remove(c); d1.remove(r - c); d2.remove(r + c)

    backtrack(0)
    return res


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))
    # 视频里是 1 -> 2 -> {3,4,5} 的三叉；这里用二叉树演示同样的现象
    print("根到叶子路径（正确回溯） ->", all_root_to_leaf(root))
    print("根到叶子路径（忘记回溯） ->", all_root_to_leaf_wrong(root), "<- 3 被带进了 4 的分支")
    print("46 permute([1,2,3]) ->", permute([1, 2, 3]))
    print("47 permute_unique([1,1,2]) ->", permute_unique([1, 1, 2]))
    print("   对比：不查重 permute([1,1,2]) 有", len(permute([1, 1, 2])), "个（含重复）")
    print("39 combination_sum([2,3,6,7], 7) ->", combination_sum([2, 3, 6, 7], 7))
    sol = solve_n_queens(4)
    print("51 solve_n_queens(4) 共", len(sol), "种解，第一种：")
    for row in sol[0]:
        print("     ", row)
