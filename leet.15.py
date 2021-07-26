# Solution 1: first solution I thought of, praise our lord hashmap
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        for i, n in enumerate(nums):
            hashMap = {}
            for indx, m in enumerate(nums[i+1:]):
                j = indx + i + 1
                complement = -(n + m)
                if complement in hashMap:
                    k = hashMap[complement]
                    if k != i and k != j:
                        newElement = sorted([n, m, complement])
                        if not newElement in output:
                            output.append(newElement)
                hashMap[m] = j
        return output

# Solution 2: tried to make it more efficient but was not successful
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         length = len(nums)
#         output = []
#         i = 0
#         while i < length-2 and nums[i] <= 0:
#             j = i+1
#             while j < length-1 and -nums[i] >= 2*nums[j]:
#                 complement = -(nums[i] + nums[j])
#                 k = j+1
#                 while k < length and complement > nums[k]:
#                     k += 1
#                 if k < length and complement == nums[k]:
#                     newElement = [nums[i], nums[j], complement]
#                     if not newElement in output:
#                         output.append(newElement)
#                 j += 1
#             i += 1
#         return output

sol = Solution()
result = sol.threeSum([-1,0,1,2,-1,-4])
print(result)
result = sol.threeSum([1, 0, 0, 0, -1])
print(result)
# assert result == [[-1,-1,2],[-1,0,1]]

