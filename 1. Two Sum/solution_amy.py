class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for i in range(len(nums)):
            dict[str(nums[i])]=i
        for i in range(len(nums)):
            if str(target-nums[i])in dict and dict[str(target-nums[i])]!=i:
                return i,dict[str(target-nums[i])]





if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    sol=Solution()
    ans=sol.twoSum(nums,target)
    print(ans)
