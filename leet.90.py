from typing import List

class Solution(object):
    # solution with subsets pattern
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     subsets = [[]]
    #     for num in nums:
    #         for s in subsets.copy():  # here we copy the entity to avoid infinite loop
    #             current = s + [num]
    #             if current not in subsets:
    #                 subsets.append(s + [num])
    #     return subsets

    # stack solution
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)

    #     nums.sort()
    #     result = [[]]
    #     # we iterate over the array from the position i to the end
    #     stack = [(0, [])]
    #     while len(stack) > 0:
    #         i, current = stack.pop()
    #         for j in range(i, n):
    #             # if it's the first element or the value is different than the last one
    #             if i == j or last != nums[j]:
    #                 last = nums[j]
    #                 child = current + [last]
    #                 result.append(child)
    #                 stack.append((j+1, child))
    #     return result
    
    # recursive solution
    def findSubsets(self, n, nums, current, result):
        for i in range(n, len(nums)):
            if i == n or last != nums[i]:
                last = nums[i]
                child = current + [last]
                result.append(child)
                self.findSubsets(i+1, nums, child, result)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        power = [[]]
        self.findSubsets(0, nums, [], power)
        return power


sol = Solution()
print(sol.subsetsWithDup([1, 2, 3]))
print(sol.subsetsWithDup([]))
print(sol.subsetsWithDup([0]))
print(sol.subsetsWithDup([1, 2, 2]))
print(sol.subsetsWithDup([3,2,4,1]))
