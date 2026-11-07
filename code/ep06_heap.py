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
