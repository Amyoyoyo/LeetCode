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



if __name__ == '__main__':
    nums = [3,3]
    target = 6
    sol=Solution()
    ans=sol.twoSum(nums,target)
    print(ans)
    ans2=sol.twoSum(nums,target)
    print(ans2)