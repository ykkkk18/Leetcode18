"""第 2 集：数组双指针（Two Pointers）"""
from typing import List


# ---------- 模板 1：同向双指针 ----------
# [0, i)   处理好、要保留的数据      （i 是"下一个可以填充的位置"）
# [i, j)   处理过、不需要的数据
# [j, n)   还没处理的数据
# 特点：保留元素的相对顺序
def same_direction_template(arr, keep):
    i = 0
    for j in range(len(arr)):        # while j < len(arr)
        if keep(arr, i, j):          # 需要 arr[j]
            arr[i] = arr[j]          # 填到 i 的位置
            i += 1                   # i 移到下一个可填充位置
        # 否则跳过 arr[j]，i 不动
    return i                         # [0, i) 是结果


# ---------- 模板 2：相向双指针 ----------
# [0, i) 和 (j, n-1] 都是处理好的数据，[i, j] 是待处理的数据
# 特点：不保证相对顺序；每轮至少移动一个指针，否则死循环
def opposite_direction_template(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        # 根据 arr[i] 和 arr[j] 决定做什么（交换 / 取较小值 ...）
        i += 1
        j -= 1


# ---------- 344. 反转字符串（相向） ----------
def reverse_string(s: List[str]) -> None:
    i, j = 0, len(s) - 1
    while i < j:                     # 写 i <= j 也对：中间元素和自己交换
        s[i], s[j] = s[j], s[i]      # 每一"层"交换首尾
        i += 1
        j -= 1


# ---------- 26. 删除有序数组中的重复项（同向） ----------
def remove_duplicates(nums: List[int]) -> int:
    i = 0
    for j in range(len(nums)):
        # i == 0：还没有处理好的数据，第一个元素一定要
        # 只需和已处理部分的最后一个元素 nums[i-1] 比较
        if i == 0 or nums[j] != nums[i - 1]:
            nums[i] = nums[j]
            i += 1
    return i                         # 新数组长度，nums[:i] 是去重结果


# ---------- 283. 移动零（同向，视频中用作"相对顺序"的例子） ----------
def move_zeroes(nums: List[int]) -> None:
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:             # 非 0 才保留，相对顺序不变
            nums[i] = nums[j]
            i += 1
    for k in range(i, len(nums)):    # 剩下的位置填 0
        nums[k] = 0


# ---------- 补充练习 11. 盛最多水的容器（相向） ----------
def max_area(height: List[int]) -> int:
    i, j, best = 0, len(height) - 1, 0
    while i < j:
        best = max(best, (j - i) * min(height[i], height[j]))
        if height[i] < height[j]:    # 移动较矮的一边才可能变大
            i += 1
        else:
            j -= 1
    return best


# ---------- 补充练习 167. 两数之和 II（有序数组，相向） ----------
def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    i, j = 0, len(numbers) - 1
    while i < j:
        s = numbers[i] + numbers[j]
        if s == target:
            return [i + 1, j + 1]    # 题目要求 1-based 下标
        if s < target:
            i += 1
        else:
            j -= 1
    return []


if __name__ == "__main__":
    s = list("hello"); reverse_string(s)
    print("344 reverse_string('hello') ->", "".join(s))
    s = list("Hannah"); reverse_string(s)
    print("344 reverse_string('Hannah') ->", "".join(s))

    nums = [1, 2, 2, 3, 5, 5]
    k = remove_duplicates(nums)
    print("26  remove_duplicates([1,2,2,3,5,5]) ->", k, nums[:k])

    nums = [1, 2, 0, 3, 0, 8]
    move_zeroes(nums)
    print("283 move_zeroes([1,2,0,3,0,8]) ->", nums)

    print("11  max_area([1,8,6,2,5,4,8,3,7]) ->", max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print("167 two_sum_sorted([2,7,11,15], 9) ->", two_sum_sorted([2, 7, 11, 15], 9))
