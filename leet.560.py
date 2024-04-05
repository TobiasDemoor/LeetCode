from collections import defaultdict
from typing import List

class Solution:
    # prefix sum array
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = 0
        count = 0
        mpp = defaultdict(int)
        # if the difference between the preSum and k is 0 it should count once
        mpp[0] = 1
        for i in range(n):
            preSum += nums[i]
            remove = preSum - k
            count += mpp[remove]
            # add 1 to the map at the value of preSum since if in the following items one value of
            # preSum is exceeded over k by the value of preSum the subarray exists
            mpp[preSum] += 1

        return count

sol = Solution()
print(sol.subarraySum([1,2,3,4], 3))