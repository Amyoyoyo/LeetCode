class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for i in range(len(nums)):
            dict[str(nums[i])]=i
        for i in range(len(nums)):
            if str(target-nums[i])in dict and dict[str(target-nums[i])]!=i:
                return i,dict[str(target-nums[i])]