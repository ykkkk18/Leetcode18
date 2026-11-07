# LeetCode 刷题套路系列 · Python 学习笔记（合订本）

> 包含 7 天学习路径、18 集笔记（含全部代码和运行结果）、全系列总结。


---

# 7 天学习路径

> 视频总时长约 8.6 小时，平均每天约 70 分钟视频，加上 2～3 小时动手练习，**每天总共约 3～4 小时**。
> 顺序完全按照课程的编排：从数据结构到搜索，再到 DP，前面的内容是后面的基础，不建议打乱。

## 每天的固定流程

1. **看视频**（1～1.5 倍速），同时打开对应的笔记。
2. **运行代码**：`python code/epXX_xxx.py`，对照笔记中的"实际输出"，确认理解了每一行。
3. **默写模板**：合上笔记，在白纸或空文件里写出当天的模板，写不出来就回看。
4. **刷练习题**：先做视频里的例题，不看答案，再做"练习"列里的题。卡住 20 分钟就看题解，第二天再独立重做一遍。
5. **自测**：回答当天的自测问题，答不上来就回到笔记对应的小节。

## 总览

| 天 | 集数 | 主题 | 视频时长 | 当天要掌握的模板 |
| --- | --- | --- | --- | --- |
| Day 1 | 1、2、3 | 方法论 · 双指针 · 二分查找 | 约 57 分钟 | 同向/相向双指针；二分三模板 |
| Day 2 | 4、5、6 | 链表 · 栈 · 堆 | 约 72 分钟 | 快慢指针、递归反转；单调栈；Top K 堆 |
| Day 3 | 7、8、9 | 哈希表 · 树的 BFS · 树的 DFS | 约 78 分钟 | 哈希查找；BFS 层序；Bottom-up / Top-down |
| Day 4 | 10、11、12 | 图的 BFS · Dijkstra · 图的 DFS | 约 94 分钟 | 多源 BFS；最小堆最短路；连通块染色 |
| Day 5 | 13、14 | 搜索 → DP · 一维 DP | 约 66 分钟 | Top-down 搜索；DFS + 记忆化 |
| Day 6 | 15、16 | 二维 DP · 区间 DP | 约 66 分钟 | 矩阵 / LCS；按长度填表 |
| Day 7 | 17、18 + 复习 | 数组 + k · 回溯 · 总复习 | 约 61 分钟 | 切一刀 + k-1；记录 → 递归 → 回溯 |

---

## Day 1：打地基——方法论、双指针、二分查找

| 笔记 | 代码 |
| --- | --- |
| [01 刷题方法论](notes/01-刷题方法论.md) · [02 双指针](notes/02-双指针.md) · [03 二分查找](notes/03-二分查找.md) | `ep02_two_pointers.py` · `ep03_binary_search.py` |

- **例题**：344、26、283；二分的三个模板函数；1062（或者先做免费的同类题 1011）
- **练习**：11、167、27、977；34、35、69、410、1011
- **自测**：
  1. 同向双指针中 `i` 的含义是什么？为什么它能保持相对顺序？
  2. 二分查找的两大原则是什么？什么情况下 mid 必须偏右？
  3. 最长重复子串这道题，为什么能在"长度"上做二分？

## Day 2：线性结构——链表、栈、堆

| 笔记 | 代码 |
| --- | --- |
| [04 链表](notes/04-链表.md) · [05 栈](notes/05-栈.md) · [06 堆](notes/06-堆.md) | `ep04_linked_list.py` · `ep05_stack.py` · `ep06_heap.py` |

- **例题**：876、19、206；739、735；215、23
- **练习**：141、21、25；20、496、84；347、703、295
- **自测**：
  1. 链表的递归三部曲是什么？反转链表时哪两行的顺序不能颠倒？
  2. 739 题中栈的定义是什么？为什么要从右往左遍历？
  3. 为什么"大小为 k 的最小堆"的堆顶就是第 k 大？`>=` 能写成 `>` 吗？

## Day 3：查找与树——哈希表、树的 BFS 和 DFS

| 笔记 | 代码 |
| --- | --- |
| [07 哈希表](notes/07-哈希表.md) · [08 树的 BFS](notes/08-树的BFS.md) · [09 树的 DFS](notes/09-树的DFS.md) | `ep07_hashmap.py` · `ep08_tree_bfs.py` · `ep09_tree_dfs.py` |

- **例题**：1、560；102、104、199；104（DFS 版）、124、129
- **练习**：3、49、138；103、111；236、112、543
- **自测**：
  1. 560 题为什么要预存 `{0: 1}`？
  2. BFS 模板里为什么要先记下 size？
  3. 124 题中递归的返回值和全局答案分别代表什么？为什么不能把"人字形"路径返回给父结点？

## Day 4：图——BFS、Dijkstra、DFS

| 笔记 | 代码 |
| --- | --- |
| [10 图的 BFS](notes/10-图的BFS.md) · [11 Best-First Search](notes/11-图的BestFirstSearch.md) · [12 图的 DFS](notes/12-图的DFS.md) | `ep10_graph_bfs.py` · `ep11_best_first_search.py` · `ep12_graph_dfs.py` |

- **例题**：542、127；743、787；200、332
- **练习**：994、1091、934；1631；695、207、133
- **自测**：
  1. 图的 BFS 和树的 BFS 有哪两点不同？什么是多源 BFS？
  2. Dijkstra 为什么在"弹出时"查重，而不是"入堆时"？
  3. 332 题为什么必须用后序遍历？

> 这是视频最长的一天，如果时间不够，可以把 Day 4 的练习题挪到 Day 7 再做。

## Day 5：从搜索到 DP——搜索入门、一维 DP

| 笔记 | 代码 |
| --- | --- |
| [13 搜索与动态规划入门](notes/13-搜索与动态规划入门.md) · [14 一维动态规划](notes/14-一维动态规划.md) | `ep13_search_dp.py` · `ep14_dp_1d.py` |

- **例题**：78、139；96、91
- **练习**：46、70；198、322、140、300
- **自测**：
  1. 画出 `[1,3,4]` 求子集的搜索树。为什么到达叶子时要复制结果？
  2. 搜索和 DP 的模板差了哪两步？
  3. 96 题的关键观察是什么？为什么是"相乘"？
- **今天要做的一件事**：用 70 题亲手对比"纯搜索"和"记忆化"的运行时间，代码里已经写好了。

## Day 6：二维 DP——矩阵、双序列、区间

| 笔记 | 代码 |
| --- | --- |
| [15 二维动态规划入门](notes/15-二维动态规划入门.md) · [16 区间 DP](notes/16-二维动态规划进阶-区间DP.md) | `ep15_dp_2d.py` · `ep16_dp_interval.py` |

- **例题**：63、1143；877、5
- **练习**：62、64、718、72；486、516、647、312
- **自测**：
  1. 2D DP 的四种常见输入形式分别是什么？
  2. LCS 中两个字符不相等时，为什么不加 1？
  3. 区间 DP 的填表顺序是什么？为什么 DFS 写法可以不关心这个顺序？
  4. 最长回文子串里，只递归 `(i+1, j-1)` 会漏掉什么？

## Day 7：收尾与总复习——数组 + k、回溯

| 笔记 | 代码 |
| --- | --- |
| [17 数组加 k](notes/17-二维动态规划高级-数组加k.md) · [18 回溯](notes/18-回溯.md) · [全系列总结](notes/19-全系列总结.md) | `ep17_dp_array_k.py` · `ep18_backtracking.py` |

- **例题**：410、188；46、47
- **练习**：121、122、123、1011（用二分法再做一遍 410）；39、40、77、51
- **总复习（约 1.5 小时）**：
  1. 读[全系列总结](notes/19-全系列总结.md)的知识地图表，对每一行**口述**"看到什么想到它"和模板。
  2. 对照"易错点清单"，逐条回到代码里找出对应的那一行。
  3. 从 Day 1～6 中每天挑 1 道当时卡住的题，**限时 25 分钟**重做。
- **自测**：
  1. 410 题的 DP 状态和递推规则是什么？它的二分解法又是什么？
  2. 188 题为什么要有"继承"分支？
  3. 回溯的三步是什么？47 题的去重为什么要放在"同一层"？

---

## 7 天之后

