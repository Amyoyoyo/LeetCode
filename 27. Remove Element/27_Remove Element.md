# 题目-移除元素
>【英文版】https://leetcode.com/problems/remove-element/
>【中文版】https://leetcode-cn.com/problems/remove-element/<br>

给定一个数组`nums`和一个值`val`，你需要**原地**[^in-place-cn]移除所有数值等于`val`的元素，返回移除后数组的新长度。<br>
不要使用额外的数组空间，你必须在**原地**[^in-place-en]修改输入数组并在使用$O(1)$额外空间的条件下完成。<br>
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

**示例**
给定`nums = [3,2,2,3]`, `val = 3`,
函数应该返回新的长度 2, 并且 `nums` 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。

**特殊情况**
输入为[]
输入的`nums`长度为1
输入的`nums`所有值都等于`val`

# 暴力求解
从头到尾遍历，遇到`nums[i]==val`的就删除
★ 时间复杂度：$O(n^2)$
数组的删除操作需要将删除位置后面的所有元素前移一位$O(n)$，遍历一遍数组，共$O(n^2)$
★ 空间复杂度：$O(1)$
<details>
<summary>Brute Force-python</summary>

<pre><code>
class Solution(object):
    def removeElement(self, nums, val):
        i=0
        while i < len(nums):
            if nums[i]==val:
                nums.pop(i)
            i+=1
        return len(nums)
</code></pre>
Runtime: 20 ms, faster than 63.55% of Python online submissions for Remove Element.<br>Memory Usage: 11.8 MB, less than 52.83% of Python online submissions for Remove Element.
</details>

# 双指针-拷贝覆盖
与[LeetCode 26 Remove Duplicates from Sorted Array](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)的思路一样，使用双指针(慢指针i与快指针j)。
★ 时间复杂度：$O(n)$
★ 空间复杂度：$O(1)$

## 从后往前遍历
若从后往前遍历，将`nums[j]==val`的值放到后面(放到`nums[i]`)。但是从后往前遍历需要考虑较多的特殊情况。最好从前往后遍历
<details>
<summary>Double Pointers_copy -python-1</summary>

<pre><code>
class Solution(object):
    def removeElement(self, nums, val):
        if len(nums)<=1:
            if len(nums)==0: return 0  # 输入为[]的特殊情况
            if nums[0]==val:return 0  # 输入的`nums`长度为1的特殊情况
            else: return 1
        i=len(nums)-1
        j=i-1
        while j >=0:
            if nums[i]==val:
                i-=1
            elif nums[i]!=val and nums[j]==val:
                nums[j]=nums[i]
                # nums[i]=val #助理解，可注释
                i-=1
            j-=1
        if nums[j+1]==val:return 0 # 输入的`nums`所有值都等于`val`的特殊情况

        return i+1
</code></pre>
Runtime: 24 ms, faster than 32.22% of Python online submissions for Remove Element.<br>Memory Usage: 11.7 MB, less than 67.92% of Python online submissions for Remove Element.
</details>
&nbsp;
## 从前往后遍历
当 `nums[j]` 与给定的值相等时，递增`j`以跳过该元素。只要 `nums[j] ≠ val`，我们就复制`nums[j]`到`nums[i]`并同时递增两个索引。重复这一过程，直到`j`到达数组的末尾，该数组的新长度为`i`。[^LeetCode]
<img src="https://raw.githubusercontent.com/Amyoyoyo/media/master/blog/LeetCode27_doublepointer_copy.gif">[^gif]

<details>
<summary>Double Pointers_copy -python-2</summary>

<pre><code>
class Solution(object):
    def removeElement(self, nums, val):
        i=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i
</code></pre>
Runtime: 24 ms, faster than 32.22% of Python online submissions for Remove Element.<br>Memory Usage: 11.7 MB, less than 62.26% of Python online submissions for Remove Element.
</details>

# 双指针-交换移除
**思路**
现在考虑数组包含很少的要删除的元素的情况。例如，`num=[1，2，3，5，4]`，`Val=4`。之前的算法会对前四个元素做不必要的复制操作。另一个例子是 `num=[4，1，2，3，5]`，`Val=4`。似乎没有必要将 `[1，2，3，5]` 这几个元素左移一步，因为问题描述中提到元素的顺序可以更改。
**算法**
当遇到 `nums[i] = val` 时，将当前元素与最后一个元素进行交换，并释放最后一个元素。这实际上使数组的大小减少了 1。<br>
请注意，被交换的最后一个元素可能是想要移除的值。但是不要担心，在下一次迭代中，仍然会检查这个元素。[^LeetCode]
注意
需要将`j`赋值为`len(nums)`，否则需要单独考虑`nums`长度为1的情况
<img src="https://raw.githubusercontent.com/Amyoyoyo/media/master/blog/LeetCode27_doublepointer_swap.gif">[^gif]
★ 时间复杂度：$O(n)$
★ 空间复杂度：$O(1)$
<details>
<summary>Double Pointer_swap-python</summary>

<pre><code>
class Solution(object):
    def removeElement(self, nums, val):
        i=0
        j=len(nums)
        while i < j:
            if nums[i]==val:
                nums[i]=nums[j-1]
                j-=1
            else:
                i+=1
        return i
</code></pre>
Runtime: 20 ms, faster than 63.60% of Python online submissions for Remove Element.<br>Memory Usage: 11.8 MB, less than 43.40% of Python online submissions for Remove Element.
</details>

#参考
[^LeetCode]: [LeetCode](https://leetcode-cn.com/problems/remove-element/solution/)
[^in-place-cn]: [原地算法](https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95)
[^in-place-en]: [in-place algorithm](https://en.wikipedia.org/wiki/In-place_algorithm)
[^gif]: [画解算法by灵魂画师牧码](https://leetcode-cn.com/problems/remove-element/solution/hua-jie-suan-fa-27-yi-chu-yuan-su-by-guanpengchn/)