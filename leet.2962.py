from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # attributes of the input
        maxNums = max(nums)
        lengthNums = len(nums)
        # global count of subarrays
        subarrayCount = 0
        maxNumsPositions = []
        auxArray = []

        # we swipe the end of the window from left to right
        end = 0
        count = 0
        aux = 0
        while end < lengthNums:
            if nums[end] == maxNums: 
                maxNumsPositions.append(end)
                if count >= k and aux > 0:
                    auxArray.append((count, aux))
                    aux = 0
                count += 1
            if count >= k: 
                aux += 1
                subarrayCount += 1
            end += 1
        if count >= k and aux > 0:
            auxArray.append((end-1, count, aux))

        if subarrayCount == 0: return 0

        for (count, aux) in auxArray:
            limitPos = maxNumsPositions[count - k]
            subarrayCount += aux * limitPos
                    
        return subarrayCount


sol = Solution()
print(sol.countSubarrays([1,3,2,3,3], 2))
print(sol.countSubarrays([1,3,2,3,1], 2))
print(sol.countSubarrays([1,4,2,1], 3))