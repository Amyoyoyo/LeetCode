class Solution(object):
    def searchInsert(self, nums, target):
        if nums[len(nums) - 1] < target:
            return len(nums)

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


'''
Runtime: 32 ms, faster than 86.48% of Python online submissions for Search Insert Position.
Memory Usage: 12.3 MB, less than 56.14% of Python online submissions for Search Insert Position.
'''
if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 4

    sol = Solution()
    ans = sol.searchInsert(nums, target)
    print(ans)
