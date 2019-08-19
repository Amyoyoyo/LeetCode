class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def traverse(self,l):
        i=1
        sum=0
        while l is not None:
            sum+=l.val*i
            i=i*10
            l=l.next
        return sum

    def addTwoNumbers(self, l1, l2):
        l1_sum=self.traverse(l1)
        l2_sum=self.traverse(l2)
        sum=l1_sum+l2_sum

        if l1 is not None or l2 is not None:
            if sum==0:
                return ListNode(0)
        dummyHead=ListNode(0)
        pointer=dummyHead
        while sum>0:
            remainder=sum%10
            pointer.next=ListNode(remainder)
            pointer=pointer.next
            sum =int(sum/10)
        return dummyHead.next

'''
Runtime: 60 ms, faster than 41.80% of Python online submissions for Add Two Numbers.
Memory Usage: 11.8 MB, less than 60.29% of Python online submissions for Add Two Numbers.
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

