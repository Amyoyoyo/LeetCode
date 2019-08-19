class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        while i!=(len(nums)-1) and nums:
            if nums[i]==nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1

        return len(nums)
'''
Runtime: 76 ms, faster than 37.59% of Python online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 13.7 MB, less than 17.19% of Python online submissions for Remove Duplicates from Sorted Array.
'''

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    sol=Solution()
    ans=sol.removeDuplicates(nums)
    print('non-duplicated:',ans)
    for i in range(ans):
        print(nums[i])