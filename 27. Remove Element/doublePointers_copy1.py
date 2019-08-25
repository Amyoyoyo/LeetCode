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

'''
Runtime: 24 ms, faster than 32.22% of Python online submissions for Remove Element.
Memory Usage: 11.7 MB, less than 67.92% of Python online submissions for Remove Element.
'''


if __name__ == '__main__':
    nums=[3,3]
    val=2
    sol=Solution()
    ans=sol.removeElement(nums,val)
    print('ans=',ans)
    print('nums=',nums)