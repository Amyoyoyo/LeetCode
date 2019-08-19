class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry=0
        dummyHead=ListNode(0)
        pointer=dummyHead
        while (l1 is not None) or (l2 is not None) or carry==1:
            if l1 is not None:
                x=l1.val
                l1=l1.next
            else:
                x=0
            if l2 is not None:
                y=l2.val
                l2=l2.next
            else:
                y=0

            sum=x+y+carry
            if carry==1:
                carry=0
            if sum>9:
                carry=1
                sum%=10
            pointer.next=ListNode(sum)
            pointer=pointer.next

        return dummyHead.next

'''
Runtime: 48 ms, faster than 93.27% of Python online submissions for Add Two Numbers.
Memory Usage: 11.9 MB, less than 47.79% of Python online submissions for Add Two Numbers.
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

