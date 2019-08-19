class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for i,val in enumerate(nums):
            if dict.get(target-val) is not None:
                return i,dict.get(target-val)
            else:
                dict[val]=i









if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    sol=Solution()
    ans=sol.twoSum(nums,target)
    print(ans)
