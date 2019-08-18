#题目
【英文版】https://leetcode.com/problems/two-sum/<br>
【中文版】https://leetcode-cn.com/problems/two-sum/<br>
给定一个整数数组 $nums$ 和一个目标值 $target$，请你在该数组中找出和为目标值的那**两个**整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
:type nums: List[int]
:type target: int
:rtype: List[int]


#示例
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

#解法
##暴力搜索
遍历$nums$中的每一个元素$x$，查找$nums$中另一个元素$j$使得$x+j=target$
★ 时间复杂度：$O(n^2)$
&emsp;&emsp;对于每个元素，我们试图通过遍历数组的其余部分来寻找它所对应的目标元素，这将耗费$O(n)$的时间。因此时间复杂度为$O(n^2)$。
★ 空间复杂度：$O(1)$

<details>
<summary>Brute Force -python-1</summary>

<pre><code>
class Solution(object):
    def twoSum(self, nums, target):
        index1=0
        index2=0
        for i in range(len(nums)):
            ele1=nums[i]
            for j in range(i+1,len(nums)):
                lel2=nums[j]
                if ele1+lel2==target:
                    index1=i
                    index2=j
                    break
        return index1,index2
</code></pre>
结果
执行用时 :4172 ms, 在所有 Python 提交中击败了26.93%的用户<br>
内存消耗 :12.7 MB, 在所有 Python 提交中击败了25.36%的用户<br>

代码可精简部分
1. 无需定义变量index1、index2，直接在ele1+lel2==target部分return
2. 无需定义变量ele1、lel2，直接使用nums[i]、nums[j]
</details>

<details>
<summary>Brute Force -python-2</summary>

<pre><code>
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
</code></pre>
执行用时 :4996 ms, 在所有 Python 提交中击败了16.95%的用户
内存消耗 :12.4 MB, 在所有 Python 提交中击败了37.72%的用户
</details>
&nbsp;
##哈希表
• 以空间换速度
• 保持数组中的每个元素与其索引相互对应的最好方法：哈希表[^HashTable]
&emsp;&emsp;哈希表支持以**近似**恒定的时间进行快速查找。用“近似”来描述，是因为一旦出现冲突，查找用时可能会退化到$O(n)$。但只要你仔细地挑选哈希函数，在哈希表中进行查找的用时应当被摊销为$O(1)$[^LeetCode]
&nbsp;
###两遍哈希表
&emsp;&emsp;在第一次迭代中，我们将每个元素的值和它的索引添加到表中。然后，在第二次迭代中，我们将检查每个元素所对应的目标元素$(target - nums[i])$是否存在于表中。注意，该目标元素不能是$nums[i]$本身！[^LeetCode]
★ 时间复杂度：$O(n)$
&emsp;&emsp;我们把包含有$n$个元素的列表遍历两次。由于哈希表将查找时间缩短到$O(1)$，所以时间复杂度为$O(n)$。
★ 空间复杂度：$O(n)$
&emsp;&emsp;所需的额外空间取决于哈希表中存储的元素数量，该表中存储了$n$个元素。

<details>
<summary>Two-pass Hash Table -python</summary>

<pre><code>
class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for i in range(len(nums)):
            dict[str(nums[i])]=i
        for i in range(len(nums)):
            if str(target-nums[i])in dict and dict[str(target-nums[i])]!=i:
                return i,dict[str(target-nums[i])]
</code></pre>
结果
执行用时 :44 ms, 在所有 Python 提交中击败了92.95%的用户  
内存消耗 :14.2 MB, 在所有 Python 提交中击败了5.01%的用户  
</details>
&nbsp;
###一遍哈希表
在进行迭代并将元素插入到表中的同时，我们还会回过头来检查表中是否已经存在当前元素所对应的目标元素。如果它存在，那我们已经找到了对应解，并立即将其返回。[^LeetCode]
<img src="https://raw.githubusercontent.com/Amyoyoyo/media/master/leetcode/twosum_hashtable.gif" width="400px" />[^gif]

<details>
<summary>One-pass Hash Table -python</summary>

<pre><code>
class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for i in range(len(nums)):
            if str(target - nums[i]) in dict and dict[str(target - nums[i])] != i:
                return i,dict[str(target-nums[i])]
            else:
                dict[str(nums[i])] = i
</code></pre>
结果
执行用时 :84 ms, 在所有 Python 提交中击败了59.23%的用户
内存消耗 :13.9 MB, 在所有 Python 提交中击败了5.01%的用户
</details>
&nbsp;
#参考
[^LeetCode]: [LeetCode题解](https://leetcode-cn.com/problems/)
[^HashTable]: [哈希表](https://baike.baidu.com/item/%E5%93%88%E5%B8%8C%E8%A1%A8/5981869?fr=aladdin)
[^gif]: [画解算法by灵魂画师牧码](https://leetcode-cn.com/problems/two-sum/solution/jie-suan-fa-1-liang-shu-zhi-he-by-guanpengchn/)