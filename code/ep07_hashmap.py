"""第 7 集：哈希表 HashMap —— 需要"快速查找"时，用哈希表把 O(n) 查找降到 O(1)"""
from collections import defaultdict
from typing import List, Optional


# ---------- 1. 两数之和 ----------
# 暴力：两层循环 O(n^2)
def two_sum_brute(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]
    return []


# 哈希表：查找对象 = 目前见过的 值 -> 下标   时间 O(n)，空间 O(n)
def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:              # O(1) 查找
            return [seen[target - x], i]
        seen[x] = i                         # 先查后存，避免同一个元素用两次
    return []                               # 题目保证有解，这行不会执行


# 不要求返回下标时：排序 + 相向双指针（复习第 2 集）  O(n log n)
def two_sum_values(nums: List[int], target: int) -> List[int]:
    a = sorted(nums)                        # 排序后原下标就乱了，所以只能返回值
    i, j = 0, len(a) - 1
    while i < j:
        s = a[i] + a[j]
        if s == target:
            return [a[i], a[j]]
        if s > target:
            j -= 1                          # 太大：右指针左移
        else:
            i += 1                          # 太小：左指针右移
    return []


# ---------- 560. 和为 K 的子数组 ----------
# 子数组和 = 前缀和(0..x) - 前缀和(0..y)
# 查找对象 = 目前为止所有前缀和 -> 出现次数
def subarray_sum(nums: List[int], k: int) -> int:
    count = defaultdict(int)
    count[0] = 1                            # 关键：前缀和 0 默认出现过 1 次
    s = res = 0
    for x in nums:
        s += x
        res += count[s - k]                 # 有多少个之前的前缀和 = s-k，就有多少个子数组和为 k
        count[s] += 1
    return res


# ---------- 推荐题 3. 无重复字符的最长子串（哈希表 + 滑动窗口） ----------
def length_of_longest_substring(s: str) -> int:
    last, left, best = {}, 0, 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1             # 窗口左端跳过重复字符
        last[ch] = right
        best = max(best, right - left + 1)
    return best


# ---------- 推荐题 49. 字母异位词分组（key = 排序后的字符串） ----------
def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for w in strs:
        groups["".join(sorted(w))].append(w)
    return list(groups.values())


# ---------- 推荐题 138. 随机链表的复制（哈希表：旧结点 -> 新结点） ----------
class Node:
    def __init__(self, val, next=None, random=None):
        self.val, self.next, self.random = val, next, random


def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    old2new = {None: None}
    cur = head
    while cur:                              # 第一遍：只建新结点
        old2new[cur] = Node(cur.val)
        cur = cur.next
    cur = head
    while cur:                              # 第二遍：连 next 和 random
        old2new[cur].next = old2new[cur.next]
        old2new[cur].random = old2new[cur.random]
        cur = cur.next
    return old2new[head]


if __name__ == "__main__":
    print("1   two_sum_brute([2,15,9,7], 9) ->", two_sum_brute([2, 15, 9, 7], 9))
    print("1   two_sum([2,15,9,7], 9)       ->", two_sum([2, 15, 9, 7], 9))
    print("    two_sum_values([2,15,9,7], 16) ->", two_sum_values([2, 15, 9, 7], 16))
    print("560 subarray_sum([1,1,1], 2) ->", subarray_sum([1, 1, 1], 2))
    print("560 subarray_sum([1], 1)     ->", subarray_sum([1], 1), "(若不预存 0:1 会错算成 0)")
    v = [3, 4, 7, 2, -3, 1, 4, 2]
    print("560 视频例子 subarray_sum([3,4,7,2,-3,1,4,2], 7) ->", subarray_sum(v, 7))
    print("3   length_of_longest_substring('abcabcbb') ->", length_of_longest_substring("abcabcbb"))
    print("49  group_anagrams(['eat','tea','tan','ate','nat','bat']) ->",
          group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    a, b = Node(7), Node(13); a.next = b; b.random = a
    c = copy_random_list(a)
    print("138 copy_random_list(7->13, 13.random=7) -> 新链表", c.val, "->", c.next.val,
          "| 13.random =", c.next.random.val, "| 是新结点:", c is not a and c.next.random is c)
