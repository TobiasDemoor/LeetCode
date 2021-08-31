from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        if nums[i] > nums[j]:
            while i < j:
                mid = (i + j) // 2
                if nums[mid] > nums[j]:
                    i = mid + 1
                else:
                    j = mid
        
        return nums[i]

sol = Solution()

assert sol.findMin([4,5,6,7,0,1,2]) == 0
assert sol.findMin([3,4,5,6,1,2]) == 1
assert sol.findMin([11,13,15,17]) == 11
assert sol.findMin([4,5,6,7,0,1,2]) == 0