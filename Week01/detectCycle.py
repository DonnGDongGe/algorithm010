# 环形链表2
# 方法一：快慢指针
class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast


def detectCycle(head):
    try:
        fast = head.next
        slow = head
        while fast is not slow:
            fast = fast.next.next
            slow = slow.next
    except:
        # if there is an exception, we reach the end and there is no cycle
        return None

    # since fast starts at head.next, we need to move slow one step forward
    slow = slow.next
    while head is not slow:
        head = head.next
        slow = slow.next

    return head
# 方法二：哈希表
# 首先，我们分配一个 Set 去保存所有的列表节点。我们逐一遍历列表，检查当前节点是否出现过，如果节点已经出现过，
# 那么一定形成了环且它是环的入口。否则如果有其他点是环的入口，我们应该先访问到其他节点而不是这个节点。其他情况，
# 没有成环则直接返回 null 。算法会在遍历有限个节点后终止，这是因为输入列表会被分成两类：成环的和不成环的。
# 一个不成欢的列表在遍历完所有节点后会到达 null - 即链表的最后一个元素后停止。
# 一个成环列表可以想象成是一个不成环列表将最后一个 null 元素换成环的入口。如果 while 循环终止，
# 我们返回 null 因为我们已经将所有的节点遍历了一遍且没有遇到重复的节点，这种情况下，列表是不成环的。
# 对于循环列表， while 循环永远不会停止，但在某个节点上， if 条件会被满足并导致函数的退出。

def detectCycle(head):
    visited = set()

    node = head
    while node is not None:
        if node in visited:
            return node
        else:
            visited.add(node)
            node = node.next.next

        return None
