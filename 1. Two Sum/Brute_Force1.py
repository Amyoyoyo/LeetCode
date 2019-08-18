class Solution(object):
    def twoSum(self, nums, target):
        index1=0
        index2=0
        for i in range(len(nums)):
            ele1=nums[i]
            for j in range(i+1,len(nums)):
                lel2=nums[j]
                if ele1+lel2==target:
                    index1=i
                    index2=j
                    break
        return index1,index2