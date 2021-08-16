from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        acum = 0
        listSum = []
        for n in nums:
            acum += n
            listSum.append(acum)
        self.listSum = listSum

    def sumRange(self, left: int, right: int) -> int:
        return self.listSum[right] - (self.listSum[left-1] if left > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
