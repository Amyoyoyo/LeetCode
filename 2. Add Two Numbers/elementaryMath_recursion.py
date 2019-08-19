class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2,dummyHead=ListNode(0),carry=0):
        pointer=dummyHead
        if l1 or l2 or carry:
            carry,sum=divmod((l1.val if l1 else 0)+(l2.val if l2 else 0)+carry,10)
            pointer.next=ListNode(sum)
            pointer=pointer.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            self.addTwoNumbers(l1,l2,pointer,carry)
            return dummyHead.next
        else:
            return None

'''
Runtime: 44 ms, faster than 97.92% of Python online submissions for Add Two Numbers.
Memory Usage: 12.1 MB, less than 5.88% of Python online submissions for Add Two Numbers.
'''

if __name__ == '__main__':
    l1=ListNode(2)
    l1.next=ListNode(4)
    l1.next.next=ListNode(3)
    l2=ListNode(5)
    l2.next=ListNode(6)
    l2.next.next=ListNode(4)

    sol=Solution()
    ans=sol.addTwoNumbers(l1,l2)
    pointer=ans
    while pointer is not None:
        print(pointer.val)
        pointer=pointer.next

