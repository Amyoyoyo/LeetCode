class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for i,val in enumerate(nums):
            if dict.get(target-val) is not None:
                return i,dict.get(target-val)
            else:
                dict[val]=i

'''
执行用时 :64 ms, 在所有 Python 提交中击败了65.16%的用户
内存消耗 :13.1 MB, 在所有 Python 提交中击败了16.60%的用户
'''








if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    sol=Solution()
    ans=sol.twoSum(nums,target)
    print(ans)
