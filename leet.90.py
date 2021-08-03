# Solution 1: does not work for certain cases
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 0: return [[]]
        nums.sort()
        power = [[], nums]
        for n in range(length, 1, -1):
            for i in range(length):
                subs = []
                last = i+n-1
                if last > length:
                    subs.extend(nums[:last - length])
                    subs.extend(nums[i:])
                else:
                    subs.extend(nums[i:last])
                if not subs in power:
                    power.append(subs)
        return power

# Solution 2: works and is fast enough
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) == 0: return [[]]
        power = [[], nums]
        for s in power:
            n = len(s)
            if n > 1:
                subs = s[:n-1]
                if not subs in power:
                    power.append(subs)
                for i in range(1,n):
                    subs = s[:i-1]
                    subs.extend(s[i:])
                    if not subs in power:
                        power.append(subs)
        return power

# Solution 3: recursion!
class Solution(object):
    def findSubsets(self, n, nums, current, result):
        for i in range(n, len(nums)):
            if i == n or last != nums[i]:
                last = nums[i]
                child = current + [last]
                result.append(child)
                self.findSubsets(i+1, nums, child, result)

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
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
