class Solution(object):
    def twoSum(self, nums, target):
        nums_copy=nums.copy() # 保留原数组，sort函数会修改原数组
        nums.sort() # 排序-timsort算法

        vals=[] # 满足两数相加==target的数
        for i in range(len(nums)):
            start=i+1
            end=len(nums)-1
            while(start<=end):
                mid_s = int((start + end) / 2)
                if nums[mid_s]==target-nums[i]:
                    vals.append(nums[i])
                    vals.append(nums[mid_s])
                    break
                elif nums[mid_s]<target-nums[i]:
                    start=mid_s
                else:
                    end=mid_s
                mid_e = int((start + end) / 2)
                if mid_e==mid_s:
                    start+=1

        result=[]
        for i in range(len(nums_copy)):# 在原数组中找这两个数的索引
            if (nums_copy[i]==vals[0])or(nums_copy[i]==vals[1]):
                result.append(i)

        return result



if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    sol=Solution()
    ans=sol.twoSum(nums,target)
    print(ans)
