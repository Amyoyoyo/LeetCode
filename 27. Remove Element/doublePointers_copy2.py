class Solution(object):
    def removeElement(self, nums, val):
        i=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i

'''
Runtime: 24 ms, faster than 32.22% of Python online submissions for Remove Element.
Memory Usage: 11.7 MB, less than 62.26% of Python online submissions for Remove Element.
'''

if __name__ == '__main__':
    nums=[3]
    val=3
    sol=Solution()
    ans=sol.removeElement(nums,val)
    print('ans=',ans)
    print('nums=',nums)