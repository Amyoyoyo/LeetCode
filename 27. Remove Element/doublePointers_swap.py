class Solution(object):
    def removeElement(self, nums, val):
        i=0
        j=len(nums)
        while i<j:
            if nums[i]==val:
                nums[i]=nums[j-1]
                j-=1
            else:
                i+=1
        return i

'''
Runtime: 20 ms, faster than 63.60% of Python online submissions for Remove Element.
Memory Usage: 11.8 MB, less than 43.40% of Python online submissions for Remove Element.
'''
if __name__ == '__main__':
    nums=[0,1,2,2,3,0,4,2]
    val=2
    sol=Solution()
    ans=sol.removeElement(nums,val)
    print('ans=',ans)
    print('nums=',nums)