# 题目-删除排序数组中的重复项
>【英文版】https://leetcode.com/problems/remove-duplicates-from-sorted-array/
>【中文版】https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/<br>

给定一个排序数组，你需要在**原地**[^in-place-cn]删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。<br>不要使用额外的数组空间，你必须在**原地**[^in-place-en]修改输入数组并在使用$O(1)$额外空间的条件下完成。

**示例**
>给定数组`nums = [1,1,2]`, 
>函数应该返回新的长度`2`, 并且原数组`nums`的前两个元素被修改为`1`,`2`。 
>你不需要考虑数组中超出新长度后面的元素。
> """
>:type nums: List[int]
>:rtype: int
>"""

**说明**
>为什么返回数值是整数，但输出的答案是数组呢?
>请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
>你可以想象内部操作如下:
>nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
>int len = removeDuplicates(nums);
>在函数里修改输入数组对于调用者是可见的。
>根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
>for (int i = 0; i < len; i++) {
>&emsp;&emsp;print(nums[i]);
>}

**特殊情况**
输入为[]

#暴力求解
直接对比第`i`位与第`i+1`位的值，若相同则删除第`i+1`位，否则i+=1.
★ 时间复杂度：$O(n^2)$
数组的删除操作需要将删除位置后面的所有元素前移一位$O(n)$，遍历一遍数组，共$O(n^2)$
★ 空间复杂度：$O(1)$
<details>
<summary>Brute Force -python</summary>

<pre><code>
class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        while i!=(len(nums)-1) and nums:
            if nums[i]==nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1

        return len(nums)
</code></pre>
Runtime: 76 ms, faster than 37.59% of Python online submissions for Remove Duplicates from Sorted Array.<br>Memory Usage: 13.7 MB, less than 17.19% of Python online submissions for Remove Duplicates from Sorted Array.<br>
因为删除操作回影响数组长度，每次都要重新计算len(nums)，采用逆遍历可以避免。
</details>

#双指针
数组完成排序后，我们可以放置两个指针`i`和`j`，其中 `i`是慢指针，指向非重复的最后一个元素；而`j`是快指针，去查找下一个非重复的元素。只要`nums[i]=nums[j]`，我们就增加`j`以跳过重复项。当我们遇到`nums[i]≠nums[j]`时，跳过重复项的运行已经结束，则把`nums[j]`的值复制到`nums[i]`。然后递增`i`，接着我们将再次重复相同的过程，直到`j`到达数组的末尾为止。[^LeetCode]
<img src="https://raw.githubusercontent.com/Amyoyoyo/media/master/blog/doublepointers.gif" width=50% height=50%>
★ 时间复杂度：$O(n)$
★ 空间复杂度：$O(1)$

<details>
<summary>Double Pointers -python-1</summary>

<pre><code>
class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        j=i+1
        while j!=len(nums) and nums:
            if nums[i]==nums[j]:
                j+=1
            else:
                nums[i+1]=nums[j]
                i+=1
                j+=1
        return i+1
</code></pre>
Runtime: 60 ms, faster than 95.81% of Python online submissions for Remove Duplicates from Sorted Array.<br>Memory Usage: 13.5 MB, less than 87.50% of Python online submissions for Remove Duplicates from Sorted Array.<br>代码可精简部分：<br>1. j+=1在if和else后都出现，之间放在while循环里不同判断
&nbsp;
</details>
<details>
<summary>Double Pointers -python-2</summary>

<pre><code>
class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        j=i+1
        while j!=len(nums) and nums:
            if nums[i]!=nums[j]:
                nums[i + 1] = nums[j]
                i += 1
            j+=1
        return i+1
</code></pre>
Runtime: 60 ms, faster than 95.81% of Python online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 13.5 MB, less than 93.75% of Python online submissions for Remove Duplicates from Sorted Array.
</details>
&nbsp;
#各方法运行结果
方法|执行用时|击败用户|内存消耗|击败用户
-|-|-|-|-
Brute Force 1 | 76 ms|37.59%|13.7 MB|17.19%
Double Pointers 1 | 60 ms|95.81%|13.5 MB|87.50%
Double Pointers 2 |60 ms|95.81%|13.5 MB|93.75%



#参考
[^LeetCode]: [LeetCode](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)
[^in-place-cn]: [原地算法](https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95)
[^in-place-en]: [in-place algorithm](https://en.wikipedia.org/wiki/In-place_algorithm)