- **巩固（第 2～3 周）**：每天 2～3 道新题，按专题轮换，可以从 Leetcode 仓库的 [INDEX.md](https://github.com/ykkkk18/leetcode/blob/main/INDEX.md) 里按标签挑题。
- **模拟面试**：讲者强调"能讲清楚思路"和"能做出来"同样重要。找朋友互相出题，或者对着录音口述：题意 → 暴力解 → 优化思路 → 复杂度 → 写代码。
- **间隔复习**：第 1、3、7、14 天各回顾一次当天的模板，默写一遍。


---

# 第 1 集：如何正确刷题——三大误区与刷题方法论

> 本集是整个系列的开篇，没有代码，讲的是"怎么刷"比"刷多少"更重要。

## 一、为什么方法比努力重要

讲者用自己健身受伤的经历类比：方法不对，练得越多伤得越重。刷题是纯脑力活动，更需要一套系统的方法论。方法错误的代价不只是浪费时间，更严重的是让人对刷题产生厌恶，最终半途而废。

## 二、三大刷题误区

| 误区 | 为什么错 | 正确做法 |
| --- | --- | --- |
| 1. 刷题可以短期突击 | 刷题是从基础到高阶的系统工程，地基不牢，上面堆多少砖都会塌 | 先打基础，制定长期、合理的计划 |
| 2. 只刷高频题就够了 | 高频题之所以高频，是因为它考察的知识点全面，很多是由经典题延伸出来的。只刷高频、甚至背题，遇到新题就无从下手 | 理解背后的算法知识点，掌握常见套路 |
| 3. 能解题就能拿下面试 | 面试官会追问思路。只会让代码"跑通"，却讲不清完整思路，同样会挂 | 能有逻辑地讲出思路、抓住面试官提示、优化算法；多和朋友做模拟面试（mock interview） |

## 三、刷题三步走

1. **掌握一门编程语言**
   讲者推荐 Java，理由是向面试官传递"编程基础扎实"的信号。
   *笔记说明：本笔记按你的需求统一使用 Python。Python 写算法题代码更短，国内外面试普遍接受；只要能讲清复杂度和底层数据结构（例如 `list`、`dict`、`heapq`、`deque` 的时间复杂度），一样能体现基础。*
2. **深入理解基础数据结构**
   这是正式刷题前的预备工作。只有理解了数据结构的特性，才能明白为什么某类题总用某种结构，也才能准确分析时间和空间复杂度。
3. **按算法模块系统刷题**
   不要按 Easy → Medium → Hard 随机刷，那样越刷越乱。应该按类别集中训练，比如这周专攻 BFS，下周专攻 HashMap，这样才能总结出套路，并发现不同题目之间的共性。

## 四、本系列的结构

每一集对应一个算法类别，包括三部分：
- **识别题型的特征**：看到什么样的题，就想到这个套路
- **解题模板**：把思路快速转成代码
- **经典例题与进阶练习**：用实践巩固知识点

系列覆盖的类别（第 2～18 集）：双指针 → 二分查找 → 链表 → 栈 → 堆 → 哈希表 → 树的 BFS/DFS → 图的 BFS / Best-First / DFS → 搜索与动态规划 → 一维/二维 DP → 回溯。

## 本集要点

- 方法 > 努力，刷题是"熟能生巧"的技术，不是玄学。
- 先打基础，再按模块刷题，最后用模拟面试练习表达。
- 心态：不焦虑，按教程顺序脚踏实地推进。


---

# 第 2 集：数组题型——双指针 Two Pointers

## 一、核心思想：两个指针把数组分成三块

### 1. 同向双指针（i、j 都从左往右走）

```
 [0, i)        [i, j)          [j, n)
 处理好·要的    处理过·不要的     还没处理
```

- `i` 的含义是**下一个可以填充的位置**，`i` 左边（不含 `i`）是结果。
- `j` 是扫描指针，每次看一个新元素。
- **重要特性**：处理后，保留下来的元素**相对顺序不变**。

### 2. 相向双指针（i 从左、j 从右，相向而行）

```
 [0, i)      [i, j]       (j, n-1]
 处理好       待处理        处理好
```

- 处理后**不保证相对顺序**。
- 每一轮**至少移动一个指针**，否则会死循环。

### 3. 区间开闭要统一

左闭右开还是左闭右闭可以按个人习惯，但**一个位置不能同时有两种含义**。比如 `i` 不能既属于"处理好要的"，又属于"处理过不要的"。

## 二、面试技巧：先澄清"相对顺序要不要保持"

例：把数组 `[1,2,0,3,0,8]` 里的 0 都挪到末尾。
- 要求非 0 元素保持原顺序（`1,2,3,8`），就只能用**同向**双指针。
- 不要求保持顺序，同向、相向都可以。

面试官通常不会主动说明，要**自己提出来问**。这正是在考察你有没有这个意识。

## 三、通用解题步骤

**同向：**
1. 初始化 `i = j = 0`
2. `while j < n`：
   - 需要 `arr[j]`：`arr[i] = arr[j]`，`i += 1`
   - 不需要：跳过，`i` 不动
   - `j += 1`
3. `[0, i)` 就是结果

**相向：**
1. 初始化 `i = 0, j = n - 1`（固定从两端开始）
2. `while i <= j`（或 `i < j`）：根据 `arr[i]` 和 `arr[j]` 决定做什么（交换、取较小值……），然后**至少移动一个指针**
3. 具体做什么要根据题意来定，靠多练才能融会贯通

## 四、例题

### 344. 反转字符串（相向）
要求原地修改，不能额外开数组。思路是逐层交换首尾：先交换最外层的 `h` 和 `o`，然后去掉首尾，向里走一层，再交换 `e` 和 `l`……直到两指针相遇。
- `while i < j` 和 `while i <= j` 都对：字符数为奇数时，中间元素和自己交换，等于没交换。

### 26. 删除有序数组中的重复项（同向）
数组已排序，所以重复元素一定挨在一起。去重后要保持从小到大，也就是保持相对顺序，所以用同向双指针。
- **关键点**：新元素只需要和**已处理部分的最后一个元素 `nums[i-1]`** 比较。因为 `i` 左边已经去重且有序，最后一个就是最大的。
- `i == 0` 时还没有任何结果，第一个元素一定保留。
- 返回 `i`，也就是新长度：`[0, i)` 共 `i` 个元素。

以 `[1,2,2,3,5,5]` 为例的手动推演：

| j | nums[j] | nums[i-1] | 操作 | 结果区 [0,i) |
| --- | --- | --- | --- | --- |
| 0 | 1 | 无 | 保留 | 1 |
| 1 | 2 | 1 | 保留 | 1 2 |
| 2 | 2 | 2 | 跳过 | 1 2 |
| 3 | 3 | 2 | 保留 | 1 2 3 |
| 4 | 5 | 3 | 保留 | 1 2 3 5 |
| 5 | 5 | 5 | 跳过 | 1 2 3 5 |

## 五、完整代码

视频中的模板和例题（344、26、283），加上两道补充练习（11、167）。视频结尾的练习题列表只在画面上出现、没有念出来，这两道是我补充的同类经典题：

```python
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
```

运行 `python ep02_two_pointers.py` 的实际输出：

```text
344 reverse_string('hello') -> olleh
344 reverse_string('Hannah') -> hannaH
26  remove_duplicates([1,2,2,3,5,5]) -> 4 [1, 2, 3, 5]
283 move_zeroes([1,2,0,3,0,8]) -> [1, 2, 3, 8, 0, 0]
11  max_area([1,8,6,2,5,4,8,3,7]) -> 49
167 two_sum_sorted([2,7,11,15], 9) -> [1, 2]
```

## 六、复杂度

所有例题都只扫描一遍：时间 O(n)，额外空间 O(1)。

## 本集要点
- 同向双指针保持相对顺序，相向双指针不保持。
- `i` 表示"下一个可以填充的位置"，`[0, i)` 是结果。
- 相向时每一轮至少移动一个指针。
- 面试时主动澄清是否需要保持相对顺序。


---

# 第 3 集：二分查找 Binary Search——两大原则、三大模板

## 一、定义

**二分查找是在"有序区间"内做 O(log n) 搜索的方法。**最常见的场景是排好序的数组，但"有序区间"不一定是数组本身，也可以是**答案的取值范围**，见第五节。

## 二、两大原则（最重要，也最容易疏忽）

1. **每次都要缩小搜索区间**：否则会死循环。
2. **每次缩小时不能排除潜在答案**：答案被排除后就再也找不回来了。

所有模板中边界写成 `mid`、`mid+1` 还是 `mid-1`，循环条件写成 `<=` 还是 `<`，都是从这两条原则推出来的。

## 三、mid 的写法

```python
mid = l + (r - l) // 2      # 推荐写法
mid = (l + r) // 2          # Java/C++ 中 l+r 可能超过 int 上限而溢出
```

Python 的整数不会溢出，但面试时写成第一种，能体现你知道这个细节。

## 四、三大模板

| 模板 | 用途 | 循环条件 | 缩小区间的方式 |
| --- | --- | --- | --- |
| 1. 精确值 | 找等于 k 的位置 | `l <= r` | `l = mid + 1` / `r = mid - 1` |
| 2. 模糊值 | 第一次/最后一次出现、比 k 大的最小值等 | `l < r` | `l = mid + 1, r = mid`，或 `l = mid, r = mid - 1` |
| 3. 万用型 | 最接近 k 的值等；前两种都能改写成这种 | `l < r - 1` | `l = mid` / `r = mid` |

### 为什么模板 1 不能找"最接近 4 的数"？

在 `[1,2,5,...]` 里找最接近 4 的数：先看到 5 > 4，往左走；再看到 2 < 4，往右走，最后停在 2。但 5 才是答案，它只差 1。模板 1 只适合找精确值。

### 模板 2：第一次出现（`l = mid + 1`, `r = mid`）

- `arr[mid] < k`：mid 不可能是答案，放心排除，`l = mid + 1`。
- `arr[mid] >= k`：mid **可能**就是第一次出现的位置。程序只看得到 mid 这一个值，不知道左边还有没有 k，所以**要往左找，但不能排除 mid**，即 `r = mid`。
- 为什么循环条件是 `l < r`？如果写 `l <= r`，当 `l == r == mid` 时，`r = mid` 等于什么都没做，下一轮还是一样，形成死循环，违背原则 1。

### 模板 2：最后一次出现（`l = mid`, `r = mid - 1`）

- 和上面对称，但 **mid 要偏右**：`mid = l + (r - l + 1) // 2`。
- 原因：区间只剩两个元素时，整数除法向下取整，mid 会落在左边那个上，`l = mid` 就没有移动，形成死循环。让 mid 偏右，就能保证每轮区间都缩小。

> 口诀：**出现 `l = mid` 就让 mid 偏右（+1）；出现 `r = mid` 就让 mid 偏左（默认写法）。**

### 模板 3：万用型（找最接近 k 的值）

循环在 `l`、`r` **相邻**时结束，最后留下两个候选，再分三种情况：
1. `arr[r] < k`：最大值都比 k 小，说明 k 在数组右边之外，返回 `r`。
2. `arr[l] > k`：最小值都比 k 大，说明 k 在数组左边之外，返回 `l`。
3. 否则 `arr[l] <= k <= arr[r]`：比较 `k - arr[l]` 和 `arr[r] - k`，返回更近的那个。

## 五、进阶：在"答案区间"上二分——1062. 最长重复子串

题意：找出至少出现两次的最长子串的长度。例如 `"abbaba"` 的答案是 2（`"ab"` 和 `"ba"` 都出现了两次）；`"aaaaa"` 的答案是 4，两次出现可以重叠。

- **暴力解法**：子串有 O(n²) 个，用哈希集合查重时比较字符串还要 O(n)，总共 O(n³)。
- **关键观察**：答案长度位于 `[0, n-1]` 区间内，而且是"有序"的。如果长度为 x 的重复子串存在，更短的一定也存在。
- 于是写一个辅助函数 `ok(x)` 判断长度 x 是否可行，再在 `[0, n-1]` 上二分：
  - `ok(mid)` 为真：mid 可能就是答案，但还想找更长的，所以 `l = mid`，mid 要偏右。
  - `ok(mid)` 为假：更长的也一定不行，`r = mid - 1`。
- 复杂度：O(log n) 轮，每轮 `ok` 约 O(n²)（切片 + 哈希），总共 O(n² log n)，比 O(n³) 快。

**讲者提示**：谷歌很喜欢这一类题，它们都是这个思路换了个马甲。典型题目有 410. 分割数组的最大值、1011. 在 D 天内送达包裹的能力、1231. 分享巧克力。代码里附上了 1011 和 410 的解法，它们的写法完全相同。

## 六、完整代码

```python
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
```

运行 `python ep03_binary_search.py` 的实际输出：

```text
精确值  find_exact(1..7, 3) -> 2
精确值  find_exact(1..7, 9) -> -1
首次出现 first_occurrence([1,1,2,2,2,6,7], 2) -> 2
末次出现 last_occurrence([1,1,2,2,2,6,7], 2)  -> 4
最接近   closest([1,2,5,9,12], 4) -> 下标 2 值 5
最接近   closest([1,4,6], 2)      -> 值 1
1062 longest_repeating_substring('abcd') -> 0
1062 longest_repeating_substring('abbaba') -> 2
1062 longest_repeating_substring('aabcaabdaab') -> 3
1062 longest_repeating_substring('aaaaa') -> 4
1011 ship_within_days([1..10], 5) -> 15
410  split_array([7,2,5,10,8], 2) -> 18
```

## 本集要点
- 二分查找有两大原则：**每次缩小区间**、**不排除潜在答案**。
- 三大模板：精确值用 `<=`；模糊值用 `<`；万用型用 `< r-1`，最后再比较两个候选。
- 出现 `l = mid` 时，mid 要偏右。
- "有序区间"也可以是答案的取值范围，配合一个判断可行性的函数使用。


---

# 第 4 集：链表 Linked List——双指针与递归两大套路

## 一、链表 vs 数组

| 操作 | 数组 Array | 单链表 Linked List |
| --- | --- | --- |
| 内存 | 连续 | 不一定连续，每个结点存 `val` 和 `next` |
| 按位置访问 | O(1)，用下标访问 | O(n)，只能从 head 一个个往后走 |
| 末尾添加 | 均摊 O(1)，因为需要扩容 | O(n)，要先走到尾巴；新建结点本身是 O(1) |
| 删除 | O(n)，后面的元素都要前移 | O(n)，要先找到位置 |

单链表只能拿到头结点 `head`，**没有下标，也不能从后往前走**。所以操作链表只能靠指针，这就引出了两大套路。

## 二、套路一：双指针（能解决约 60% 的链表题）

链表的双指针**一定是同向的**，因为没法从尾巴往回走。每道题只要定义好两件事：
1. **两个指针隔开多远？**
2. **各自的移动速度是多少？**

### 例 1：876. 找中间结点（一快一慢）
- `i`、`j` 都从 head 出发；`j` 每次走 2 步，`i` 每次走 1 步。
- `j` 走到末尾时走了 n 步，`i` 刚好走了 n/2 步，正好在中点。
- 暴力做法是先走一遍求长度，再走 n/2 步。时间复杂度同为 O(n)，但要遍历两遍；快慢指针只需一遍。
- 循环条件 `while j and j.next`：因为要做两次 `.next`，两次都必须保证不会访问到空结点。

### 例 2：倒数第 k 个结点（先隔开，再同速）
- 先让 `j` 走 k 步，和 `i` 拉开距离 k。
- 两者同速前进，直到 `j` 走出链表，此时 `i` 就在倒数第 k 个结点。原因是 `j` 到达位置 n 时，`i` 在位置 n-k。
- LeetCode 19 题要求**删除**倒数第 n 个结点。代码里加了一个哑结点，让 `i` 停在待删结点的前一个，方便删除。

## 三、套路二：自底向上递归 Bottom-up Recursion

面试官常在简单题上**故意考递归**，比如反转链表。递归的调用栈是"先进后出"的，正好可以模拟"从后往前"处理链表，弥补链表不能倒着走的缺点。

**三部曲：**
1. **向子问题要答案**：调用下一层递归。
2. **在当前层做点事**：根据题意决定。
3. **返回本层的结果**。

注意：第 1 步拿到的值，就是下一层第 3 步返回的值，**两者含义必须相同**。

**最重要的一点：要相信你的递归函数是对的。**把后面的子链表当成已经处理好的黑盒，只关心当前这一层要做什么。

### 例 3：206. 反转链表（递归）
反转的是**箭头（引用）**，不是交换结点里的值。

假设当前在结点 3，后面的 `4→5` 已经反转成 `5→4`，现在 4 是这段的尾巴，3 仍然指向 4：
1. `head.next.next = head`：让 4 指回 3。
2. `head.next = None`：断开 3 指向 4 的旧箭头。
3. 返回新的头，也就是原来的尾巴 5。它在最底层产生，然后被一路原样返回上来。

- **base case**：`head is None`（输入就是空表）或 `head.next is None`（到达尾巴）。
- **两行顺序不能反**：如果先断开 `head.next`，就再也找不到下一个结点了。

## 四、完整代码

包括视频中的三道例题（876、19、206），以及补充练习：141 环形链表、21 合并有序链表、25 K 个一组翻转链表。视频提到练习题里"只有一道 Hard"，链表专题最经典的 Hard 就是 25 题，它用的正是递归三部曲。

```python
"""第 4 集：链表 Linked List —— 快慢双指针 + 自底向上递归"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(vals):                       # [1,2,3] -> 1->2->3
    dummy = cur = ListNode()
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):                     # 1->2->3 -> [1,2,3]
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


# ========== 套路一：双指针（同向；定义好"间隔多少"和"各自速度"） ==========

# 876. 链表的中间结点：快指针每次 2 步，慢指针每次 1 步
def middle_node(head: ListNode) -> ListNode:
    i = j = head
    while j and j.next:                # 两次 .next 都不能踩到 None
        i = i.next
        j = j.next.next
    return i                           # 偶数个结点时返回靠后的中点


# 19 的核心：倒数第 k 个结点。先让 j 领先 k 步，再同速前进，j 出界时 i 就是答案
def kth_from_end(head: ListNode, k: int) -> ListNode:
    i = j = head
    for _ in range(k):
        j = j.next
    while j:
        i = i.next
        j = j.next
    return i


# 19. 删除链表的倒数第 N 个结点：加一个哑结点，让 i 停在"待删结点的前一个"
def remove_nth_from_end(head: ListNode, n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    i = j = dummy
    for _ in range(n + 1):
        j = j.next
    while j:
        i, j = i.next, j.next
    i.next = i.next.next
    return dummy.next


# 补充 141. 环形链表：快慢指针，有环必相遇
def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False


# ========== 套路二：自底向上递归（Bottom-up Recursion）三部曲 ==========
# 1. 向子问题要答案   2. 在当前层做点事   3. 返回本层答案（含义必须和第 1 步一致）
# 要"相信"递归函数是对的：把后面的子链表当成已经处理好的黑盒

# 206. 反转链表
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:      # base case：空表 / 已到尾巴
        return head
    new_head = reverse_list(head.next)         # 1. 后面已经反转好了，new_head 是原来的尾巴
    head.next.next = head                      # 2. 让后一个结点指回自己
    head.next = None                           #    再断开自己指向后一个的箭头（两行顺序不能反）
    return new_head                            # 3. 一路把新头返回上去


# 迭代版 206（面试官常让你两种都写）
def reverse_list_iter(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev


# 补充 21. 合并两个有序链表（递归三部曲）
def merge_two_lists(a, b):
    if not a or not b:
        return a or b
    if a.val <= b.val:
        a.next = merge_two_lists(a.next, b)
        return a
    b.next = merge_two_lists(a, b.next)
    return b


# 补充 25. K 个一组翻转链表（Hard，同样是递归三部曲）
def reverse_k_group(head, k):
    node, cnt = head, 0
    while node and cnt < k:                    # 不足 k 个就保持原样
        node, cnt = node.next, cnt + 1
    if cnt < k:
        return head
    rest = reverse_k_group(node, k)            # 1. 后面的先翻好
    prev, cur = rest, head                     # 2. 翻转当前这 k 个，尾巴接到 rest
    for _ in range(k):
        cur.next, prev, cur = prev, cur, cur.next
    return prev                                # 3. 返回本组新头


if __name__ == "__main__":
    print("876 middle_node([1,2,3,4,5])   ->", middle_node(build([1, 2, 3, 4, 5])).val)
    print("876 middle_node([1,2,3,4,5,6]) ->", middle_node(build([1, 2, 3, 4, 5, 6])).val)
    print("倒数第2个 kth_from_end([1,2,3,4,5], 2) ->", kth_from_end(build([1, 2, 3, 4, 5]), 2).val)
    print("19  remove_nth_from_end([1,2,3,4,5], 2) ->", to_list(remove_nth_from_end(build([1, 2, 3, 4, 5]), 2)))
    c = build([3, 2, 0, -4]); c.next.next.next.next = c.next
    print("141 has_cycle(3->2->0->-4->回到2) ->", has_cycle(c), "| 无环 [1,2] ->", has_cycle(build([1, 2])))
    print("206 reverse_list([1,2,3,4,5])      ->", to_list(reverse_list(build([1, 2, 3, 4, 5]))))
    print("206 reverse_list_iter([1,2,3,4,5]) ->", to_list(reverse_list_iter(build([1, 2, 3, 4, 5]))))
    print("21  merge_two_lists([1,2,4],[1,3,4]) ->", to_list(merge_two_lists(build([1, 2, 4]), build([1, 3, 4]))))
    print("25  reverse_k_group([1,2,3,4,5], 2) ->", to_list(reverse_k_group(build([1, 2, 3, 4, 5]), 2)))
    print("25  reverse_k_group([1,2,3,4,5], 3) ->", to_list(reverse_k_group(build([1, 2, 3, 4, 5]), 3)))
```

运行 `python ep04_linked_list.py` 的实际输出：

```text
876 middle_node([1,2,3,4,5])   -> 3
876 middle_node([1,2,3,4,5,6]) -> 4
倒数第2个 kth_from_end([1,2,3,4,5], 2) -> 4
19  remove_nth_from_end([1,2,3,4,5], 2) -> [1, 2, 3, 5]
141 has_cycle(3->2->0->-4->回到2) -> True | 无环 [1,2] -> False
206 reverse_list([1,2,3,4,5])      -> [5, 4, 3, 2, 1]
206 reverse_list_iter([1,2,3,4,5]) -> [5, 4, 3, 2, 1]
21  merge_two_lists([1,2,4],[1,3,4]) -> [1, 1, 2, 3, 4, 4]
25  reverse_k_group([1,2,3,4,5], 2) -> [2, 1, 4, 3, 5]
25  reverse_k_group([1,2,3,4,5], 3) -> [3, 2, 1, 4, 5]
```

## 五、复杂度
- 双指针类：时间 O(n)，空间 O(1)。
- 递归反转：时间 O(n)，空间 O(n)，来自递归调用栈；迭代版空间 O(1)。面试时最好两种写法都会，并能说出这个区别。

## 本集要点
- 链表双指针一定同向，只需定义好**间隔**和**速度**。
- 自底向上递归三部曲：向子问题要答案 → 做当前层的事 → 返回结果。
- 相信递归函数是对的；反转链表时，先让后一个结点指回自己，再断开旧箭头。


---

# 第 5 集：栈 Stack——定义好栈的含义

## 一、栈的特性与适用场景

- **后进先出（LIFO）**：出栈顺序和入栈顺序相反。
- **适用场景：需要记录之前的状态**。可以借助栈回到过去的状态，或者利用之前的值计算当前问题的答案。
- 限制：不能用下标访问，每次只能拿到栈顶元素。

### 栈 vs 动态规划（DP）

| | 栈 | 动态规划 |
| --- | --- | --- |
| 访问方式 | 每次只能拿栈顶 | 随时访问任意子问题，用数组或哈希表实现 O(1) 查表 |
| 每个状态被使用的次数 | 入栈一次、出栈一次，O(1) 次 | 可能被反复使用 |
| 难度 | 简单得多 | 最难的专题，见第 13～17 集 |

计算机里的**调用栈（call stack）**也是栈：递归进入下一层时保存当前函数的状态，返回时取出状态，继续执行。

## 二、解题关键：只需记住一点

> **定义好 stack 的含义。**题目问什么，就按什么来定义。

定义好之后，**单调性、栈顶的含义、遍历方向**都可以从定义推出来。所以面试时最重要的是把栈的物理含义讲清楚。

## 三、例题

### 739. 每日温度
对每一天，求还要等几天才会出现更高的温度。

- **定义**：栈里存 `array[i]` **右边**、比 `array[i]` 大的所有元素的**下标**。存下标是因为要计算天数差，演示时为了直观才写成温度值。
- **推论 1**：栈是单调的。
- **推论 2**：栈顶就是右边**最近**的更大元素，也就是答案。
- **推论 3**：要看的是"右边"，而栈是倒序的，所以**从右往左遍历**。这样右边的元素先入栈，站在 `i` 往栈里看，看到的就是右边。

**面试时讲清这四步：**
1. 初始化栈。
2. 从右往左遍历每个 `array[i]`。
3. 不断弹出，直到栈为空或栈顶大于 `array[i]`。
4. 栈为空则答案为 0，否则答案为 `栈顶下标 - i`；然后把 `i` 入栈。

以 `[73,74,75,71,69,72,76,73]` 为例：遍历到 75 时，左边的 71、72 都比它小，先被弹出，栈顶变成 76，两者相差 4 天，所以 75 的答案是 4。

### 735. 小行星碰撞
数值大小代表质量，正数向右飞，负数向左飞。相撞时小的消失，一样大则同归于尽。

- 光看到某个位置为止，是不知道前面的小行星能不能活下来的，必须回头看，所以要用栈。每颗星只会被回头看一次（要么活、要么死），用栈就够了，不需要 DP。
- **定义**：栈里是**到目前为止活下来的所有小行星**；栈顶是左边离当前最近的幸存者。
- **当前值为正（向右飞）**：直接入栈。
  - 栈顶为正：同向，永远不会相撞。
  - 栈顶为负：栈顶在左边且向左飞，当前在右边且向右飞，两者**背靠背**越飞越远。这一点比较隐晦。
- **当前值为负**：不断撞掉栈顶上**向右飞且比自己小**的，直到栈为空、栈顶也向左飞，或者栈顶比自己大。
  - 和栈顶一样大：弹出栈顶，自己也不入栈。
  - 栈为空或栈顶为负：自己活下来，入栈。
- Java 中需要把栈倒序取出才能得到原顺序；Python 的 `list` 从栈底到栈顶就是原顺序，直接返回即可。

## 四、复杂度：别被 for 里的 while 骗了

看到 for 循环里套着 while 就说 O(n²) 是错的。从全局看：**每个元素最多入栈一次、出栈一次**，所以总共是 O(n)。

## 五、完整代码

除了视频例题 739 和 735，还补充了三道经典栈题：20 有效括号、496 下一个更大元素、84 柱状图最大矩形（Hard）。视频说练习题"每道的定义都不太一样，是很好的练习"，这几道正好体现了这一点。

```python
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
```

运行 `python ep05_stack.py` 的实际输出：

```text
739 daily_temperatures [73, 74, 75, 71, 69, 72, 76, 73] -> [1, 1, 4, 2, 1, 1, 0, 0]
735 asteroid_collision [5, 10, -5] -> [5, 10]
735 asteroid_collision [8, -8] -> []
735 asteroid_collision [10, 2, -5] -> [10]
735 asteroid_collision [11, 8, 2, -5, -8, 3] -> [11, 3]
20  is_valid('()[]{}') -> True | is_valid('(]') -> False
496 next_greater_element([4,1,2],[1,3,4,2]) -> [-1, 3, -1]
84  largest_rectangle_area([2,1,5,6,2,3]) -> 10
```

## 本集要点
- 栈的核心用途：记录之前的状态，每个状态只用一次。
- **解题关键：定义好栈的含义**，单调性、栈顶含义和遍历方向都从定义推出。
- 找"右边"的东西就从右往左遍历；栈里存下标才能计算距离。
- 每个元素最多入栈、出栈各一次，复杂度是 O(n)。


---

# 第 6 集：堆 Heap——Top K 问题与多路归并

## 一、堆是什么

- 本质是**用数组实现的完全二叉树**。
- 根结点（堆顶）是全堆最大值（**最大堆 max heap**）或最小值（**最小堆 min heap**）。
- 只保证"父结点 ≥ 子结点"（或 ≤）。**同一个父结点的两个孩子之间没有大小关系**，所以堆只关心堆顶。

| 操作 | 含义 | 时间 | Python |
| --- | --- | --- | --- |
| peek | 查看堆顶 | O(1) | `heap[0]` |
| poll | 取出堆顶并重新调整堆 | O(log n) | `heapq.heappop(heap)` |
| offer | 加入元素 | O(log n) | `heapq.heappush(heap, x)` |
| heapify | 把数组原地变成堆 | **O(n)** | `heapq.heapify(arr)` |

> Python 的 `heapq` **只有最小堆**。需要最大堆时，存入相反数 `-x`。

## 二、在线算法 vs 离线算法

- **在线算法（online）**：处理**数据流**，长度未知，可以随时加入新数据，堆就是这样。
- **离线算法（offline）**：针对**固定长度**的数据，比如排序。数据从 n 个变成 2n 个时，需要全部重新排序。
- 这就是堆和排序的本质区别。本集的两个例子都是在线算法。

## 三、例 1：215. 数组中的第 K 个最大元素（Top K 问题）

> **看到 Top K，基本就用堆。**这个套路一定要记住。

注意：题目要的是排序后的第 k 个，**不是第 k 个不同的值**。在 `[3,2,1,5,6,4,5]` 中，第 4 大是 4，两个 5 各算一次。

| 方法 | 做法 | 时间 |
| --- | --- | --- |
| 排序 | 排序后取倒数第 k 个 | O(n log n) |
| 最大堆 | 原地 heapify，再弹出 k 次 | O(n + k log n) |
| **大小为 k 的最小堆** | 见下文 | **O(n log k)**，在线算法 |

### 大小为 k 的最小堆：三步

1. 初始化一个最小堆，**大小始终保持为 k**。
2. 对每个元素 x：如果堆的元素不足 k 个，**或者 x ≥ 堆顶**，就加入堆；加入后若超过 k 个，就弹出堆顶。
3. 最后**堆顶就是第 k 大**。

**为什么堆顶是第 k 大？**每次加入的都是比堆顶大的数，所以最后堆顶是堆里 k 个数中**最小的**，但它比数组里其他所有数都**大**。堆顶就像一条**分水岭**：堆里的 k-1 个数都比它大，堆外的数都比它小，所以它正好是第 k 大。

- 写 `>=` 而不是 `>`：写 `>` 的话，重复元素只算一次，就变成了"第 k 个不同的值"。
- 反过来求**第 k 小**：改用**最大堆**，比堆顶小的才加入。
- 想要整个 Top K 列表：最后堆里的所有元素就是答案。从最小堆依次弹出的顺序是从小到大，需要从大到小时反转一下。
- **在线特性**：每处理一个元素，堆顶就是"到目前为止"的第 k 大，所以能直接处理数据流（703 题）。

**手动推演**：视频中的例子是 `[3,2,3,1,2,4,1,5,5]`，k = 4。
- 前 4 个数 3、2、3、1 直接入堆，堆顶为 1。
- 遇到 2：2 ≥ 1，入堆后有 5 个，弹出 1，堆变为 {2,2,3,3}。
- 遇到 4：入堆后弹出 2，堆变为 {2,3,3,4}。
- 遇到 1：1 < 2，跳过。
- 遇到 5：入堆后弹出 2，堆变为 {3,3,4,5}。
- 遇到最后一个 5：入堆后弹出 3，堆变为 {3,4,5,5}。
- 最终堆顶为 **3**，就是答案。

> 补充：这道题还有快速选择（Quick Select）算法，平均 O(n)，但最坏 O(n²)，写起来难，而且是离线算法，不能处理数据流。面试时把堆的方法讲清楚就够了。

## 四、例 2：23. 合并 K 个升序链表

- **先看简化版**：合并 2 个有序链表（归并排序的合并步骤），用双指针，**谁小移谁**，复杂度 O(m+n)。相等时移动哪个都行，但要保持一致。
- **合并 k 个**：需要 k 个指针，每次找出 k 个里最小的。

| 每次找最小值的方法 | 时间 |
| --- | --- |
| 线性扫描 | O(k) |
| 排序 | O(k log k) |
| **最小堆** | **O(log k)** |

**为什么堆合适？**每次只移动**一个**指针：弹出一个，再加入它的下一个。堆只需 O(log k) 就能动态找到新的最小值。

**两步：**
1. 用 **k 个链表的头结点**初始化最小堆。注意不是空堆。
2. 当堆不为空时：弹出堆顶（当前最小），接到答案链表上；如果它还有 `next`，把 `next` 放进堆。

- 时间复杂度 O(N log k)，N 是结点总数。每个结点最多进、出堆各一次，堆的大小不超过 k。
- 链表不知道长度，可以看作数据流，所以这也是在线算法。
- Python 细节：`ListNode` 之间不能比较大小，堆里存 `(val, 链表编号, node)`，用编号打破平局。

## 五、完整代码

除了视频例题 215 和 23，还补上了视频推荐的同类题：347 前 K 个高频元素、703 数据流中的第 K 大元素、295 数据流的中位数。讲者特别推荐 295，认为它是一道很好的题。

```python
"""第 6 集：堆 Heap —— Top K 套路 + 多路归并（Python 用 heapq，默认是最小堆）"""
import heapq
from collections import Counter
from typing import List, Optional


# ---------- 215. 数组中的第 K 个最大元素 ----------
# 方法 1：排序  O(n log n)
def kth_largest_sort(nums: List[int], k: int) -> int:
    return sorted(nums)[-k]


# 方法 2：最大堆，原地 heapify O(n) + 弹出 k 次 O(k log n)
# heapq 只有最小堆，存相反数来模拟最大堆
def kth_largest_maxheap(nums: List[int], k: int) -> int:
    h = [-x for x in nums]
    heapq.heapify(h)
    for _ in range(k - 1):
        heapq.heappop(h)
    return -h[0]


# 方法 3（Top K 标准套路）：维护大小为 k 的最小堆  O(n log k)，在线算法
def kth_largest(nums: List[int], k: int) -> int:
    heap = []
    for x in nums:
        if len(heap) < k or x >= heap[0]:   # 写 >= 而不是 >：重复元素也要算
            heapq.heappush(heap, x)
            if len(heap) > k:               # 超过 k 个就踢掉堆顶（最小的）
                heapq.heappop(heap)
    return heap[0]                          # 堆顶 = 分水岭 = 第 k 大


# 703. 数据流中的第 K 大元素：同一个套路的"在线"版本
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k, self.heap = k, []
        for x in nums:
            self.add(x)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# 347. 前 K 个高频元素：Top K 套路，比较的是出现次数
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    heap = []
    for num, cnt in Counter(nums).items():
        heapq.heappush(heap, (cnt, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for cnt, num in sorted(heap, reverse=True)]


# ---------- 23. 合并 K 个升序链表 ----------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build(vals):
    dummy = cur = ListNode()
    for v in vals:
        cur.next = ListNode(v); cur = cur.next
    return dummy.next


def to_list(h):
    out = []
    while h:
        out.append(h.val); h = h.next
    return out


# k 个指针，每次取出 k 个里最小的：最小堆每次只 O(log k)
def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for idx, node in enumerate(lists):        # 先放入每条链表的头
        if node:
            heapq.heappush(heap, (node.val, idx, node))   # idx 用来打破平局（ListNode 不能比较）
    dummy = cur = ListNode()
    while heap:
        val, idx, node = heapq.heappop(heap)  # 当前 k 个里最小的
        cur.next = node; cur = cur.next       # 接到答案上
        if node.next:                         # 这条链表还没走完，把下一个放进堆
            heapq.heappush(heap, (node.next.val, idx, node.next))
    return dummy.next


# ---------- 295. 数据流的中位数（视频推荐的好题：两个堆） ----------
class MedianFinder:
    def __init__(self):
        self.small = []   # 最大堆（存相反数）：较小的一半
        self.large = []   # 最小堆：较大的一半

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))   # 保证 small 都 <= large
        if len(self.large) > len(self.small):                    # 保证 small 不少于 large
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2


if __name__ == "__main__":
    a = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    print("215 第4大", a, "-> 排序:", kth_largest_sort(a, 4),
          "最大堆:", kth_largest_maxheap(a, 4), "大小为k的最小堆:", kth_largest(a, 4))
    print("215 kth_largest([3,2,1,5,6,4], 2) ->", kth_largest([3, 2, 1, 5, 6, 4], 2))
    v = [3, 2, 3, 1, 2, 4, 1, 5, 5]      # 视频里手动推演的例子
    print("215 视频例子 kth_largest([3,2,3,1,2,4,1,5,5], 4) ->", kth_largest(v, 4))
    s = KthLargest(3, [4, 5, 8, 2])
    print("703 KthLargest(3,[4,5,8,2]) 依次 add 3,5,10,9,4 ->", [s.add(v) for v in (3, 5, 10, 9, 4)])
    print("347 top_k_frequent([1,1,1,2,2,3], 2) ->", top_k_frequent([1, 1, 1, 2, 2, 3], 2))
    lists = [build([1, 4, 5]), build([1, 3, 4]), build([2, 6])]
    print("23  merge_k_lists([1,4,5],[1,3,4],[2,6]) ->", to_list(merge_k_lists(lists)))
    mf, out = MedianFinder(), []
    for v in (5, 15, 1, 3):
        mf.addNum(v); out.append(mf.findMedian())
    print("295 依次加入 5,15,1,3 时的中位数 ->", out)
```

运行 `python ep06_heap.py` 的实际输出：

```text
215 第4大 [3, 2, 3, 1, 2, 4, 5, 5, 6] -> 排序: 4 最大堆: 4 大小为k的最小堆: 4
215 kth_largest([3,2,1,5,6,4], 2) -> 5
215 视频例子 kth_largest([3,2,3,1,2,4,1,5,5], 4) -> 3
703 KthLargest(3,[4,5,8,2]) 依次 add 3,5,10,9,4 -> [4, 5, 5, 8, 8]
347 top_k_frequent([1,1,1,2,2,3], 2) -> [1, 2]
23  merge_k_lists([1,4,5],[1,3,4],[2,6]) -> [1, 1, 2, 3, 4, 4, 5, 6]
295 依次加入 5,15,1,3 时的中位数 -> [5.0, 10.0, 5.0, 4.0]
```

## 本集要点
- 堆只关心堆顶；push、pop 是 O(log n)，heapify 是 O(n)。
- **Top K → 大小为 k 的堆**：求第 k 大用最小堆，求第 k 小用最大堆；堆顶就是分水岭。
- 多路归并：k 个指针，每次只移动一个，用最小堆在 O(log k) 内找到下一个最小值。
- 堆是在线算法，可以处理数据流；排序是离线算法。


---

# 第 7 集：哈希表 HashMap——用空间换查找速度

## 一、哈希表是什么

- 平均 **O(1)** 时间完成增、删、查的数据结构。
- Java 的 HashMap 用"数组 + 链表"实现，这种冲突处理方式叫拉链法（separate chaining）；另一种方式是开放寻址（open addressing）。
- 存进去的对象要能**判断相等、计算哈希值**。Java 需要实现 `equals` 和 `hashCode`，Python 对应 `__eq__` 和 `__hash__`。否则两个内容相同的对象，会因为内存地址不同而被当成不同的 key。
- **key 没有顺序**：按 1、2、3 插入，遍历出来的顺序不一定是 1、2、3。

### 家族成员

| Java | 特点 | Python 对应 |
| --- | --- | --- |
| HashMap | 无序，O(1) | `dict`，3.7 起保持插入顺序 |
| LinkedHashMap | 按插入顺序遍历，内部多维护一条双向链表 | `dict` / `collections.OrderedDict` |
| TreeMap | 按 key 从小到大遍历，用红黑树（平衡二叉树）实现，O(log n) | 标准库没有，可以用 `sortedcontainers.SortedDict`，或 `bisect` 加有序列表 |
| HashSet | 只有 key、没有 value 的 map | `set` |

## 二、什么时候用哈希表？

> **需要快速查找数据时，用哈希表加速查找。**

和数组比：数组**不能快速按值查找**，但有序、开销小，按下标访问比按 key 访问哈希表快得多。所以**不需要时就别用哈希表**。

## 三、例 1：1. 两数之和

- **暴力**：两层循环找 `x + y == target`，O(n²)。
- **优化思路**：对每个 x，要找的是 `target - x` 是否出现过，这就是"快速查找"。
  - 查找对象：**目前见过的值 → 它的下标**。
  - 对每个 x：如果 `target - x` 在表里，就找到了答案；否则把 `x → 下标` 存进表里。
  - 时间 O(n)，空间 O(n)。

**手动推演** `[2,15,9,7]`，target = 9：

| 当前 x | 要找 9-x | 表里有吗 | 表的内容（之后） |
| --- | --- | --- | --- |
| 2 | 7 | 无 | {2:0} |
| 15 | -6 | 无 | {2:0, 15:1} |
| 9 | 0 | 无（9 自己不算，必须是两个数） | {2:0, 15:1, 9:2} |
| 7 | 2 | **有，下标 0** | 返回 [0, 3] |

- **另一种思路（复习第 2 集）**：排序后用相向双指针。和太大就左移 j，和太小就右移 i。但排序后**原下标就乱了**，所以只适合返回"值"的版本，而且排序本身是 O(n log n)。

## 四、例 2：560. 和为 K 的子数组

- **关键变换**：任何子数组的和 = `前缀和(0..x) - 前缀和(0..y)`。
- 查找对象：**到当前位置为止所有出现过的前缀和 → 出现次数**。
- 对当前前缀和 `s`：如果 `s - k` 在表里出现过 c 次，就有 c 个以当前位置结尾、和为 k 的子数组，`res += c`。
- **最容易漏的一点**：表里要**预先存入 `{0: 1}`**。例如 `[1]`、k = 1：当前前缀和是 1，要找的 `1 - 1 = 0` 必须已经在表里，否则会把答案错算成 0。这个 0 代表"从开头到当前位置的整段"。
- 视频手动推演了 `[3,4,7,2,-3,1,4,2]`、k = 7，答案为 4，代码中有验证。

**步骤：**
1. 初始化哈希表为 `{0: 1}`，`sum = 0`，`res = 0`。
2. 对每个 x：`sum += x`；如果 `sum - k` 在表里，`res += 表[sum - k]`（加的是出现**次数**）；然后把 `sum` 的次数加 1。

## 五、完整代码

包括视频例题 1、560，以及讲者推荐的练习：3 无重复字符的最长子串、49 字母异位词分组、138 随机链表的复制。讲者特别提到 138 题"非常有意思，请务必做一下"。

```python
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
```

运行 `python ep07_hashmap.py` 的实际输出：

```text
1   two_sum_brute([2,15,9,7], 9) -> [0, 3]
1   two_sum([2,15,9,7], 9)       -> [0, 3]
    two_sum_values([2,15,9,7], 16) -> [7, 9]
560 subarray_sum([1,1,1], 2) -> 2
560 subarray_sum([1], 1)     -> 1 (若不预存 0:1 会错算成 0)
560 视频例子 subarray_sum([3,4,7,2,-3,1,4,2], 7) -> 4
3   length_of_longest_substring('abcabcbb') -> 3
49  group_anagrams(['eat','tea','tan','ate','nat','bat']) -> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
138 copy_random_list(7->13, 13.random=7) -> 新链表 7 -> 13 | 13.random = 7 | 是新结点: True
```

## 本集要点
- **需要快速查找时，用哈希表**，O(n) 查找变成 O(1)。
- 解题关键是想清楚**查找对象是什么**（key 存什么、value 存什么）：两数之和存"值 → 下标"，子数组和存"前缀和 → 次数"。
- 前缀和题记得预存 `{0: 1}`。
- 哈希表无序；需要顺序时用 LinkedHashMap，需要排序时用 TreeMap。


---

# 第 8 集：树 Tree 的广度优先搜索 BFS

> 学习顺序：树比图简单，BFS 比 DFS 简单，所以先学树的 BFS，循序渐进。

## 一、树的基本概念

- 和链表一样，是由引用串起来的数据，内存不一定连续。区别在于链表一个结点只连一个，树的一个结点可以连多个。
- **父结点 parent / 子结点 child** 是相对的概念：12 是 7 的父结点，同时又是 2 的子结点。
- 树可以看作一种特殊的**无环无向图**，只有**一个入口：root**。
- **99% 的题目是没有父指针的二叉树**，所以只能从上往下走。

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
```

把 `left`/`right` 换成一个 `next`，就变成了链表。所以链表是"退化"的树。

## 二、BFS 是什么

**按"层"进行搜索。**对树来说就是第 1 层（root）、第 2 层、第 3 层……对图来说更像洋葱，一圈一圈往外剥。凡是**和层数相关**的树题，都适合用 BFS。

## 三、BFS 通用模板（几乎每道题都能套）

1. **用所有入口初始化队列。**树只有 root 一个入口，以后遇到图时，要把所有起点都放进去。
2. **当队列不为空时：**
   1. **先记下当前层的结点数 `size`**（视频里的 currSize）。
   2. 对当前层的每个结点：
      - 取出结点，按题意处理（比如加入答案）；
      - **展开**它：把孩子**按题目要求的顺序**加入队列；
   3. 层数 + 1。

### 为什么要先记 size？

讲者用"盒子"比喻：取出一个大盒子时，要把里面的小盒子（孩子）放进队列。如果不先记下 `size`，队列长度会随着放入小盒子而**动态变化**，就把下一层的小盒子也当成当前层处理了。**当前层只处理当前层的大盒子。**

### 为什么用队列？

队列先进先出：先进队的先展开，正好保证从左到右、一层一层地处理。Python 用 `collections.deque`，`popleft()` 是 O(1)。

## 四、例题

### 102. 二叉树的层序遍历
标准模板。每层收集一个 `level` 列表，孩子按"先左后右"入队。

如果**去掉 `for size` 那层循环**，就没有"层"的概念了，得到的只是从上到下、从左到右的一个序列，代码中的 `bfs_order` 演示了这一点。

### 104. 二叉树的最大深度
最后展开的那一层就是最深的一层。**把"层"数字化**：每处理完一层 `depth += 1`，最后的 `depth` 就是答案。

### 199. 二叉树的右视图
站在树的右边往左看，看到的是**每一层最右边的结点**。
- 技巧：**先右后左**入队，这样每层队首就是最右边的结点。
- 也可以先左后右入队，取每层**最后一个**结点。
- 这正是模板里"按题目要求的顺序"的含义：从左到右还是从右到左，由题目决定。

## 五、完整代码

包括视频例题 102、104、199，补充练习：103 锯齿形层序遍历、111 最小深度。BFS 遇到第一个叶子就能停下，比 DFS 更快，这正好体现了 BFS 的优势。

```python
"""第 8 集：树的广度优先搜索 BFS —— 一套模板按层展开"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build_tree(vals):
    """按 LeetCode 的层序写法建树：[3,9,20,None,None,15,7]"""
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q, i = deque([root]), 1
    while q and i < len(vals):
        node = q.popleft()
        for side in ("left", "right"):
            if i < len(vals) and vals[i] is not None:
                child = TreeNode(vals[i])
                setattr(node, side, child)
                q.append(child)
            i += 1
    return root


# ================= BFS 模板 =================
# 1. 用所有入口初始化队列（树只有一个入口：root）
# 2. while 队列非空：
#      a. 先记下当前层的结点数 size（之后加入的是下一层，不能算进来）
#      b. 依次取出 size 个结点，按题意处理
#      c. 展开：把孩子按题目要求的顺序加入队列
#      d. 层数 + 1

# 102. 二叉树的层序遍历
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    if not root:
        return res
    q = deque([root])
    while q:
        size = len(q)                       # 当前层的"大盒子"个数
        level = []
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left:                   # 从左到右：先左后右
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res


# 104. 二叉树的最大深度：BFS 一共展开了几层
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    depth, q = 0, deque([root])
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1                          # 每做完一层，深度 + 1
    return depth


# 199. 二叉树的右视图：每层最右边的结点
# 按"先右后左"入队，每层队首就是最右边的结点
def right_side_view(root: Optional[TreeNode]) -> List[int]:
    res = []
    if not root:
        return res
    q = deque([root])
    while q:
        res.append(q[0].val)                # 当前层第一个 = 最右
        for _ in range(len(q)):
            node = q.popleft()
            if node.right:                  # in order：先右再左
                q.append(node.right)
            if node.left:
                q.append(node.left)
    return res


# 补充 103. 锯齿形层序遍历：层号决定方向
def zigzag_level_order(root):
    res = []
    for i, level in enumerate(level_order(root)):
        res.append(level if i % 2 == 0 else level[::-1])
    return res


# 补充 111. 二叉树的最小深度：BFS 遇到的第一个叶子就是答案（比 DFS 更快停下）
def min_depth(root):
    if not root:
        return 0
    q, depth = deque([root]), 1
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1
    return depth


# 不分层的版本：去掉 for 循环，就只是"从上到下、从左到右"的顺序
def bfs_order(root):
    out, q = [], deque([root] if root else [])
    while q:
        node = q.popleft()
        out.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return out


if __name__ == "__main__":
    t = build_tree([3, 9, 20, None, None, 15, 7])
    print("树 [3,9,20,null,null,15,7]")
    print("102 level_order    ->", level_order(t))
    print("    bfs_order(不分层) ->", bfs_order(t))
    print("104 max_depth      ->", max_depth(t))
    print("103 zigzag         ->", zigzag_level_order(t))
    print("111 min_depth      ->", min_depth(t))
    print("199 right_side_view([1,2,3,null,5,null,4]) ->", right_side_view(build_tree([1, 2, 3, None, 5, None, 4])))
    print("199 right_side_view([1,2,3,null,5])        ->", right_side_view(build_tree([1, 2, 3, None, 5])))
```

运行 `python ep08_tree_bfs.py` 的实际输出：

```text
树 [3,9,20,null,null,15,7]
102 level_order    -> [[3], [9, 20], [15, 7]]
    bfs_order(不分层) -> [3, 9, 20, 15, 7]
104 max_depth      -> 3
103 zigzag         -> [[3], [20, 9], [15, 7]]
111 min_depth      -> 2
199 right_side_view([1,2,3,null,5,null,4]) -> [1, 3, 4]
199 right_side_view([1,2,3,null,5])        -> [1, 3, 5]
```

## 六、复杂度
每个结点入队、出队各一次：时间 O(n)；队列最多同时容纳一层的结点：空间 O(w)，w 是最宽那层的宽度。

## 本集要点
- 树是只有一个入口的无环图；绝大多数题是没有父指针的二叉树。
- **BFS 模板**：队列初始化 → 记下 size → 逐个取出、处理、按顺序展开 → 层数 + 1。
- 和层数有关的题优先考虑 BFS；改变入队顺序就能解决"从右往左"类问题。
- 下一集讲 DFS：这些题也都能用 DFS 解，但 DFS 的变化更多。


---

# 第 9 集：树 Tree 的深度优先搜索 DFS

> DFS 是树里最重要的算法，图里也一样。

## 一、DFS vs BFS

| | BFS | DFS |
| --- | --- | --- |
| 形式 | 迭代（队列） | **递归**（调用栈） |
| 方向 | 水平：一层一层地走 | 垂直：一口气扎到底，没路了再回头 |
| 时间 | O(n) | O(n)：二叉树每个结点严格来说被访问 3 次（下来时、左边回来、右边回来），常数可以忽略 |
| 空间 | 和**宽度**有关，越往下层越宽，越吃内存 | 和**高度**有关，平衡树只需 O(log n)，**更省内存** |

## 二、最简单的 DFS 模板

1. **base case**：防止无限递归。
2. **做事（do something）** 和 **递归子问题（recurse）**：两者的**先后顺序不固定**。

只递归不做事没有意义，而"做事"放在哪里，就决定了遍历顺序：

| 遍历 | 顺序 | 树 `[6,3,null,1,4,null,2,null,5]` 的结果 |
| --- | --- | --- |
| 前序 preorder | **先做事**，再递归左、右 | 6 3 1 2 4 5 |
| 中序 inorder | 左 → **做事** → 右（只有二叉树才有） | 1 2 3 4 5 6（二叉搜索树的中序遍历是有序的） |
| 后序 postorder | 左 → 右 → **最后做事** | 2 1 5 4 3 6（根最后输出） |

**依然最重要的一点：相信你的递归函数是对的。**

## 三、Bottom-up DFS：从下往上传值（最常见，也最难）

利用**子问题传上来的值**构建当前问题的答案，再返回给父问题，所以**一定有返回值**。

**五步：**
1. base case
2. **向子问题要答案**：子问题的答案就是递归函数的返回值
3. **利用子问题的答案构建当前问题的答案**
4. （可选）额外操作，比如更新全局答案
5. **返回答案给父问题**：含义**必须和第 2 步相同**，因为"父亲向我要答案"就是"我向孩子要答案"

> 讲者建议：想递归时，找一个**中间状态**的结点来推，不要盯着 base case 想。

### 例 1：104. 最大深度（Bottom-up）
站在中间结点上：左子树告诉我它深 2 层，右子树告诉我它深 1 层。我取较深的一边，再加上连到自己的这一层，返回 `max(left, right) + 1`。

### 例 2：124. 二叉树中的最大路径和（Hard，"其实一点都不难"）
- 题目要的路径可以是**"人字形"**：从左边上来、经过一个顶点、再从右边下去。
- **递归函数的定义只能是"直上直下"的路径**，即从子树根往下、不拐弯的最大和。原因是如果返回人字形，父结点接上去就不再是一条合法路径了：路径到达顶点后已经拐弯往下，不能再往上走。
- 所以人字形**只能在当前层拼出来**：`left + right + node.val`，用来更新**全局最大值**（第 4 步）；返回给父结点的是 `max(left, right) + node.val`（第 5 步，和第 2 步含义一致）。
- **负数只有坏处**：`left`、`right` 如果是负的，就当成 0，等于不要这一边。
- 按转写还原视频中的树 `[-25,20,10,15,7,null,null,5,3]`：在结点 20 处拼出 `5+15+20+7 = 47`；返回给父结点的是 `20+15+5 = 40`；根是 -25，接上只会变小，所以答案是 47。

### 推荐：236. 最近公共祖先
讲者说这道题是"很多初学者最头疼的 DFS 题"，也是 Bottom-up 的经典题。递归返回的含义是：这棵子树里找到的 p 或 q（或者它们的公共祖先）。左右两边都找到了，当前结点就是答案。

## 四、Top-down DFS：从上往下传值（相对简单）

通过**参数**把值往下传，递归函数一般**没有返回值**，通常在 base case 处更新全局答案。

**四步：**
1. base case
2. 利用父问题传下来的值做计算
3. （可选）额外操作
4. 把新值通过参数传给子问题，继续递归

### 例 3：129. 求根到叶子的数字之和
- 树 `[4,9,0,5,1]` 中，路径组成的数字是 495、491、40，总和为 1026。
- 在结点 9 处：上面传下来 4，拼接成 `4*10 + 9 = 49`，再往下传。
- **base case 是叶子**，不是空结点：到了叶子才能把完整的数字加进全局和。中间结点不能加，因为后面还有数字。

## 五、完整代码

```python
"""第 9 集：树的深度优先搜索 DFS —— 前中后序 + Bottom-up + Top-down"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build_tree(vals):
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q, i = deque([root]), 1
    while q and i < len(vals):
        node = q.popleft()
        for side in ("left", "right"):
            if i < len(vals) and vals[i] is not None:
                child = TreeNode(vals[i]); setattr(node, side, child); q.append(child)
            i += 1
    return root


# ========== 最简单的 DFS 模板 ==========
# base case -> 做事(do something) 和 递归子问题(recurse)，二者顺序决定了前/中/后序
def preorder(root, out):        # 先做事，再递归
    if not root:
        return
    out.append(root.val)
    preorder(root.left, out)
    preorder(root.right, out)


def inorder(root, out):         # 左 -> 做事 -> 右（只有二叉树才有中序）
    if not root:
        return
    inorder(root.left, out)
    out.append(root.val)
    inorder(root.right, out)


def postorder(root, out):       # 左 -> 右 -> 最后才做事
    if not root:
        return
    postorder(root.left, out)
    postorder(root.right, out)
    out.append(root.val)


# ========== Bottom-up DFS（最常见、最难）==========
# 1. base case
# 2. 向子问题要答案（递归的返回值）
# 3. 利用子问题的答案，构建当前问题的答案
# 4. （可选）额外操作，例如更新全局答案
# 5. 返回答案给父问题 —— 含义必须与第 2 步相同

# 104. 二叉树的最大深度（Bottom-up）
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:                                  # 1
        return 0
    left = max_depth(root.left)                   # 2
    right = max_depth(root.right)
    return max(left, right) + 1                   # 3 + 5：较深的一边 + 连到自己的一条边


# 124. 二叉树中的最大路径和（Hard）
# 递归函数返回：从当前结点往下、"不拐弯"的最大路径和（直上直下）
# 题目要的"人字形"路径只能在当前层拼出来 -> 用全局变量记录
def max_path_sum(root: Optional[TreeNode]) -> int:
    best = float("-inf")

    def dfs(node):
        nonlocal best
        if not node:                              # 1
            return 0
        left = max(dfs(node.left), 0)             # 2 负数只有坏处，不要它（当成 0）
        right = max(dfs(node.right), 0)
        best = max(best, left + right + node.val) # 4 在当前层拼出"人字形"，更新全局答案
        return max(left, right) + node.val        # 3+5 返回给父亲的只能是"直上直下"的一边

    dfs(root)
    return best


# 补充 236. 二叉树的最近公共祖先（讲者点名的经典 Bottom-up 题）
# 返回含义：这棵子树里找到的 p 或 q（或它们的 LCA），找不到返回 None
def lowest_common_ancestor(root, p, q):
    if not root or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:                            # p、q 分别在两边 -> 当前就是 LCA
        return root
    return left or right


# ========== Top-down DFS ==========
# 1. base case   2. 用父问题传下来的值做计算   3.（可选）额外操作   4. 把新值传给子问题继续递归

# 129. 求根节点到叶节点数字之和
def sum_numbers(root: Optional[TreeNode]) -> int:
    total = 0

    def dfs(node, num):
        nonlocal total
        num = num * 10 + node.val                 # 2 拼接数字：上面传下来的 * 10 + 自己
        if not node.left and not node.right:      # 1 base case 是叶子
            total += num                          # 3 到叶子才加入全局答案
            return
        if node.left:                             # 4 往下传
            dfs(node.left, num)
        if node.right:
            dfs(node.right, num)

    if root:
        dfs(root, 0)
    return total


# 补充 112. 路径总和（Top-down：把"剩余目标"往下传）
def has_path_sum(root, target):
    if not root:
        return False
    target -= root.val
    if not root.left and not root.right:
        return target == 0
    return has_path_sum(root.left, target) or has_path_sum(root.right, target)


if __name__ == "__main__":
    t = build_tree([6, 3, None, 1, 4, None, 2, None, 5])
    for name, f in (("前序", preorder), ("中序", inorder), ("后序", postorder)):
        out = []; f(t, out); print(f"{name} [6,3,null,1,4,null,2,null,5] ->", out)
    print("104 max_depth([3,9,20,null,null,15,7]) ->", max_depth(build_tree([3, 9, 20, None, None, 15, 7])))
    print("124 max_path_sum([-10,9,20,null,null,15,7]) ->", max_path_sum(build_tree([-10, 9, 20, None, None, 15, 7])))
    print("124 视频例子 max_path_sum([-25,20,10,15,7,null,null,5,3]) ->",
          max_path_sum(build_tree([-25, 20, 10, 15, 7, None, None, 5, 3])))
    print("129 sum_numbers([4,9,0,5,1]) ->", sum_numbers(build_tree([4, 9, 0, 5, 1])), "(495+491+40)")
    print("129 sum_numbers([1,2,3])     ->", sum_numbers(build_tree([1, 2, 3])), "(12+13)")
    r = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p, q = r.left, r.left.right.right                     # 5 和 4
    print("236 LCA(5, 4) in [3,5,1,6,2,0,8,null,null,7,4] ->", lowest_common_ancestor(r, p, q).val)
    print("236 LCA(5, 1) ->", lowest_common_ancestor(r, r.left, r.right).val)
    print("112 has_path_sum([5,4,8,11,null,13,4,7,2], 22) ->",
          has_path_sum(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2]), 22))
