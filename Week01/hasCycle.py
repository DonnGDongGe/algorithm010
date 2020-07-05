# 判断是否有循环链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 创建单向链表
def liskLink(ListNode):
    head = ListNode(ListNode[0])
    p = head
    for i in range(1, len(ListNode)):
        p.next = ListNode(ListNode[i])
        p = p.next
    return head


# 判断是否存在循环链表
def hasCycle(head):
    """借助辅助空
        理解： 用一个set数据结构存储每个节点地址;
        时间复杂度O(n*1)：访问每个节点O(n)+存储每个节点O(1);
        空间复杂度O(n)
    """
    a = set()
    while head:

        if head in a:
            return True

        a.add(head)
        head = head.next
    return False

def hasCycle1(head):
    """ 
    快慢指针：
    理解：
    思路：定义一个快指针和慢指针,每次快指针走2步，慢指针走1步，判断快指针是否与慢指针重逢
    时间复杂度O(n+k)：
    情况一：链表部分成环O(n)；
    部分成环时，快指针先于慢指针进入环，慢指针进环时间O(n)；当快慢指针都进入环，
    假设环节点数量为K,当快慢指针第一次相遇时，快指针至少已经在环内已经比慢指针多走一圈
    (多走的这一圈是当慢指针进入后开始算的)，时间O(k)； 综上，时间复杂度O(k+n)，即为O(n)
    情况二：链表完全成环O(n)
    同起点，第一次相遇时，快指针已经在环内已经比慢指针多走一圈；时间复杂度O(n)
    """=fa 
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


if __name__ == "__main__":
    links = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(3)
    p3 = ListNode(4)
    p4 = ListNode(5)
    p5 = ListNode(6)
    links.next = p1
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = p4
    print(hasCycle(links))
