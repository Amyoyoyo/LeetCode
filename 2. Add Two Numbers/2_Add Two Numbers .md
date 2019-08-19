#题目-两数相加
>【英文版】https://leetcode.com/problems/add-two-numbers/
>【中文版】https://leetcode-cn.com/problems/add-two-numbers/<br>

给出两个**非空**的链表用来表示两个非负的整数。其中，它们各自的位数是按照**逆序**的方式存储的，并且它们的每个节点只能存储**一位**数字。<br>如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。<br>您可以假设除了数字 0 之外，这两个数都不会以 0 开头。<br>
**示例**
>输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
>输出：7 -> 0 -> 8
>原因：342 + 465 = 807
>"""
>:type l1: ListNode
>:type l2: ListNode
>:rtype: ListNode
>"""
>Definition for singly-linked list.
>class ListNode(object):
>&emsp;&emsp;def \_\_init\_\_(self, x):
>&emsp;&emsp;&emsp;&emsp;self.val = x
>&emsp;&emsp;&emsp;&emsp;self.next = None

#暴力求解
先求出输入链表`l1`,`l2`的和(traverse(self,l)),再用取余除10的方法逐个取出和的位数放入链表。
★ 时间复杂度：$O(max(m,n))$
★ 空间复杂的：$O(max(m,n))+1$
<details>
<summary>Brute Force -python-1</summary>

<pre><code>
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

        remainder = sum % 10
        result=ListNode(remainder)
        sum = int(sum/10)
        pointer=result
        while sum>0:
            remainder=sum%10
            pointer.next=ListNode(remainder)
            pointer=pointer.next
            sum =int(sum/10)
        return result
</code></pre>
执行用时 :64 ms, 在所有 Python 提交中击败了73.10%的用户<br>内存消耗 :11.8 MB, 在所有 Python 提交中击败了27.89%的用户<br>
代码可精简部分<br>1. 将返回链表初始化为哑结点，否则要写重复的语句要初始化表头的值
&nbsp;
</details>
<details>
<summary>Brute Force -python-2</summary>

<pre><code>
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
</code></pre>
Runtime: 60 ms, faster than 41.80% of Python online submissions for Add Two Numbers.<br>Memory Usage: 11.8 MB, less than 60.29% of Python online submissions for Add Two Numbers.
</details>
&nbsp;

# 初等数学
该问题实际为大数相加问题，若数值过大，暴力求解可能会出现问题。应使用变量`carry`来跟踪进位，并从包含最低有效位的表头开始模拟逐位相加的过程。
<img src="https://raw.githubusercontent.com/Amyoyoyo/media/master/blog/20190819124959.png">
就像在纸上计算两个数字的和那样，我们首先从最低有效位也就是列表`l1`和`l2`的表头开始相加。由于每位数字都应当处于`0 …… 9`的范围内，我们计算两个数字的和时可能会出现 “溢出”。例如，`5 + 7 = 12`。在这种情况下，我们会将当前位的数值设置为`2`，并将进位`carry=1`带入下一次迭代。进位`carry`必定是`0`或`1`，这是因为两个数字相加（考虑到进位）可能出现的最大和为`9 + 9 + 1 = 19`。[^LeetCode]
<img src="https://raw.githubusercontent.com/Amyoyoyo/media/master/blog/Add%20Two%20Numbers.gif">[^gif]
★ 时间复杂度：$O(max(m,n))$
★ 空间复杂的：$O(max(m,n))+1$
<details>
<summary>Elementary Math -python-1</summary>

<pre><code>
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
</code></pre>
Runtime: 48 ms, faster than 93.27% of Python online submissions for Add Two Numbers.<br>Memory Usage: 11.9 MB, less than 47.79% of Python online submissions for Add Two Numbers.<br>
代码可精简部分<br>1. 用`divmod()`函数代替判断语句和%=<br>2.用 ? : 语句代替if else
&nbsp;
</details>
<details>
<summary>Elementary Math -python-2</summary>

<pre><code>
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry=0
        dummyHead=ListNode(0)
        pointer=dummyHead
        while l1 or l2 or carry:
            carry,sum=divmod((l1.val if l1 else 0)+(l2.val if l2 else 0)+carry,10)
            pointer.next=ListNode(sum)
            pointer=pointer.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummyHead.next
</code></pre>
Runtime: 48 ms, faster than 93.27% of Python online submissions for Add Two Numbers.<br>Memory Usage: 11.8 MB, less than 62.50% of Python online submissions for Add Two Numbers.<br>
代码可更改部分<br>1. 可用递归代替while循环
&nbsp;
</details>
<details>
<summary>Elementary Math + recursion -python</summary>

<pre><code>
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
</code></pre>
Runtime: 44 ms, faster than 97.92% of Python online submissions for Add Two Numbers.<br>Memory Usage: 12.1 MB, less than 5.88% of Python online submissions for Add Two Numbers.
</details>
&nbsp;
#各方法运行结果
方法|执行用时|击败用户|内存消耗|击败用户
-|-|-|-|-
Brute Force 1 | 64 ms|73.10%|11.8 MB|27.89%
Brute Force 2 | 60 ms|41.80%|11.8 MB|60.29%
Elementary Math 1| 48 ms|93.27%|11.9 MB|47.79%
Elementary Math 2| 48 ms|93.27%|11.8 MB|62.50%
Elementary Math + recursion| 44 ms|97.92%|12.1 MB|5.88%

#拓展
若链表中的数字不是按逆序存储的呢？[^LeetCode]
**示例**
>输入：(3 -> 4 -> 2) + (4 -> 6 -> 5)
>输出：8 -> 0 -> 7
>原因：342 + 465 = 807

#参考
[^LeetCode]: [LeetCode题解](https://leetcode-cn.com/problems/two-sum/solution/liang-shu-xiang-jia-by-leetcode/)
[^gif]: [画解算法by灵魂画师牧码](https://leetcode-cn.com/problems/add-two-numbers/solution/hua-jie-suan-fa-2-liang-shu-xiang-jia-by-guanpengc)