```

运行 `python ep09_tree_dfs.py` 的实际输出：

```text
前序 [6,3,null,1,4,null,2,null,5] -> [6, 3, 1, 2, 4, 5]
中序 [6,3,null,1,4,null,2,null,5] -> [1, 2, 3, 4, 5, 6]
后序 [6,3,null,1,4,null,2,null,5] -> [2, 1, 5, 4, 3, 6]
104 max_depth([3,9,20,null,null,15,7]) -> 3
124 max_path_sum([-10,9,20,null,null,15,7]) -> 42
124 视频例子 max_path_sum([-25,20,10,15,7,null,null,5,3]) -> 47
129 sum_numbers([4,9,0,5,1]) -> 1026 (495+491+40)
129 sum_numbers([1,2,3])     -> 25 (12+13)
236 LCA(5, 4) in [3,5,1,6,2,0,8,null,null,7,4] -> 5
236 LCA(5, 1) -> 3
112 has_path_sum([5,4,8,11,null,13,4,7,2], 22) -> True
```

## 本集要点
- DFS 用递归，"做事"放的位置决定前序、中序还是后序；DFS 比 BFS 省内存。
- **Bottom-up 五步**：base case → 向子问题要答案 → 构建当前答案 → （更新全局）→ 返回，第 2 步和第 5 步含义必须一致。
- 题目要的答案和递归返回值不一样时（如 124 题），用**全局变量**记录答案。
- **Top-down**：值通过参数往下传，在叶子处汇总。


---

# 第 10 集：图 Graph 的广度优先搜索 BFS

## 一、图和树的区别

| | 树 | 图 |
| --- | --- | --- |
| 环 | 无环 | **可能有环**，所以必须**查重** |
| 方向 | 只能从父到子 | 分**无向图**（来回都能走）和**有向图**（箭头方向才能走） |
| 入口 | 只有 root 一个 | **没有固定入口，可能有多个起点**；图没有 root 的概念 |

## 二、图的两种表示方法

图有两个规模参数：**V**（结点数）和 **E**（边数）。

| 表示 | 结构 | 优缺点 |
| --- | --- | --- |
| 邻接矩阵 | V×V 矩阵，`m[i][j] = 1` 表示 i、j 相连 | 一定要开 V² 的空间，边很少时大部分是 0，很浪费；而且**必须预先知道 V** |
| **邻接表**（最常用） | 每个结点 → 它的邻居列表 | 边少时省内存；用 `dict` 实现时**不需要预先知道结点数**，可以动态添加 |

实际题目中往往只给出一堆边，比如 `(0,4)`、`(1,2)`，并不知道一共有多少个结点，甚至可能有不和主体相连的孤立结点。所以最常用的是 **`dict` 形式的邻接表**：key 是结点，value 是它所有邻居组成的 list 或 set。

## 三、BFS 在图上的特点

- 像剥洋葱一样**一圈一圈往外扩展**，所以适合找**最短路径**：目标在第 5 层被扩展到，最短距离就是 5。
- 一个结点第一次被访问时就记下它的层数，之后从别的路径再次到达时，不会再更新。
- **前提：所有边的权重相同（uniform cost）。**如果权重不同，比如直达要 5，绕路是 1+2=3，绕路反而更近，"层数"就不等于最短距离了。这种情况留到第 11 集讲。

## 四、图 BFS 模板

1. **用所有起点初始化队列**，再用一个**哈希集合 `visited`** 记录访问过的结点，防止在环里死循环。
2. 当队列不为空时：
   1. 记下当前层大小 `size`；
   2. 对当前层的每个结点：取出它；（可选）如果是目标，直接返回；把**没访问过且合法**的邻居入队，并标记为已访问；
   3. 层数（也就是 cost）+ 1。

"合法"指的是不越界、不是障碍物等。比如矩阵左上角的格子，只有右边和下面两个邻居。

**二维矩阵小技巧**：预先存好四个方向 `[(0,1),(1,0),(0,-1),(-1,0)]`，循环一下就能拿到上下左右四个邻居。

**时间复杂度 O(V + E)**：每个结点、每条边各访问一次。

## 五、例 1：542. 01 矩阵

求每个格子到最近的 0 的距离。相邻格子的距离为 1，正好是等权图。

- **直接的思路**：对每个 1 单独做一次 BFS 找最近的 0。最坏情况每次都要扫遍整个矩阵，O((mn)²)。
- **反向思维**：**所有 0 同时作为起点**，只做**一次** BFS。第一层扩展到的 1 距离为 1，第二层扩展到的距离为 2……总共 O(mn)。这叫**多源 BFS**。
- 矩阵问题用一个**同样大小的布尔数组**代替哈希集合，标记访问状态。
- 所有 0 一开始就被标记成已访问，所以"没访问过"的格子一定是 1，只需要再判断是否越界。

## 六、例 2：127. 单词接龙（更常见的"隐式图"）

把 `hit` 每次只改一个字母变成 `cog`，中间的每个词都必须在字典里。求最短变换序列包含的**单词数**：`hit → hot → dot → dog → cog`，共 5 个。

- **看出这是图**：每个单词是一个结点，**只差一个字母的两个单词是邻居**。这是无向图，因为把那个字母改回去就能变回来。题目没说是图，但它本质是图上的最短路径问题。这类题才是**最常见**的图题。
- **建图**：枚举所有单词对，判断是否只差一个字母，O(n²) 对。
- **细节**：
  - 终点不在字典里，直接返回 0。
  - 起点可以不在字典里。不在的话要加进去建图，否则起点没有任何邻居，一开始就"死"了。
  - `cost` 从 **1** 开始，因为数的是结点数，结点数 = 边数 + 1；返回 0 表示无解。
- 然后直接套模板：起点入队，遇到终点就返回 `cost`。

> 补充：代码中还提供了 `ladder_length_fast`，用"通配符分桶"建图。比如 `hot` 放进 `*ot`、`h*t`、`ho*` 三个桶，同一个桶里的单词互为邻居。不用比较所有单词对，单词多时快得多，面试时可以作为优化思路提出来。

## 七、完整代码

包括图的两种表示、542、127，以及推荐题 994 腐烂的橘子。994 是多源 BFS，和 542 是同一个套路。

```python
"""第 10 集：图的广度优先搜索 BFS（等权图上的最短路径）"""
from collections import defaultdict, deque
from typing import List

