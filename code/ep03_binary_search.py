"""第 3 集：二分查找 Binary Search —— 三大模板 + 在"答案区间"上二分"""
from typing import List


# ---------- 模板 1：找精确值  while l <= r，l = mid+1 / r = mid-1 ----------
def find_exact(arr: List[int], k: int) -> int:
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2           # 别写 (l+r)//2：其他语言里会溢出
        if arr[mid] == k:
            return mid
        if arr[mid] > k:
            r = mid - 1
        else:
            l = mid + 1
    return -1                            # 不存在


# ---------- 模板 2：找模糊值  while l < r ----------
# 2a 第一次出现：小于 k 的 mid 一定不是答案 -> l = mid+1；否则 mid 可能是答案 -> r = mid
def first_occurrence(arr: List[int], k: int) -> int:
    if not arr:
        return -1
    l, r = 0, len(arr) - 1
    while l < r:                         # 若写 l <= r，l==r 时 r=mid 原地不动 -> 死循环
        mid = l + (r - l) // 2           # 偶数个元素时偏左
        if arr[mid] < k:
            l = mid + 1
        else:
            r = mid                      # 不能 mid-1：会排除潜在答案
    return l if arr[l] == k else -1


# 2b 最后一次出现：大于 k 的 mid 一定不是答案 -> r = mid-1；否则 l = mid
def last_occurrence(arr: List[int], k: int) -> int:
    if not arr:
        return -1
    l, r = 0, len(arr) - 1
    while l < r:
        mid = l + (r - l + 1) // 2       # 偶数个元素时偏右！否则 l = mid 不动 -> 死循环
        if arr[mid] > k:
            r = mid - 1
        else:
            l = mid
    return l if arr[l] == k else -1


# ---------- 模板 3：万用型  while l < r-1，l = mid / r = mid ----------
# 最后剩下相邻的 l、r 两个候选，再比一比
def closest(arr: List[int], k: int) -> int:
    l, r = 0, len(arr) - 1
    while l < r - 1:
        mid = l + (r - l) // 2
        if arr[mid] < k:
            l = mid
        else:
            r = mid
    if arr[r] < k:                       # 最大值都比 k 小
        return r
    if arr[l] > k:                       # 最小值都比 k 大
        return l
    return l if k - arr[l] <= arr[r] - k else r   # k 落在两者之间


# ---------- 1062. 最长重复子串：在"答案的长度区间"上二分 ----------
# 若长度 x 存在重复子串，则更短的一定也存在 -> 答案区间 [0, n-1] 是"有序"的
def longest_repeating_substring(s: str) -> int:
    def ok(length: int) -> bool:         # 是否存在长度为 length 且出现 >=2 次的子串
        seen = set()
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub in seen:
                return True
            seen.add(sub)
        return False

    l, r = 0, len(s) - 1
    while l < r:
        mid = l + (r - l + 1) // 2       # 下面用 l = mid，所以偏右
        if ok(mid):
            l = mid                      # mid 可行，想要更长，但不能把 mid 排除
        else:
            r = mid - 1                  # mid 不可行，更长的更不可行
    return l


# ---------- 同类题 1011. 在 D 天内送达包裹的能力（视频推荐的"换马甲"题） ----------
def ship_within_days(weights: List[int], days: int) -> int:
    def need_days(cap: int) -> int:
        d, cur = 1, 0
        for w in weights:
            if cur + w > cap:
                d, cur = d + 1, 0
            cur += w
        return d

    l, r = max(weights), sum(weights)    # 运力的答案区间
    while l < r:                         # 找"最小可行值" -> first occurrence 型
        mid = l + (r - l) // 2
        if need_days(mid) <= days:
            r = mid
        else:
            l = mid + 1
    return l


# ---------- 同类题 410. 分割数组的最大值（和 1011 是同一道题） ----------
def split_array(nums: List[int], k: int) -> int:
    return ship_within_days(nums, k)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("精确值  find_exact(1..7, 3) ->", find_exact(arr, 3))
    print("精确值  find_exact(1..7, 9) ->", find_exact(arr, 9))
    a = [1, 1, 2, 2, 2, 6, 7]
    print("首次出现 first_occurrence([1,1,2,2,2,6,7], 2) ->", first_occurrence(a, 2))
    print("末次出现 last_occurrence([1,1,2,2,2,6,7], 2)  ->", last_occurrence(a, 2))
    b = [1, 2, 5, 9, 12]
    print("最接近   closest([1,2,5,9,12], 4) -> 下标", closest(b, 4), "值", b[closest(b, 4)])
    print("最接近   closest([1,4,6], 2)      -> 值", [1, 4, 6][closest([1, 4, 6], 2)])
    for s in ["abcd", "abbaba", "aabcaabdaab", "aaaaa"]:
        print(f"1062 longest_repeating_substring({s!r}) ->", longest_repeating_substring(s))
    print("1011 ship_within_days([1..10], 5) ->", ship_within_days(list(range(1, 11)), 5))
    print("410  split_array([7,2,5,10,8], 2) ->", split_array([7, 2, 5, 10, 8], 2))
