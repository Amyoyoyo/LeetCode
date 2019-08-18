class Solution(object):
    def twoSum(self, nums, target,i=0,dict={}):
        if dict.get(target-nums[i]) is not None:
            result=[dict.get(target - nums[i]),i]
            dict.clear()
            return result
        else:
            dict[nums[i]] = i
            i+=1
            return self.twoSum(nums,target,i,dict)

'''
执行用时 :52 ms, 在所有 Python 提交中击败了75.96%的用户
内存消耗 :20.8 MB, 在所有 Python 提交中击败了5.01%的用户
'''

if __name__ == '__main__':
    nums = [3,3]
    target = 6
    sol=Solution()
    ans=sol.twoSum(nums,target)
    print(ans)
    ans2=sol.twoSum(nums,target)
    print(ans2)