# ---------- 图的表示 ----------
# 邻接矩阵：V x V，matrix[i][j] = 1 表示 i、j 相连。边少时浪费空间
# 邻接表：  node -> 邻居列表。不知道结点总数时用 dict（会自动扩容）
EDGES = [(0, 1), (0, 4), (1, 4), (1, 2), (1, 3), (2, 3), (3, 4)]


def adjacency_matrix(n, edges):
    m = [[0] * n for _ in range(n)]
    for a, b in edges:
        m[a][b] = m[b][a] = 1             # 无向图：两个方向都连
    return m


def adjacency_list(edges):
    g = defaultdict(list)
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)
    return dict(g)


# ================= 图 BFS 模板 =================
# 1. 用【所有】起点初始化队列，并用 visited 记录访问过的结点（图可能有环，必须查重）
# 2. while 队列非空：
#      a. 记下当前层大小 size
#      b. 逐个取出结点；(可选) 若是目标则直接返回
#         把【没访问过且合法】的邻居入队，并立刻标记 visited
#      c. 层数 / cost + 1
# 注意：只适用于每条边权重相同（uniform cost）的图
# 复杂度 O(V + E)

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]   # 二维矩阵的上下左右四个邻居


# ---------- 542. 01 矩阵：每个格子到最近的 0 的距离 ----------
# 反向思维：不是每个 1 各做一次 BFS（O((mn)^2)），而是所有 0 同时作为起点做一次 BFS（O(mn)）
def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    res = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]   # 二维矩阵用布尔数组代替 hash set
    q = deque()
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:                   # 所有 0 都是起点
                q.append((i, j))
                visited[i][j] = True
    cost = 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if mat[i][j] == 1:
                res[i][j] = cost                 # 第一次被扩展到时的层数就是最近距离
            for di, dj in DIRS:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    q.append((x, y))
                    visited[x][y] = True
        cost += 1
    return res


