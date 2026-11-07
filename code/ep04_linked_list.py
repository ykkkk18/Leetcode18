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
