class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i]<target:
                i+=1
            else:
                return i
        return i

if __name__ == '__main__':
    nums=[1,3,5,6]
    target=0

    sol=Solution()
    ans=sol.searchInsert(nums,target)
    print(ans)