# ---------- 127. 单词接龙 ----------
# 隐式图：两个单词只差一个字母就是邻居（无向图）
def one_change_away(a: str, b: str) -> bool:
    return sum(x != y for x, y in zip(a, b)) == 1


def construct_graph(words: List[str]):
    g = defaultdict(list)
    for i in range(len(words)):                  # 枚举每一对单词：O(n^2 * L)
        for j in range(i + 1, len(words)):
            if one_change_away(words[i], words[j]):
                g[words[i]].append(words[j])
                g[words[j]].append(words[i])
    return g


def ladder_length(begin: str, end: str, word_list: List[str]) -> int:
    words = list(word_list)
    if end not in words:
        return 0
    if begin not in words:                       # 起点可以不在字典里，加进去方便建图
        words.append(begin)
    g = construct_graph(words)
    visited, q = {begin}, deque([begin])
    cost = 1                                     # 题目数的是单词个数 = 边数 + 1
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur == end:                       # 可选步骤：找到终点直接返回
                return cost
            for nb in g.get(cur, []):
                if nb not in visited:
                    visited.add(nb)
                    q.append(nb)
        cost += 1
    return 0


# 更快的建图方式（面试加分）：通配符分桶  "hot" -> "*ot","h*t","ho*"，O(n * L^2)
def ladder_length_fast(begin, end, word_list):
    words = set(word_list)
    if end not in words:
        return 0
    buckets = defaultdict(list)
    for w in words | {begin}:
        for i in range(len(w)):
            buckets[w[:i] + "*" + w[i + 1:]].append(w)
    visited, q, cost = {begin}, deque([begin]), 1
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur == end:
                return cost
            for i in range(len(cur)):
                for nb in buckets[cur[:i] + "*" + cur[i + 1:]]:
                    if nb not in visited:
                        visited.add(nb); q.append(nb)
        cost += 1
    return 0


# ---------- 推荐题 994. 腐烂的橘子（多源 BFS，和 542 同一个套路） ----------
def oranges_rotting(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    q = deque((i, j) for i in range(m) for j in range(n) if grid[i][j] == 2)
    fresh = sum(row.count(1) for row in grid)
    minutes = 0
    while q and fresh:
        for _ in range(len(q)):
            i, j = q.popleft()
            for di, dj in DIRS:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2               # 直接改原数组充当 visited
                    fresh -= 1
                    q.append((x, y))
        minutes += 1
    return -1 if fresh else minutes


if __name__ == "__main__":
    print("邻接矩阵:")
    for row in adjacency_matrix(5, EDGES):
        print("   ", row)
    print("邻接表:", adjacency_list(EDGES))
    for mat in ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [1, 1, 1]]):
        print("542 update_matrix", mat, "->", update_matrix(mat))
    wl = ["hot", "dot", "dog", "lot", "log", "cog"]
    print("127 ladder_length('hit','cog',", wl, ") ->", ladder_length("hit", "cog", wl))
    print("127 ladder_length_fast 同一输入 ->", ladder_length_fast("hit", "cog", wl))
    print("127 字典里没有 'cog' ->", ladder_length("hit", "cog", wl[:-1]))
    print("994 oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) ->", oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
```

运行 `python ep10_graph_bfs.py` 的实际输出：

```text
邻接矩阵:
    [0, 1, 0, 0, 1]
    [1, 0, 1, 1, 1]
    [0, 1, 0, 1, 0]
    [0, 1, 1, 0, 1]
    [1, 1, 0, 1, 0]
邻接表: {0: [1, 4], 1: [0, 4, 2, 3], 4: [0, 1, 3], 2: [1, 3], 3: [1, 2, 4]}
542 update_matrix [[0, 0, 0], [0, 1, 0], [0, 0, 0]] -> [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
542 update_matrix [[0, 0, 0], [0, 1, 0], [1, 1, 1]] -> [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
127 ladder_length('hit','cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'] ) -> 5
127 ladder_length_fast 同一输入 -> 5
127 字典里没有 'cog' -> 0
994 oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) -> 4
```

## 推荐练习（视频结尾列出的等权 BFS 题）
934 最短的桥、310 最小高度树、1091 二进制矩阵中的最短路径、994 腐烂的橘子、863 二叉树中所有距离为 K 的结点、317 离建筑物最近的距离。

## 本集要点
- 图可能有环、有多个入口，所以要**把所有起点入队**并用 `visited` 查重。
- 最常用的表示是 `dict` 形式的邻接表。
- 等权图上，BFS 的层数就是最短距离；**多源 BFS**（所有起点同时出发）能把 O((mn)²) 降到 O(mn)。
- 很多题是**隐式图**，要自己发现"结点是什么、邻居是什么"，然后套模板。


---

# 第 11 集：图 Graph 的 Best-First Search（最优优先搜索）

## 一、为什么需要它

- 第 10 集的 BFS（Breadth-First Search）只适用于**等权图（uniform cost）**，所有边的代价相同。
- **边权不同（non-uniform cost）**时，层数不再等于最短距离。这时要用 **Best-First Search**：**优先展开当前最优（cost 最小）的结点**。
- 怎样每次快速拿到"最优"的结点？用**堆**（第 6 集）。堆每次只给出堆顶，也就是最小的那个，正好满足需要。
- 这就是图中最有名的最短路径算法：**Dijkstra 算法**。

## 二、直观例子

起点 0，边 `0→3` 代价 3，`0→5` 代价 8，`3→5` 代价 2：
1. 展开 0：结点 3 暂定 cost 为 3，结点 5 暂定 cost 为 8。
2. 3 比 8 小，**先展开 3**：经过 3 到达 5 的代价是 3 + 2 = 5，比 8 小，把 5 更新为 5。
3. 最后展开 5，它的最短距离是 5。

就像转机：直飞 8 块钱，转一次机 3 + 2 = 5 块钱，转机更便宜。

## 三、模板：和 BFS 几乎一样，只是**队列换成堆**

1. 用所有起点初始化**最小堆**，每个起点带一个初始 cost，通常为 0；再用一个**哈希集合**记录**已展开**的结点。
2. 当堆不为空时：
   1. 弹出一个结点（堆顶 = 当前 cost 最小的结点）；
   2. **如果已经展开过，跳过**；否则标记为已展开，并记下它的 cost；
   3. （可选）如果是终点，直接返回；
   4. 所有邻居以 **"当前结点的 cost + 边的 cost"** 入堆。

### 和 BFS 的关键区别：查重的位置

- BFS 在**入队时**查重：邻居访问过就不入队。
- Best-First 在**弹出时**查重。原因是**同一个结点可能以不同的 cost 入堆多次**，比如 A 从 B 过来代价是 2，从 C 过来代价是 3，A 就会入堆两次。入堆时还不知道哪个 cost 最小，交给堆去排序。按照最优优先的原则，**A 第一次被弹出时一定带着最小的 cost**，之后再弹出的 A 直接跳过。所以一个结点**可以入堆多次，但只会被展开一次**。

复杂度：每个结点、每条边都要处理，再乘上堆操作的 log。空间 O(V)，也就是堆里的所有元素。

## 四、例 1：743. 网络延迟时间

n 个结点，`times[i] = (u, v, w)` 表示一条**有向边** u→v，传输时间为 w。从 k 发出信号，求所有结点都收到信号的最短时间。

- **转化**：信号同时向各条边扩散，像自来水管分叉后同时流出。最远的房子通水时，所有房子都已经通水了。所以答案就是**到"最远"结点的最短路径**。
- **建图**：邻接表里除了邻居，还要**多存一个 cost**，即 `u → [(v, w), ...]`。Java 要另外写一个类，Python 直接用元组。
- **主逻辑**：套模板，起点 cost 为 0。用 `dict` 同时充当"已展开集合"和"最短时间表"。这道题没有终点，要把整张图都展开完。
- **结果**：展开的结点数 ≠ n，说明有结点收不到信号，返回 -1；否则返回所有最短时间里的最大值。

## 五、例 2：787. K 站中转内最便宜的航班

在最多中转 k 次的前提下，求 src 到 dst 的最低票价。
- 例：`0→1`（100）、`1→2`（100）、`0→2`（500）。k = 1 时可以在 1 中转，答案是 **200**；k = 0 时只能直飞，答案是 **500**。

**多了一个维度：中转次数。**
- 堆里存三个值：`(价格, 城市, 剩余中转次数)`。
- 剩余次数小于 0 时，这是**终止状态**，不能再往外飞。如果这里恰好是终点，仍然可以返回。
- 这道题有**终点**，用上模板里的可选步骤：**第一次弹出终点时，它的价格一定是最便宜的**，直接返回。
- 题目保证没有重复航班和自环。视频据此去掉了 visited 查重。但同一个城市可能以不同的"剩余次数"多次入堆，最坏情况下状态会爆炸，导致超时。代码里加了一个剪枝：到同一个城市时，如果之前已经以**更低价格、更多剩余次数**展开过，就跳过。这是我补充的工程细节。
- 代码里还附了 **Bellman-Ford** 解法：循环 k+1 轮，每轮用上一轮的结果松弛所有边，面试时可以作为对比。

## 六、完整代码

```python
"""第 11 集：Best-First Search（Dijkstra）—— 边权不同的图上找最短路径：把队列换成堆"""
import heapq
from collections import defaultdict
from typing import List

# ================= Best-First Search 模板 =================
# 1. 用所有起点初始化最小堆，每个起点带初始 cost（通常 0）；visited 记录"已展开"的结点
# 2. while 堆非空：
#      a. 弹出 cost 最小的结点
#      b. 已展开过 -> 跳过；否则标记为已展开，记下它的 cost（此时一定是最优的）
#      c. (可选) 是终点就直接返回
#      d. 所有邻居以 "当前 cost + 边的 cost" 入堆
# 和普通 BFS 的区别：查重放在"弹出时"(b)，而不是"入堆时"。
#   同一个结点可能以不同 cost 入堆多次，但只有 cost 最小的那次会被展开。
# 时间 O((V+E) log V) 量级，空间 O(V+E)


# ---------- 743. 网络延迟时间 ----------
# 从 k 出发，信号传遍所有结点的时间 = 到"最远"结点的最短路径
def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)                    # u -> [(v, w)]  有向图，要多存一个 cost
    for u, v, w in times:
        graph[u].append((v, w))
    cost = {}                                    # 已展开的结点 -> 最短时间（兼做 visited）
    heap = [(0, k)]                              # (cost, node)：cost 放前面，堆按它排序
    while heap:
        t, node = heapq.heappop(heap)
        if node in cost:                         # 已展开过，跳过
            continue
        cost[node] = t                           # 第一次弹出时就是最短时间
        for nb, w in graph[node]:
            if nb not in cost:                   # 小优化：已展开的就不必再入堆
                heapq.heappush(heap, (t + w, nb))
    return max(cost.values()) if len(cost) == n else -1   # 有结点到不了 -> -1


# ---------- 787. K 站中转内最便宜的航班 ----------
# 多了一个维度：中转次数。堆里存 (price, city, 剩余可中转次数)
def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))
    heap = [(0, src, k)]                         # 视频里从 k 倒着减到 0，更直观
    best_stops = {}                              # 剪枝：到同一城市，剩余次数更少的状态不必再展开
    while heap:
        price, city, stops = heapq.heappop(heap)
        if city == dst:                          # 最先弹出的终点一定最便宜
            return price
        if stops < 0:                            # 中转次数用完了：终止状态，不能再飞
            continue
        if best_stops.get(city, -2) >= stops:
            continue
        best_stops[city] = stops
        for nb, w in graph[city]:
            heapq.heappush(heap, (price + w, nb, stops - 1))
    return -1


