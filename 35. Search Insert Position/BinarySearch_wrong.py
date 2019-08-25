class Solution(object):
    def searchInsert(self, nums, target):
        if len(nums) == 1 and nums[0] < target:
            return 1
        elif len(nums) == 1:
            return 0

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left + 1)//2
            if nums[mid] < target:
                left = mid
            elif nums[mid] == target:
                return mid
            else:
                right = mid
        return left


if __name__ == '__main__':
    nums = [1, 3]
    target = 2

    sol = Solution()
    ans = sol.searchInsert(nums, target)
    print(ans)
