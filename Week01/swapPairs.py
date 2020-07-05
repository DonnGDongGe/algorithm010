# 两两交换链表中的节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        thead = ListNode(-1)
        thead.next = head
        c = thead
        while c.next and c.next.next:
            a, b = c.next, c.next.next
            # c.next, a.next = b, b.next
            c.next = b
            a.next = b.next
            b.next = a
            c = c.next.next
        return thead.next


def link(linkList):
    head = ListNode(linkList[0])
    p = head
    for i in range(1, len(linkList)):
        p.next = ListNode(linkList[i])
        p = p.next
    return head


list1 = [1, 2, 3, 4]
head = link(list1)
head = Solution().swapPairs(head)