# 787 的另一种经典解法：Bellman-Ford，限制最多 k+1 条边（面试可作为对比）
def find_cheapest_price_bf(n, flights, src, dst, k):
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    for _ in range(k + 1):
        new = dist[:]                            # 只用上一轮的结果，保证边数不超
        for u, v, w in flights:
            if dist[u] + w < new[v]:
                new[v] = dist[u] + w
        dist = new
    return -1 if dist[dst] == INF else dist[dst]


# ---------- 推荐题 1631. 最小体力消耗路径（Best-First 在矩阵上，cost = 路径上最大高度差） ----------
def minimum_effort_path(heights: List[List[int]]) -> int:
    m, n = len(heights), len(heights[0])
    heap, done = [(0, 0, 0)], set()
    while heap:
        effort, i, j = heapq.heappop(heap)
        if (i, j) in done:
            continue
        done.add((i, j))
        if (i, j) == (m - 1, n - 1):
            return effort
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and (x, y) not in done:
                e = max(effort, abs(heights[x][y] - heights[i][j]))
                heapq.heappush(heap, (e, x, y))
    return 0


if __name__ == "__main__":
    print("743 network_delay_time([[2,1,1],[2,3,1],[3,4,1]], n=4, k=2) ->",
          network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
    print("743 有结点到不了 network_delay_time([[1,2,1]], n=2, k=2) ->",
          network_delay_time([[1, 2, 1]], 2, 2))
    print("    视频开头例子 0->3(3), 0->5(8), 3->5(2)：到 5 的最短时间 ->",
          network_delay_time([[0, 3, 3], [0, 5, 8], [3, 5, 2]], 3, 0))
    f = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    print("787 find_cheapest_price(0->2, k=1) ->", find_cheapest_price(3, f, 0, 2, 1),
          "| Bellman-Ford ->", find_cheapest_price_bf(3, f, 0, 2, 1))
    print("787 find_cheapest_price(0->2, k=0) ->", find_cheapest_price(3, f, 0, 2, 0),
          "| Bellman-Ford ->", find_cheapest_price_bf(3, f, 0, 2, 0))
    print("1631 minimum_effort_path([[1,2,2],[3,8,2],[5,3,5]]) ->",
          minimum_effort_path([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
```

运行 `python ep11_best_first_search.py` 的实际输出：

```text
743 network_delay_time([[2,1,1],[2,3,1],[3,4,1]], n=4, k=2) -> 2
743 有结点到不了 network_delay_time([[1,2,1]], n=2, k=2) -> -1
    视频开头例子 0->3(3), 0->5(8), 3->5(2)：到 5 的最短时间 -> 5
787 find_cheapest_price(0->2, k=1) -> 200 | Bellman-Ford -> 200
787 find_cheapest_price(0->2, k=0) -> 500 | Bellman-Ford -> 500
1631 minimum_effort_path([[1,2,2],[3,8,2],[5,3,5]]) -> 2
```

## 本集要点
- 边权相同 → BFS + 队列；**边权不同 → Best-First（Dijkstra）+ 最小堆**。
- 查重放在**弹出时**：结点可以多次入堆，但只展开一次，第一次弹出时的 cost 就是最优。
- 有终点的题，第一次弹出终点时就可以返回。
- 带限制条件（如中转次数）时，把限制条件也放进堆里的状态。


---

# 第 12 集：图 Graph 的深度优先搜索 DFS

## 一、图上的 DFS

和树的 DFS 概念相同：**一口气扎到最深**，走到死路再**回溯**（借助调用栈），然后换另一条路继续扎到底。
和树的区别在于**图可能有环**，遇到已经访问过的结点要停下，否则会死循环。

## 二、图 DFS 模板

**主函数：**
1. 初始化一个哈希集合记录已访问结点。如果题目保证无环，可以省略。
2. 对每个入口结点调用 `dfs`。DFS 是递归，通常要单独写一个函数，参数里带着"状态"。

**`dfs(状态)`：**
- **A.** 校验当前结点：已访问、不合法或已经是答案时，直接 return，相当于 base case。
- **B.** 做点事（**前序** pre-order）。
- 对每个邻居：
  - **C.** 校验邻居：不合法就不递归。
  - 递归 `dfs(邻居)`。
- **D.** 做点事（**后序** post-order），比如收尾工作。

**A 和 C 二选一，也可以都做**：A 是"先进去，发现不合法再退出来"；C 是"先检查，不合法就不进去"。
**B 和 D 根据题意来选**：先做事再递归是前序，先递归再做事是后序。

**复杂度 O(n·k)**：DFS 一般只允许每个结点被访问常数次，k 是 B、D 两步的工作量。

> 重要：**DFS 一定要先定义好"状态"**，也就是递归函数的参数代表什么。

## 三、例 1：200. 岛屿数量

二维网格中，上下左右相连的 1 组成一座岛，求岛的数量。

- 每一片相连的 1 都是一张**独立的图**。
- 从左到右、从上到下扫描网格，**每遇到一个还没访问过的 1**：岛屿数加 1，然后以它为起点做一次遍历（BFS、DFS 都可以），把整座岛**染色**，也就是标记为已访问。
- 之后再扫到这座岛上的其他 1 时，因为已经染过色，就不会重复计数。
- **小技巧**：直接把访问过的 1 改成 0，代替哈希集合。0 本来就是不合法的结点，改完后外层循环的 `if == 1` 自然就跳过了。讲者说这个方法"比较恶心"，因为它修改了输入；代码里先复制一份再修改。
- **状态**就是当前位置 `(i, j)`。
- 时间 O(mn)：每个格子最多访问一次。

## 四、例 2：332. 重新安排行程（较难）

给定一组机票 `[from, to]`，从 JFK 出发，**每张机票必须用且只能用一次**，排出行程。有多种行程时，返回**字典序最小**的那个。

- **这是在"边"上的遍历**：每张机票就是一条边，用过就扔掉。
- **建图**：本题需要按字典序取邻居，所以用"城市 → **最小堆**"代替普通列表。从堆里弹出既能保证字典序，又能顺便**删除这条边**，保证每条边只走一次。
- **状态**：当前所在的城市。

### 为什么必须用后序，不能用前序？

- **前序**是到一个结点就先把它加进答案，再往后走。问题在于这时**还不知道后面的路能不能走通**。
  - 视频例子：`JFK→SFO`、`JFK→PVG`、`SFO→NRT`、`NRT→JFK`。按字典序先飞 PVG，就困在 PVG 了，没有机票可以离开。前序已经把 PVG 写进答案，无法挽回。
- **后序**是**先把后面所有可能性递归完，再处理当前结点**。递归时会把 SFO 和 PVG 两条路都走完，死胡同 PVG 会**最先**被加入答案。所以后序得到的是**倒序**的行程，最后整体反转一次即可：`JFK → SFO → NRT → JFK → PVG`。
- 还是那句话：**相信递归函数是对的**，它会把后面的路都处理好。

时间 O((V+E) log E)：每条边弹出一次，每次堆操作 O(log)。

## 五、完整代码

包括视频例题 200、332（附前序错误版的对比），补充练习：695 岛屿最大面积（用 A 方式校验，同时是 Bottom-up）、207 课程表（有向图找环，用三色标记 + 后序）。

```python
"""第 12 集：图的深度优先搜索 DFS"""
import heapq
import sys
from collections import defaultdict
from typing import List

sys.setrecursionlimit(10000)

# ================= 图 DFS 模板 =================
# 主函数：初始化 visited（无环可省）；对每个入口调用 dfs
# dfs(状态, ...):
#   A. 校验当前结点：已访问 / 不合法 / 已是答案 -> return       （A 与 C 二选一或都做）
#   B. 做点事（前序 pre-order）
#   for 每个邻居:
#      C. 校验邻居：不合法就不递归
#      递归 dfs(邻居)
#   D. 做点事（后序 post-order）                                 （B 与 D 根据题意选）
# 复杂度 O(n * k)：每个结点访问常数次，k 是 B/D 的工作量

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# ---------- 200. 岛屿数量 ----------
# 每遇到一个没访问过的 '1'，就以它为起点做一次遍历，把整座岛"染色"（这里直接改成 '0'）
def num_islands(grid: List[List[str]]) -> int:
    grid = [row[:] for row in grid]              # 复制一份，避免改坏调用者的输入
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        grid[i][j] = "0"                         # 标记已访问（代替 hash set）
        for di, dj in DIRS:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":   # C. 先校验再递归
                dfs(x, y)

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                count += 1                       # 发现一座新岛
                dfs(i, j)                        # 把整座岛染掉
    return count


# 补充 695. 岛屿的最大面积（同一模板，dfs 返回面积 -> Bottom-up）
def max_area_of_island(grid: List[List[int]]) -> int:
    grid = [row[:] for row in grid]
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if not (0 <= i < m and 0 <= j < n) or grid[i][j] == 0:   # A. 先进来再校验
            return 0
        grid[i][j] = 0
        return 1 + sum(dfs(i + di, j + dj) for di, dj in DIRS)

    return max((dfs(i, j) for i in range(m) for j in range(n)), default=0)


# ---------- 332. 重新安排行程 ----------
# 每张机票（边）必须且只能用一次 -> 在"边"上遍历；用过的边直接从堆里删掉
# 必须用后序：先把后面所有可能性递归完，再把当前城市加入答案（最后整体反转）
def find_itinerary(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)                    # 城市 -> 最小堆（保证字典序最小）
    for src, dst in tickets:
        heapq.heappush(graph[src], dst)
    route = []

    def dfs(city):
        while graph[city]:
            nxt = heapq.heappop(graph[city])     # 弹出即删除这张机票
            dfs(nxt)
        route.append(city)                       # D. 后序：子路线都走完了才加自己

    dfs("JFK")
    return route[::-1]                           # 后序得到的是倒序


# 用"前序"会出什么问题：贪心先飞字典序小的，可能走进死胡同
def find_itinerary_preorder_wrong(tickets):
    graph = defaultdict(list)
    for s, d in tickets:
        heapq.heappush(graph[s], d)
    route, city = ["JFK"], "JFK"
    while graph[city]:
        city = heapq.heappop(graph[city])
        route.append(city)
    return route


# ---------- 补充 207. 课程表（有向图找环：DFS 三色标记） ----------
def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)
    state = [0] * num_courses                    # 0 未访问，1 正在当前路径上，2 已完成

    def dfs(u):
        if state[u] == 1:                        # 回到了当前路径上的结点 -> 有环
            return False
        if state[u] == 2:
            return True
        state[u] = 1
        if not all(dfs(v) for v in graph[u]):
            return False
        state[u] = 2                             # 后序：所有后继都没问题才算完成
        return True

    return all(dfs(c) for c in range(num_courses))


if __name__ == "__main__":
    g1 = [list("11110"), list("11010"), list("11000"), list("00000")]
    g2 = [list("11000"), list("11000"), list("00100"), list("00011")]
    print("200 num_islands(例1) ->", num_islands(g1), "| num_islands(例2) ->", num_islands(g2))
    print("695 max_area_of_island ->", max_area_of_island(
        [[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 1, 0, 0, 0]]))
    t1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print("332 find_itinerary(例1) ->", find_itinerary(t1))
    t2 = [["JFK", "SFO"], ["JFK", "PVG"], ["SFO", "NRT"], ["NRT", "JFK"]]   # 视频里的例子
    print("332 find_itinerary(视频例子) ->", find_itinerary(t2))
    print("    前序贪心（错误）    ->", find_itinerary_preorder_wrong(t2), "<- 先飞 PVG 就困住了")
    print("207 can_finish(2, [[1,0]]) ->", can_finish(2, [[1, 0]]),
          "| can_finish(2, [[1,0],[0,1]]) ->", can_finish(2, [[1, 0], [0, 1]]))
```

运行 `python ep12_graph_dfs.py` 的实际输出：

```text
200 num_islands(例1) -> 1 | num_islands(例2) -> 3
695 max_area_of_island -> 5
332 find_itinerary(例1) -> ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
332 find_itinerary(视频例子) -> ['JFK', 'SFO', 'NRT', 'JFK', 'PVG']
    前序贪心（错误）    -> ['JFK', 'PVG'] <- 先飞 PVG 就困住了
207 can_finish(2, [[1,0]]) -> True | can_finish(2, [[1,0],[0,1]]) -> False
```

## 本集要点
- 图 DFS 模板：A/C 校验二选一，B/D 前序、后序根据题意选。
- 先定义好**状态**：网格题是 `(i, j)`，行程题是当前城市。
- "连通块计数"的套路：遇到一个没访问过的起点就计数加 1，再把整个连通块染色。
- **需要先知道后面所有可能性**时用后序，比如 332 题；"每条边只用一次"时在边上遍历，用过就删。
- 讲者建议多做题，培养对"前序还是后序""校验放在递归前还是递归后"的感觉。


---

# 第 13 集：搜索 Search 与动态规划 DP 入门

> **Search 是 DP 的"爸爸"。**两者在代码和概念上只差一点点：先彻底掌握搜索，再变成 DP 就非常简单了。

## 一、什么是搜索

- 一个大问题由多个子问题构成时，**不断分解问题**，最终构建出大问题的答案，这个过程叫搜索。
- **搜索空间可以画成一棵树。**面试时把搜索树画出来，既帮自己理清思路，也让面试官看出你对问题理解透彻。
- 时间复杂度取决于这棵树的**深度**和**每个结点的分支数**。
- **最重要的一点（DP 同样如此）：定义好状态。**保证每个子问题都能用一个状态来描述，也就是**子问题 = 状态**。

## 二、例 1：78. 子集（Top-down 搜索）

n 个元素的集合有 2ⁿ 个子集。所有子集构成的集合叫幂集（power set）。

**画搜索树**：以 `[1,3,4]` 为例，对每个元素都有两种选择，**要或不要**，所以是一棵二叉树：
- 第几层就代表考虑到第几个元素，n 层，叶子共 2ⁿ 个，这就是"2 的 n 次方"的由来。
- 一直走左边（都不要）得到空集；一直走右边（都要）得到 `[1,3,4]`。
- **状态 = (index, 当前子集)**。只有当前子集还不够，没有 index 就不知道下一个该考虑谁。

这是 **Top-down DFS**：状态从上往下传，**答案在叶子上**。

### Top-down 搜索模板
1. **定义状态**：所有子问题，包括最上层的大问题，都必须能用这个状态表示。这一步最难，没有模板可套，只能靠练习培养感觉。
2. 初始化初始状态，调用 `dfs`。
3. `dfs` 里：
   - a. **base case**：递归一上来就要检查，否则会死循环。
   - b. 对每个子问题：**更新到下一个状态 → 递归 → 恢复状态（restore state）**。

### 重中之重：恢复状态

同一层的兄弟结点之间不应该互相影响，它们只和父结点有关。父结点调用每个孩子时，传下去的东西必须一样。如果分支 1 往 `cur` 里加了元素却不删掉，分支 2 拿到的就是被改过的状态，"不要"这条分支就会变成"要"。

**另一个细节**：到达叶子、把 `cur` 加入结果时**必须复制一份**。因为整个过程只复用同一个列表，不复制的话，结果里存的全是同一个引用，最后内容全都一样。

## 三、从搜索到动态规划

- **搜索空间里有重复子问题**时，把子问题的答案记录下来，保证每个子问题只算一次，这就是 DP。所以 DP 也叫**"搜索 + 记忆化（memoization）"**。
- 记忆化本身一点都不难，可以用哈希表或数组当一张表格。**真正难的是：怎么搜索、状态是什么、递推规则是什么。**
- 子集问题**没有**重复子问题，每个分支都是新状态，所以用不上 DP。
- DP 的时间复杂度取决于**子问题的个数**：每个子问题至少算一次，但只算一次。在搜索树上，重复的结点被"剪掉"后，可能从 2ⁿ 变成 n²。
- **所有 DP 都可以写成 Bottom-up DFS 的形式。**

代码里用爬楼梯（70 题）直观对比：纯搜索要重复计算大量子问题，加上记忆化后几乎瞬间完成。

### Bottom-up DFS（DP）模板
1. **定义状态**
2. 初始化 memo（记录已算过的子问题）
3. `return dfs(最终状态)`：这里要的是**顶层**的答案，所以把最终状态作为切入点传进去

`dfs(状态)`：
1. base case
2. **如果当前问题已经算过，直接返回 memo 里的答案** ← DP 才有
3. 向每个子问题要答案，用它们**构建当前问题的答案**。这一步叫 **transition rule（递推规则）**
4. **把当前答案存进 memo** ← DP 才有
5. 返回答案

只有 1、3、5 三步就是普通搜索，加上 2、4 就是 DP。

> **小技巧**：定义好状态后，**从一个中间状态出发**去想递推规则。DP 的两大难点是**定义状态**和**递推规则**，而状态定义好了，递推规则通常就比较好想。

## 四、例 2：139. 单词拆分

判断字符串能否由字典中的单词拼成，单词可以重复使用。`"leetcode"` → True（leet + code）；`"applepenapple"` → True；`"catsandog"` → False。

### 单个数组或字符串，状态通常只有两种定义法
- **1D**：`dp[i]` 表示 `[0, i)` 这一段的答案（也可以是 `[i, n)`）。相当于只有一块挡板，左边隐含从 0 开始。
- **2D**：`dp[i][j]` 表示子数组 `[i, j]` 的答案，相当于两块挡板。
- 以后还会见到 3D，比如多了一个"k 步之内"的限制，但那个 k 和数组下标无关。
- **先试 1D**，可行就不必考虑 2D，因为 2D 的复杂度一定更高。

### 定义与递推
- **状态**：`dp(i)` 表示 `s[0:i]` 能否被拆分。
- **从中间状态 i 出发想**：如果某个更小的子问题 `dp(j)` 为真，并且剩下的 `s[j:i]` 正好是字典里的一个词，那 `dp(i)` 就为真。
- 枚举所有切法 `j ∈ [0, i)`，**有一种成立就为真，全都不成立才为假**。j 必须小于 i，否则就是用当前问题算当前问题，会死循环。
- 右边那一段 `s[j:i]` 不是从 0 开始的，不符合状态定义，所以**不能再递归**，只能直接查字典。
- **base case**：`i == 0`，空串认为可以拆分。
- **入口**：`dfs(n)`，也就是整个字符串。
- **优化**：先检查右半段在不在字典里，不在就不用递归左半段；把字典转成 `set`，查找 O(1)。

时间 O(n²)：共 n+1 个子问题，每个子问题最多回头看 n 个更小的子问题（不计字符串切片的开销）。

## 五、完整代码

包括视频例题 78、139，以及补充：46 全排列（纯搜索）、70 爬楼梯（搜索与记忆化的对比）。视频推荐的练习是"前两道搜索题、后三道最基础的 DP 题"，46 和 70 分别对应这两类。

```python
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
```

运行 `python ep13_search_dp.py` 的实际输出：

```text
78  subsets([1,3,4]) -> [[1, 3, 4], [1, 3], [1, 4], [1], [3, 4], [3], [4], []]
    subsets([1,3,4,7]) 个数 -> 16 (= 2^4)
46  permute([1,2,3]) -> [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
70  爬 30 级楼梯：纯搜索 1346269（0.098s）| 记忆化 1346269（0.000026s）
139 word_break('leetcode', ['leet', 'code']) -> True | lru_cache 版 -> True
139 word_break('applepenapple', ['apple', 'pen']) -> True | lru_cache 版 -> True
139 word_break('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']) -> False | lru_cache 版 -> False
```

## 本集要点
- **搜索**：画出搜索树，定义状态，Top-down 时记得**恢复状态**，到叶子时**复制结果**。
- **DP = 搜索 + 记忆化**：在 Bottom-up DFS 上多加"查表"和"存表"两步。
- 难点是**定义状态**和**递推规则**；从中间状态出发去想递推。
- 单个数组的状态先试 1D（`[0, i)`），不行再考虑 2D（`[i, j]`）。


---

# 第 14 集：一维动态规划 1D DP

> DP 系列从 1D 讲到 2D，最多到 3D，不会有 4D。

## 一、回顾

- Search 和 DP 都是由子问题构建大问题；区别在于 **DP 有重复子问题**。
- 重中之重：**定义好状态**；强烈建议**把搜索空间画成树**。
- DP 有两种写法，本系列**推荐 Bottom-up DFS + 记忆化**，原因见第四节。
- 定义好状态后，**从中间状态出发**去想递推规则。
- **拿不定主意时，把整个数组直接代进去**，先画出搜索树，再找规律。

## 二、例 1：96. 不同的二叉搜索树

用 1..n 能组成多少种不同的 BST？n = 3 时有 5 种。

**暴力思路**：在 `[1..n]` 中轮流选根。根左边的数只能进左子树，右边的数只能进右子树，左右区间再分别递归。

**画树找重复子问题**：
- 选 1 当根时，右边剩 `[2,3]`；选 3 当根时，左边剩 `[1,2]`。这两个区间看起来不同，但 `[1,2]` 能组成的 BST，把每个值加 1 就变成了 `[2,3]` 的 BST。
- **所以答案只和区间大小有关，和具体数值无关。**按大小重新画树，就会出现大量重复子问题：大小为 3 的问题会分出 (0,2)、(1,1)、(2,0)，其中大小为 2 的子问题出现了两次。推广到 n，从中间往两边看，整棵树左右**镜像对称**，几乎一半都是重复计算。

**状态**：`dp(n)` 表示 n 个结点能组成多少种 BST。

**递推**：根取 i（从 1 到 n），左子树有 **i-1** 个结点（i 自己用作根），右子树有 **n-i** 个结点。左边 x 种、右边 y 种，两两组合共 **x × y** 种，相当于两层 for 循环。把所有 i 的结果加起来就是 `dp(n)`。

**base case**：`n <= 1` 时为 1，空树也算一种。

时间 O(n²)：n+1 个子问题，每个子问题内部循环 n 次。

## 三、例 2：91. 解码方法

A~Z 编码为 1~26，求一串数字有多少种解码方式。`"12"` 有 AB、L 两种；`"226"` 有 BZ、VF、BBF 三种。

- 和单词拆分很像：切一刀后右边固定，左边继续拆。但这道题右边**最多只有两位**，所以**只需回头看两个子问题**。
- **状态**：`dp(n)` 表示前 n 个字符的解码方式数。
- **递推**：
  - 最后 1 个字符合法（不是 `'0'`），则 `+ dp(n-1)`；
  - 最后 2 个字符合法（**10～26**），则 `+ dp(n-2)`。
- **特殊情况**：`"10"` 只能解码为 J，因为单个 0 不合法；`"27"` 只能解码为 BG，因为 27 超过了 26。
- **base case**：`n == 0` 时空串算 1 种；`n == 1` 时，字符是 `'0'` 返回 0，否则返回 1。
- 注意下标：n 表示长度，所以最后一个字符是 `s[n-1]`。

## 四、两种写法对比

| | Bottom-up DFS + 记忆化（推荐） | 正向填表 |
| --- | --- | --- |
| 思路 | 从最大的问题出发，拆成子问题，递归到 base case 再返回 | 先填 base case，从小到大一层层填到最终问题 |
| 代码 | 稍长 | 更短 |
| 理解 | **符合人类思维**：大问题 → 拆小 → 再拆小 | "反人类"：从答案的最底层倒着往上推 |

两种写法的代码都放在了下面，答案完全一致。讲者推荐先用 DFS 写对，熟练后再改成填表。

## 五、完整代码

包括视频例题 96、91（各两种写法），以及视频推荐列表里的同类 1D DP 题：198 打家劫舍、322 零钱兑换、140 单词拆分 II。
140 题不是求数值，而是**列出所有方案**。讲者提醒，逻辑和 139 一样，只是 memo 里存的东西从"真/假"变成了"所有拆法的列表"。

```python
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
```

运行 `python ep14_dp_1d.py` 的实际输出：

```text
96  num_trees(n=1..6)       -> [1, 2, 5, 14, 42, 132]
96  num_trees_table(n=1..6) -> [1, 2, 5, 14, 42, 132]
91  num_decodings('12') -> 2 | 填表版 -> 2
91  num_decodings('226') -> 3 | 填表版 -> 3
91  num_decodings('06') -> 0 | 填表版 -> 0
91  num_decodings('10') -> 1 | 填表版 -> 1
91  num_decodings('27') -> 1 | 填表版 -> 1
91  num_decodings('2101') -> 1 | 填表版 -> 1
198 rob([2,7,9,3,1]) -> 12
322 coin_change([1,2,5], 11) -> 3 | coin_change([2], 3) -> -1
140 word_break_ii('catsanddog', [cat,cats,and,sand,dog]) -> ['cat sand dog', 'cats and dog']
```

## 本集要点
- 1D DP 的状态通常是"前 n 个"或"大小为 n"。
- 画搜索树找重复子问题；关键观察往往是**答案只和某个量有关**，比如 96 题只和区间大小有关。
- 递推规则：枚举最后一步怎么切。96 题枚举根的位置，91 题只看最后 1 位或最后 2 位。
- 推荐 Bottom-up DFS + 记忆化，它和正向填表等价，但更好理解。


---

# 第 15 集：二维动态规划 2D DP（入门）

## 一、2D DP 的四种常见情况

| 输入 | 状态 | 难度 | 所在集 |
| --- | --- | --- | --- |
| 一个二维数组 | `(row, col)`，需要两个下标描述位置 | 较简单 | 本集 |
| 两个一维数组 | `(i, j)`，各负责一个数组；**看到两个一维数组输入，基本就是 2D** | 较简单 | 本集 |
| 一个一维数组 + k | `(i, k)`，多一个 k 维度 | 变化多 | 第 16 集 |
| 一个一维数组，状态是区间 | `(i, j)` 表示子数组 `[i..j]` | 变化多 | 第 16、17 集 |

依然是：**定义好状态，从中间状态出发想递推规则。**

## 二、例 1：63. 不同路径 II

机器人从左上角出发，**只能往右或往下**走，网格中有障碍物，求走到右下角的路径数。

- **状态**：`dp(i, j)` 表示从 (0,0) 走到 (i,j) 的路径数。
- **递推**：只能往右、往下走，反过来说，到达 (i,j) 只能**从上边或左边过来**，所以 `dp(i,j) = dp(i-1,j) + dp(i,j-1)`。
- **重复子问题**：(3,3) 会问 (2,3) 和 (3,2)，它们又都会问 (2,2)。
- **base case**：
  - (0,0) 是起点，记为 1；
  - 越界或是障碍物，记为 0，这样的状态不会再往下展开。
- 入口：`dfs(m-1, n-1)`，也就是终点。

### 正向填表 + padding 技巧
多开一行一列并全部填 0，这样计算 `i-1`、`j-1` 时永远不会越界，可以省掉越界判断，越界的位置等于加了 0。代价是 dp 表和原数组的**下标错开一位**，访问原数组时要写 `grid[i-1][j-1]`。

## 三、例 2：1143. 最长公共子序列（LCS）

- **子序列**可以不连续，但**顺序不能乱**；**子数组**必须连续。
  - `"abcde"` 和 `"ace"` 的 LCS 是 `"ace"`，长度为 3。
  - `"ac"` 和 `"ca"` 的 LCS 长度只有 1，顺序不能颠倒。
- 这道题的递归树不太直观，所以**先定义状态**：`dp(i, j)` 表示 `text1[0..i]` 和 `text2[0..j]` 的 LCS 长度。
- **只需回头看一个字符**：回头看两个字符的情况，已经包含在连续回头看两次一个字符里了。
  - **最后两个字符 c1 == c2**：这对字符一定可以用上，`dp(i,j) = dp(i-1,j-1) + 1`。两个字符都用掉了，所以两边各砍掉一个。
  - **c1 != c2**：两者不可能同时用上，丢掉其中一个，`dp(i,j) = max(dp(i-1,j), dp(i,j-1))`。这里**不加 1**，只是继承较好的那个答案。
    - 比如 `abc` 和 `abd`：c 和 d 不相等，丢掉一个后，`ab` 和 `abd` 的 LCS 为 2。
    - 只要 i、j 中有一个变小，就是更小的子问题。
- **base case**：i 或 j 越界，相当于有一个是空串，LCS 为 0。
- **重复子问题**：(4,2) 会展开 (3,2)，(3,3) 也会展开 (3,2)。

## 四、为什么推荐 DFS + 记忆化，而不是正向填表？

- DFS 写法**只需要知道"当前要向哪些子问题要答案"**，比如向左、上、左上要答案。**填表顺序是递归自动决定的**，不需要操心。
- 正向填表**必须有大局观**：要先想清楚表的填充顺序，是从左到右、从上到下，还是**斜着填**，否则写不出那两层 for 循环。
  - 本集两题都向"左、上、左上"要答案，所以填表顺序是从左到右、从上到下，比较直观。
  - 后面区间类的 2D DP 需要**沿对角线斜着填**，正向写法会难很多。

## 五、完整代码

包括视频例题 63、1143（各两种写法），视频推荐的"最长公共子数组"（LeetCode 上是 718 题：最长重复子数组）。和 LCS 的区别是：子数组要求连续，字符不相等时直接归零，答案取整张表的最大值。另外补充了经典的 72 编辑距离。

```python
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
```

运行 `python ep15_dp_2d.py` 的实际输出：

```text
63   unique_paths_with_obstacles([[0,0,0],[0,1,0],[0,0,0]]) -> 2 | 填表版 -> 2
63   4x4、(3,1) 是障碍 -> 16 | 填表版 -> 16
1143 LCS('abcde', 'ace') -> 3 | 填表版 -> 3
1143 LCS('abc', 'abc') -> 3 | 填表版 -> 3
1143 LCS('abc', 'def') -> 0 | 填表版 -> 0
1143 LCS('ac', 'ca') -> 1 | 填表版 -> 1
718  find_length([1,2,3,2,1], [3,2,1,4,7]) -> 3
72   min_distance('horse', 'ros') -> 3
```

## 本集要点
- 2D DP 有四种情况；二维矩阵、两个一维数组这两种最入门。
- 矩阵路径类题：看清"只能从哪里来"，就能写出递推规则。
- LCS 类题：只看最后一个字符，相等则 +1 并两边各砍一个，不相等则二选一继承较大值。
- padding 技巧可以省掉越界判断；DFS 写法不用操心填表顺序，这是它的最大优势。


---

# 第 16 集：二维 DP 进阶——一维数组、二维状态（区间 DP）

> 本集的重点是：**输入是一维数组，但状态需要两个指针 `(i, j)` 来表示一段子数组。**

## 一、例 1：877. 石子游戏

一排石子堆，Alex 和 Lee 轮流**从头或尾**拿走一堆，Alex 先手。Alex 的总数**严格大于**对方才算赢。题目要求考虑所有可能性：只要有一种情况下 Alex 输了或打平，就返回 false。

例：`[5,3,4,5]`，Alex 无论怎么拿都能赢，所以返回 True。

### 为什么 1D 不行？

1D 状态只有一个指针，另一端是**固定**的，隐含为 0 或 n。这道题两头都能拿：拿走头部后左边界要移动，拿走尾部后右边界要移动，一个指针表示不了。**必须用 `(i, j)` 两个指针表示剩下的子数组。**

### 状态与递推
- **状态**：`dp(i, j)` 表示面对 `piles[i..j]` 时，**当前玩家**能拿到的**最大相对分**，即自己的分减去对手的分。
- **为什么用相对分**：用相对分只需要"两层相减"，比分别记录两个人的绝对分简单得多。
- **递推**：这道题的递推规则题目已经给出了，就是拿头或拿尾，再"套一层外壳"取最大值：
  - 拿头：`piles[i] - dp(i+1, j)`。拿完后轮到对手，对手的最大相对分要从我的分里减掉。
  - 拿尾：`piles[j] - dp(i, j-1)`。
- **base case**：`i == j` 时只剩一堆，返回 `piles[i]`；`i > j` 时是空区间，返回 0（平手）。
- **最终判断**：`dp(0, n-1) > 0` 才算赢，等于 0 是平手。
- memo 是 n×n 的表，因为两个指针各有 n 种取值。

### 正向填表：沿对角线斜着填

- `dp(i, j)` 依赖 `dp(i+1, j)` 和 `dp(i, j-1)`，也就是**长度少 1 的区间**。所以必须把长度为 1 的区间全部算完，才能算长度为 2 的，依此类推。
- 在表上的样子：先填对角线（长度为 1），再填旁边一条对角线……最后填到右上角 `(0, n-1)`。
- **推荐的模板**：
  ```
  for length in 2..n:              # 外层：区间长度（长度 1 是 base case）
      for i in 0..n-length:        # 内层：左端点，要给右端点留出空间
          j = i + length - 1       # 右端点由 i 和 length 算出来
          套用递推规则
  ```
- 讲者说：外层循环放长度、`j = i + length - 1` 这种写法，没见过的话很难自己想出来。而 DFS 写法也是按对角线填表的，但你完全不用操心这件事，所以**仍然推荐 DFS + 记忆化**。

## 二、例 2：5. 最长回文子串（高频，难点在于要"绕一个弯"）

- **暴力**：O(n²) 个子串，每个用 O(n) 判断是否回文，共 O(n³)。
- 和子串有关，1D 做不了，所以用 `(i, j)`。

### 难点 1：状态不是"题目问什么就定义什么"
- 一般题目问什么就定义什么，但这里如果定义成"最长回文"很难递推。
- 正确的**状态**：`dp(i, j)` 表示 `s[i..j]` **是不是回文**。
- **递推**：回文就像剥洋葱，从外往里一层层比较，所以 `s[i] == s[j]` **并且** `dp(i+1, j-1)` 为真时，当前区间是回文。
- **base case**：长度 ≤ 1 都算回文，单个字符和空串都是。
- 用一个**全局变量**记录找到的最长回文。

### 难点 2：只按上面的递推会漏掉答案
- 从 `(0, 5)` 出发只会递归到 `(1, 4)`，再到 `(2, 3)`。但长度为 4 的子区间其实有**三个**：`(0,3)`、`(1,4)`、`(2,5)`，就像一个滑动窗口。如果答案恰好在 `(0,3)` 里，就漏掉了。
- 解决办法：**每个长度为 L 的区间，还要递归两个长度为 L-1 的区间**，也就是去掉头的 `(i+1, j)` 和去掉尾的 `(i, j-1)`。这样所有子区间都会被覆盖，同时出现大量重复子问题，正好用 DP 优化。
- **小优化（if/else）**：如果当前区间已经是回文，更短的子区间不可能更长，就不用再递归那两个子区间。最坏复杂度不变。

时间 O(n²)。

## 三、完整代码

包括视频例题 877、5（各两种写法），补充同一类型的推荐题：486 预测赢家（和 877 同一个模型，平手也算玩家 1 赢）、516 最长回文子序列。
`"babad"` 的答案 `"bab"` 和 `"aba"` 都正确。DFS 版和填表版遍历顺序不同，所以返回的回文不一样，这是正常的。

```python
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
```

运行 `python ep16_dp_interval.py` 的实际输出：

```text
877 stone_game([5, 3, 4, 5]) -> True | 填表版 -> True
877 stone_game([3, 7, 2, 3]) -> True | 填表版 -> True
877 stone_game([1, 5, 2]) -> False | 填表版 -> False
486 predict_the_winner([1,5,233,7]) -> True | [1,5,2] -> False
5   longest_palindrome('babad') -> 'aba' | 填表版 -> 'bab'
5   longest_palindrome('cbbd') -> 'bb' | 填表版 -> 'bb'
5   longest_palindrome('a') -> 'a' | 填表版 -> 'a'
5   longest_palindrome('forgeeksskeegfor') -> 'geeksskeeg' | 填表版 -> 'geeksskeeg'
516 longest_palindrome_subseq('bbbab') -> 4
```

## 本集要点
- 能从两头操作，或者和"子串、子数组"有关的题，状态用区间 `(i, j)`。
- 博弈题用**相对分**：`max(拿头 - 对手的 dp, 拿尾 - 对手的 dp)`。
- 区间 DP 的填表顺序是**按长度从小到大**，在表上就是沿对角线斜着填；DFS 写法会自动处理这一点。
- 最长回文子串：状态是"是否回文"，再用全局变量记录最长的一个；记得递归两个"少一个字符"的子区间，否则会漏掉答案。


---

# 第 17 集：二维 DP 高级——一维数组 + k

> 这是 2D DP 的最后一集，面试中大部分常见的 DP 题型到这里就讲完了。
> 更难的还有"一维数组、二维状态再加 k"，也就是 3D 状态，属于进阶内容，本系列不展开。

本集的状态是**"一维状态 + k"**：一个维度表示"前 n 个元素"，另一个维度表示 k，比如分几组、最多几笔交易。

## 一、例 1：410. 分割数组的最大值

把数组分成 m 个连续子数组，使**各组和的最大值**尽可能小。

例：`[7,2,5,10,8]` 分成 2 组，共有 4 种切法：

| 切法 | 两组的和 | 最大值 |
| --- | --- | --- |
| 7 \| 2,5,10,8 | 7, 25 | 25 |
| 7,2 \| 5,10,8 | 9, 23 | 23 |
| 7,2,5 \| 10,8 | 14, 18 | **18** |
| 7,2,5,10 \| 8 | 24, 8 | 24 |

所有最大值里取最小的，答案是 **18**。

### 状态与 base case
- **状态**：`dp(m, n)` 表示把**前 n 个数**分成 **m 组**时，最大组和的最小值。
- **base case**：
  - `m == 1`：只分一组，答案就是前 n 个数的总和；
  - `m > n`：n 个数分不出 m 组，状态不合法。

### 递推：借用 139 单词拆分的思路
- **切一刀**：右边 `nums[k..n-1]` 自成一组，**不再细分**；左边前 k 个数**递归**，分成 **m-1** 组。因为切了一刀就多出一组，剩下的只需分 m-1 组。
- 这一种切法的答案是 `max(dp(m-1, k), 右边的和)`。
- **枚举所有切点 k ∈ [1, n)**，取最小值。必须真的切一刀，左右两边都不能为空，所以 k 不能取 0，也不能取 n。
- **前缀和**可以 O(1) 求出右边的和，不懂前缀和可以先做 **303. 区域和检索**。正向填表时，第一行的 base case 本身就是前缀和，不用另外开数组。
- 时间 O(m·n²)。

> 讲者提到：这道题的**最优解其实是二分查找**，见第 3 集"在答案区间上二分"，复杂度 O(n log(sum))。本集只讲 DP 解法。

## 二、例 2：188. 买卖股票的最佳时机 IV（Hard）

最多完成 k 笔交易，同一时间最多持有一股，必须先买后卖，求最大利润。
- `k=2, [2,4,1]`：2 买 4 卖，利润为 2。
- `k=2, [3,2,6,5,0,3]`：2 买 6 卖赚 4，0 买 3 卖赚 3，总共 7。

### 状态与 base case
- **状态**：`dp(k, n)` 表示用前 n 天的价格、**最多** k 笔交易能赚的最多钱。
- **base case**：`k == 0` 时没有交易次数，赚 0；`n <= 1` 时只有 0 天或 1 天，也赚 0。
- **小技巧**：`k >= n/2` 时，两天才能组成一笔交易，所以等于**不限交易次数**，直接用 **122 题**（股票 II）的贪心法：把每一段上涨都吃下来。LeetCode 的数据里 k 可能非常大，这一步能避免状态爆炸。

### 递推：多了一步"继承"
- 大问题和子问题的**唯一区别在于最后一天**。所以只需要回头看一个元素。
- **继承**：第 n 天不交易，直接继承 `dp(k, n-1)`。因为题目说的是**最多** k 笔，可以不做。
- **在第 n 天卖出**：枚举买入日 i，利润为 `dp(k-1, i) + prices[n-1] - prices[i-1]`。前 i 天用 k-1 笔交易，再加上这一笔。
- 所有候选答案取最大值。
- 搜索树中同样有大量重复子问题，比如"3 个价格、最多 2 笔"这个状态会出现多次。

时间 O(k·n²)。讲者提到可以用"滚动更新"去掉最内层循环，优化到 **O(k·n)**，但面试一般不会要求。代码中附上了这个优化版。

## 三、完整代码

```python
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
```

运行 `python ep17_dp_array_k.py` 的实际输出：

```text
410 split_array([7, 2, 5, 10, 8], m=2) -> 18 | 填表版 -> 18
410 split_array([1, 2, 3, 4, 5], m=2) -> 9 | 填表版 -> 9
410 split_array([7, 4, 2, 5, 8], m=4) -> 8 | 填表版 -> 8
188 max_profit(k=2, [2, 4, 1]) -> 2 | 填表版 -> 2 | O(kn) 版 -> 2
188 max_profit(k=2, [3, 2, 6, 5, 0, 3]) -> 7 | 填表版 -> 7 | O(kn) 版 -> 7
188 max_profit(k=3, [3, 2, 6, 5]) -> 4 | 填表版 -> 4 | O(kn) 版 -> 4
188 max_profit(k=100, [1, 3, 2, 8]) -> 8 | 填表版 -> 8 | O(kn) 版 -> 8
```

## 推荐练习
讲者说这一类"一维数组 + k"的题，除了股票系列前几道，**后面基本全是 Hard**，但都是同一个套路：切一刀，右边固定，左边带着 k-1 递归。另外这类题还涉及**背包问题**，是更进阶的内容，可以留作后续研究。

## 本集要点
- "一维数组 + k"的状态：`(前 n 个元素, k)`。
- 套路：**切一刀，右边固定，左边用 k-1 递归**，枚举所有切点取最优。
- 题目说"最多 k 次"时，记得加上"不做、直接继承"这个分支。
- 用前缀和加速区间求和；k 很大时退化为不限次数的简单情况。
- **DP 的难点永远是定义状态和递推规则**，代码都是同一个模板。


---

# 第 18 集：回溯 Backtracking

## 一、回溯是什么

- 回溯是 DFS 的一种形式，写法类似 **Top-down DFS**，但多了一个**状态回溯**的概念。
- 搜索每条分支前先记录当前状态；**试完一条分支后，要把状态恢复成当前结点的样子**，再去试下一条分支。
- **为什么要回溯**：不回溯的话，A 分支修改过的状态会被带进 B 分支。A、B 本来是**相互独立**的，就会互相干扰，导致结果出错。

### 直观例子：根到叶子的路径
视频中的树是 1 → 2 → {3, 4, 5}，期望得到 123、124、125。
- 状态（路径）一路往下走：`[1] → [1,2] → [1,2,3]`，到达叶子后加入答案。
- **如果不回溯**，回到 2 再去走 4 的分支，状态就变成了 `[1,2,3,4]`。3 被带进了 4 的分支，这是错的。
- **正确做法**：从 3 返回时把 3 弹出，状态恢复成 `[1,2]`，再去走 4，得到 `[1,2,4]`。
- 代码中用一棵二叉树演示了"正确回溯"和"忘记回溯"的对比。

## 二、回溯模板：记录 → 递归 → 回溯

```
backtrack(state):
    1. 检查 base case
    2. 对每条分支 / 每种可能性：
        a. 记录（修改）当前状态 → 得到下一个状态
        b. backtrack(下一个状态)
        c. 回溯：恢复成 a 之前的状态
```

模板很短，但和 DP 一样，**每道题的状态是什么、怎么记录、怎么回溯都不一样**，需要多练。

## 三、例 1：46. 全排列（元素互不相同）

- **数学本质**：n 个元素有 **n!** 种排列。第 1 个位置有 n 种选择，第 2 个位置剩 n-1 种……乘到 1 为止。我们要做的就是**模拟这个过程**。
- **画递归树**：第 k 层对应下标 k-1 这个位置。第 1 层有 n 个分支，第 2 层每个结点有 n-1 个分支……叶子共 n! 个。
- **状态** = 数组当前的排列 + `index`（当前要填的位置）。`index` 之前的位置已经固定。
- **交换技巧**：要把 `nums[i]` 放到 `index` 位置，直接 **swap** 两者。被挤走的元素正好放进 `nums[i]` 空出来的位置，不需要额外的缓冲区，元素总数也不变。
- **base case**：`index == n`，把**数组的副本**加入答案。不复制的话，答案里存的全是同一个引用，最后会是 n! 个一模一样的数组。
- **回溯**：递归返回后**再 swap 回来**。
- 时间、空间都是 O(n!)，因为要返回 n! 个结果。

## 四、例 2：47. 全排列 II（有重复元素）

- `[1,1,2]` 不查重的话会产生两个 `[1,1,2]`：第一个 1 在前和第二个 1 在前，结果其实一样。
- **查重机制**：在**同一层**尝试各种可能时，用一个 `set` 记录这一层放到 `index` 上用过的**值**。值已经用过就**跳过这个分支**，也就是剪枝。
- 为什么能剪：第一个位置都是 2 时，后面剩下的 `[1,2]` 和 `[2,1]` 看起来不同，但它们继续往下搜，得到的排列集合完全一样。
- 代码只比 46 题多了两行：初始化 `set`，以及 `if` 判断。

## 五、完整代码

包括视频的路径例子、46、47，以及补充的两道经典回溯题：39 组合总和（排序后剪枝）、51 N 皇后。

```python
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
```

运行 `python ep18_backtracking.py` 的实际输出：

```text
根到叶子路径（正确回溯） -> [[1, 2, 3], [1, 2, 4], [1, 5]]
根到叶子路径（忘记回溯） -> [[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]] <- 3 被带进了 4 的分支
46 permute([1,2,3]) -> [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
47 permute_unique([1,1,2]) -> [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
   对比：不查重 permute([1,1,2]) 有 6 个（含重复）
39 combination_sum([2,3,6,7], 7) -> [[2, 2, 3], [7]]
51 solve_n_queens(4) 共 2 种解，第一种：
      .Q..
      ...Q
      Q...
      ..Q.
```

## 本集要点
- 回溯 = Top-down DFS + **状态回溯**，核心三步：**记录 → 递归 → 回溯**。
- 到达 base case 时加入答案的必须是**副本**。
- 排列题可以用 swap 原地选元素，回溯时再换回来。
- 有重复元素时，在**同一层**用 set 去重，剪掉重复的分支。
- 代码不长，难点在于想清楚状态以及什么时候回溯，需要多练。


---

# 全系列总结：LeetCode 刷题套路的知识地图

## 一、一张表看完 18 集

| 集 | 专题 | 看到什么想到它 | 核心模板 / 一句话套路 | 代表题 |
| --- | --- | --- | --- | --- |
| 1 | 方法论 | — | 先打基础，再**按模块**刷题，最后用模拟面试练表达 | — |
| 2 | 双指针 | 数组原地修改、去重、有序数组找两数 | 同向：`[0,i)` 是结果，保持相对顺序；相向：每轮至少动一个指针 | 26, 283, 344, 11 |
| 3 | 二分查找 | 有序区间、"最小的可行值" | 两大原则：**每次缩小区间、不排除潜在答案**；三模板 `<=` / `<` / `<r-1` | 34, 1062, 410, 1011 |
| 4 | 链表 | 链表题 | 快慢指针（定义好间隔和速度）+ 自底向上递归三部曲 | 876, 19, 206, 25 |
| 5 | 栈 | 需要"回头看"之前的状态、下一个更大元素 | **定义好栈的含义**，单调性从定义推出 | 739, 735, 84 |
| 6 | 堆 | Top K、多路归并、数据流 | **大小为 k 的堆**，堆顶是分水岭 | 215, 23, 295 |
| 7 | 哈希表 | 需要快速查找 | 想清楚**查找对象**（key 和 value 各存什么） | 1, 560, 3 |
| 8 | 树 BFS | 和层数有关 | 队列 → 记下 size → 逐个取出并按顺序展开 → 层数 + 1 | 102, 104, 199 |
| 9 | 树 DFS | 树的大多数题 | Bottom-up 五步（向子问题要答案）/ Top-down（参数往下传） | 104, 124, 129, 236 |
| 10 | 图 BFS | 等权图最短路径、隐式图 | **所有起点**入队 + visited 查重；多源 BFS | 542, 127, 994 |
| 11 | Best-First（Dijkstra） | 边权不同的最短路径 | 队列换成**最小堆**；**弹出时**查重 | 743, 787 |
| 12 | 图 DFS | 连通块、需要遍历所有边 | A/C 校验二选一，B/D 前序、后序按题意选 | 200, 332, 207 |
| 13 | 搜索 → DP | 求所有方案 / 求最优 | **DP = 搜索 + 记忆化**；Top-down 要恢复状态 | 78, 139 |
| 14 | 1D DP | 单个数组、"前 n 个" | `dp(n)` 回头看若干个更小的子问题 | 96, 91, 198 |
| 15 | 2D DP | 矩阵、两个字符串 | `dp(i,j)` 看左、上、左上；LCS 只看最后一个字符 | 63, 1143, 72 |
| 16 | 区间 DP | 两头操作、子串、回文 | `dp(i,j)` 表示区间；按长度从小到大（沿对角线填表） | 877, 5, 516 |
| 17 | 数组 + k | 分 k 组、最多 k 笔交易 | **切一刀**，右边固定，左边带着 k-1 递归 | 410, 188 |
| 18 | 回溯 | 列出所有排列、组合、方案 | **记录 → 递归 → 回溯**；同一层用 set 去重 | 46, 47, 51 |

## 二、贯穿全系列的五条主线

1. **按模块刷，不按难度刷。**每个专题先掌握"识别特征 + 模板"，再用例题巩固。按 Easy、Medium、Hard 随机刷，很难形成体系。

2. **一切从"定义"开始。**
   - 双指针：`i` 的含义是"下一个可以填充的位置"；
   - 栈：栈里存的是什么；
   - 哈希表：查找对象是什么；
   - 递归 / DFS / DP：**状态**是什么、返回值是什么含义。
   定义清楚后，单调性、遍历方向、递推规则都能推出来。讲者在多集里反复强调："定义好状态是最难，也是最重要的一步。"

3. **递归的信念：相信你的递归函数是对的。**
   - 链表反转、树的 Bottom-up、图的后序遍历、DP，都是"把子问题当黑盒，只想当前这一层"。
   - Bottom-up 的"向子问题要的答案"和"返回给父问题的答案"，**含义必须一致**。

4. **搜索家族是一棵树。**
   ```
   搜索 Search
   ├── BFS（队列）      → 树按层 / 图的等权最短路径
   ├── Best-First（堆） → 图的带权最短路径 Dijkstra
   └── DFS（递归）
       ├── Top-down：参数往下传；需要恢复状态 → 回溯 Backtracking
       └── Bottom-up：返回值往上传；有重复子问题 → 记忆化 → 动态规划 DP
   ```

5. **复杂度要从全局看。**
   - 单调栈里 for 套 while 仍然是 O(n)，因为每个元素只进栈、出栈各一次；
   - DP 的复杂度 = 子问题个数 × 每个子问题的工作量；
   - 回溯的复杂度通常等于答案的个数，比如全排列是 O(n!)。

## 三、常见易错点清单

| 易错点 | 出现在 |
| --- | --- |
| 二分查找出现 `l = mid` 却没让 mid 偏右，导致死循环 | 第 3 集 |
| 快慢指针只判断了 `j`，没判断 `j.next` | 第 4 集 |
| 反转链表时先断开 `next`，就找不到下一个结点了 | 第 4 集 |
| Top K 写成 `>`，重复元素只算了一次 | 第 6 集 |
| 前缀和哈希表忘了预存 `{0: 1}` | 第 7 集 |
| BFS 没先记录 size，把下一层也算进了当前层 | 第 8 集 |
| 124 题把"人字形"路径返回给了父结点 | 第 9 集 |
| Dijkstra 在入堆时查重，丢掉了更优的路径 | 第 11 集 |
| 332 题用前序遍历，走进了死胡同 | 第 12 集 |
| 回溯没有恢复状态，或者加入答案时没有复制 | 第 13、18 集 |
| 最长回文子串只递归 `(i+1, j-1)`，漏掉了答案 | 第 16 集 |

## 四、关于语言

视频讲者推荐用 Java 面试。本笔记全部改用 **Python** 实现，所有代码都实际运行验证过。Python 版的几个对应关系：
- 栈：`list`（`append` / `pop`）
- 队列：`collections.deque`（`append` / `popleft`）
- 堆：`heapq`，只有最小堆，最大堆存相反数
- 哈希表：`dict` / `set` / `collections.defaultdict` / `Counter`
- 记忆化：`functools.lru_cache`，或者手写 `memo`

## 五、下一步

1. 按[《7 天学习路径》](notes/20-7天学习路径.md)把 18 集过一遍。
2. 每个专题的推荐练习题，都可以在 Leetcode 仓库的 [INDEX.md](https://github.com/ykkkk18/leetcode/blob/main/INDEX.md) 里按题号找到完整题解。
3. 7 天之后：每天从已学的专题中随机抽 2～3 道新题，限时 30 分钟，**先口述思路再写代码**，用来练习第 1 集说的"讲清楚思路"。
