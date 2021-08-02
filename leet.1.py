class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i, n in enumerate(nums):
            compl = target-n
            if compl in hashMap:
                return [hashMap[compl], i]
            hashMap[n] = i
        raise Exception("No solution found")
