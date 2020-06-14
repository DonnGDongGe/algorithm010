class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list2link(List):
    head = ListNode(List[0])  #创建一个头节点并将list第一个值赋值给头结点
    p = head  #创建头指针
    for i in range(1, len(List)):  #list从第二位开始遍历
        p.next = ListNode(List[i])  #下一个结点p.next指向list值
        p = p.next  #指针往下移动
    return head  #返回头结点


old_list = [1, 2, 3, 4, 5]
link = list2link(old_list)


class Solution:
    def reverseList(self, head):
        prev = None

        curr = head

        while curr:
            next = curr.next
            curr.next = prev # cur的next节点指向空
            prev = curr
            curr = next

        return prev


Solution().reverseList(link)