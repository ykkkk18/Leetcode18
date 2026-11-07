"""第 5 集：栈 Stack —— 解题关键只有一条：定义好 stack 的含义"""
from typing import List


# ---------- 739. 每日温度 ----------
# stack 定义：array[i] 右边、比 array[i] 大的所有元素的下标（存下标才能算距离）
# 推论：栈是单调的；栈顶 = array[i] 右边最近的更大元素
# 方向：要看"右边"，所以从右往左遍历
def daily_temperatures(temps: List[int]) -> List[int]:
    n = len(temps)
    res = [0] * n
    stack = []                                   # Python 的 list 就能当栈用
    for i in range(n - 1, -1, -1):
        while stack and temps[stack[-1]] <= temps[i]:
            stack.pop()                          # 不比我大的，违反定义 -> 弹出
        res[i] = stack[-1] - i if stack else 0   # 栈空：右边没有更大的，答案 0
        stack.append(i)
    return res


# ---------- 735. 小行星碰撞 ----------
# stack 定义：到目前为止活下来的所有小行星；栈顶 = 左边离我最近的幸存者
def asteroid_collision(asteroids: List[int]) -> List[int]:
    stack = []
    for a in asteroids:
        if a > 0:                                # 向右飞：和左边任何东西都不会面对面相撞
            stack.append(a)
            continue
        # a < 0 向左飞：一直撞掉左边比自己小的、向右飞的
        while stack and stack[-1] > 0 and stack[-1] < -a:
            stack.pop()
        if stack and stack[-1] == -a:            # 一样大：同归于尽
            stack.pop()
        elif not stack or stack[-1] < 0:         # 栈空或栈顶也向左：我活下来
            stack.append(a)
        # 否则：栈顶更大，我被撞没
    return stack                                 # Python list 从底到顶就是原顺序


# ---------- 补充 20. 有效的括号（stack：还没配对的左括号） ----------
def is_valid(s: str) -> bool:
    pair = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pair:
            if not stack or stack.pop() != pair[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


# ---------- 补充 496. 下一个更大元素 I（739 的变形） ----------
def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    nxt, stack = {}, []
    for x in reversed(nums2):
        while stack and stack[-1] <= x:
            stack.pop()
        nxt[x] = stack[-1] if stack else -1
        stack.append(x)
    return [nxt[x] for x in nums1]


# ---------- 补充 84. 柱状图中最大的矩形（Hard，单调栈） ----------
# stack 定义：左边、高度严格小于当前柱子的下标（单调递增）
def largest_rectangle_area(heights: List[int]) -> int:
    stack, best = [], 0
    for i, h in enumerate(heights + [0]):        # 末尾补 0，把栈清空
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1    # 弹出后新栈顶是左边界
            best = max(best, height * (i - left - 1))
        stack.append(i)
    return best


if __name__ == "__main__":
    t = [73, 74, 75, 71, 69, 72, 76, 73]
    print("739 daily_temperatures", t, "->", daily_temperatures(t))
    for a in ([5, 10, -5], [8, -8], [10, 2, -5], [11, 8, 2, -5, -8, 3]):
        print("735 asteroid_collision", a, "->", asteroid_collision(a))
    print("20  is_valid('()[]{}') ->", is_valid("()[]{}"), "| is_valid('(]') ->", is_valid("(]"))
    print("496 next_greater_element([4,1,2],[1,3,4,2]) ->", next_greater_element([4, 1, 2], [1, 3, 4, 2]))
    print("84  largest_rectangle_area([2,1,5,6,2,3]) ->", largest_rectangle_area([2, 1, 5, 6, 2, 3]))
