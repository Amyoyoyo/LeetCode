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
'''
Runtime: 60 ms, faster than 95.81% of Python online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 13.5 MB, less than 87.50% of Python online submissions for Remove Duplicates from Sorted Array.
'''

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    sol=Solution()
    ans=sol.removeDuplicates(nums)
    print('non-duplicated:',ans)
    for i in range(ans):
        print(nums[i])