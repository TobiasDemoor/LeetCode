# Solution 1: does not work for all cases
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return -1
        closest = nums[:3]
        closestSum = sum(closest)
        closestDif = abs(closestSum - target)
        for n in nums[3:]:
            resultOld = closest
            resultOldSum = closestSum
            for i, m in enumerate(resultOld):
                newSum = resultOldSum - m + n
                newDif = abs(newSum - target)
                if newDif < closestDif:
                    closestDif = newDif
                    closestSum = newSum
                    closest = resultOld[:]
                    closest[i] = n
        return closestSum

# Solution 2: correct but slow ~O(n^3)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        best = sum(nums[:3])
        bestDif = abs(best - target)
        l = len(nums)
        i = 0
        while i < l-2:
            j = i + 1
            while j < l-1:
                k = j + 1
                while k < l:
                    current = nums[i] + nums[j] + nums[k]
                    currentDif = abs(current - target)
                    if currentDif < bestDif:
                        best = current
                        bestDif = currentDif
                    k += 1
                j += 1
            i += 1

        return best

# Solution 3: correct and fast enough ~O(n^3)
# class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        best = float("inf")
        bestDif = float("inf")
        length = len(nums)
        i = 0
        while i < length-2:
            n = nums[i]
            j = i + 1
            while j < length-1 and (n < 0 or n <= target):
                m = nums[j]
                partialSum = n + m
                k = j + 1
                while k < length and (m < 0 or partialSum <= target):
                    current = partialSum + nums[k]
                    currentDif = abs(current - target)
                    if currentDif < bestDif:
                        best = current
                        bestDif = currentDif
                        if bestDif == 0:
                            return target
                    k += 1
                j += 1
            i += 1
        return best

# Solution 4: leetCode's solution ~O(n^2)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        bestDif = float('inf')
        bestSum = float('inf')
        length = len(nums)
        for i in range(length-2):
            n = nums[i]
            base = i + 1
            top = length - 1
            while base < top:
                currentSum = n + nums[base] + nums[top]
                currentDif = abs(currentSum - target)
                if currentDif < bestDif:
                    bestDif = currentDif
                    bestSum = currentSum
                if currentSum < target:
                    base += 1
                else:
                    top -= 1
            if bestDif == 0:
                return target
        return bestSum

import time

start = time.time()
sol = Solution()
result = sol.threeSumClosest([-1, 2, 1, -4], 1)
print(result)
result = sol.threeSumClosest([1, 1, 1, 0], -100)
print(result)
result = sol.threeSumClosest([1, 1, 1, 0], 100)
print(result)
result = sol.threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82)
print(result)
result = sol.threeSumClosest([-100, -98, -2, -1], -101)
print(result)
print((time.time() - start)*1000)
