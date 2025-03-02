class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode()
        current = dummy
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry > 0:
            current.next = ListNode(carry)
        return dummy.next
    

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next