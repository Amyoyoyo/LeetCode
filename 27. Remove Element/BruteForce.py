class Solution(object):
    def removeElement(self, nums, val):
        i=0
        while i < len(nums):
            if nums[i]==val:
                nums.pop(i)
            i+=1
        return len(nums)

'''
Runtime: 20 ms, faster than 63.55% of Python online submissions for Remove Element.
Memory Usage: 11.8 MB, less than 52.83% of Python online submissions for Remove Element.
'''

if __name__ == '__main__':
    nums=[3,2,2,3]
    val=3
    sol=Solution()
    ans=sol.removeElement(nums,val)
    print('ans=',ans)
    print('nums=',nums)