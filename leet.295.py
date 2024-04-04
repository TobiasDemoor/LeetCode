import math

class MedianFinder:

    def __init__(self):
        # heap containing all number bellow median and the median if there is one
        self.lesserHeapLength = 0
        self.lesserHeap = []
        # heap containing all number above median
        self.greaterHeapLength = 0
        self.greaterHeap = []

    def insertIntoLesserHeap(self, num: int) -> None:
        i = self.lesserHeapLength
        self.lesserHeap.append(num)
        j = math.floor((i-1)/2)
        while j > -1 and num > self.lesserHeap[j]:
            self.lesserHeap[j], self.lesserHeap[i] = self.lesserHeap[i], self.lesserHeap[j]
            i = j
            j = math.floor((i-1)/2)
        self.lesserHeapLength += 1

    def insertIntoGreaterHeap(self, num: int) -> None:
        i = self.greaterHeapLength
        self.greaterHeap.append(num)
        j = math.floor((i-1)/2)
        while j > -1 and num < self.greaterHeap[j]:
            self.greaterHeap[j], self.greaterHeap[i] = self.greaterHeap[i], self.greaterHeap[j]
            i = j
            j = math.floor((i-1)/2)
        self.greaterHeapLength += 1

    def removeLesserHeapRoot(self):
        if self.lesserHeapLength == 1:
            self.lesserHeap.pop()
            self.lesserHeapLength -= 1
            return
        self.lesserHeap[0] = self.lesserHeap.pop()
        self.lesserHeapLength -= 1  
        i = 0
        while i*2+1 < self.lesserHeapLength:
            left = self.lesserHeap[i*2+1]
            if i*2+2 < self.lesserHeapLength:
                right = self.lesserHeap[i*2+2]
            else:
                right = float('-inf')
            if left > right:
                if self.lesserHeap[i] < left:
                    self.lesserHeap[i], self.lesserHeap[i*2+1] = self.lesserHeap[i*2+1], self.lesserHeap[i]
                    i = i*2+1
                else:
                    break
            else:
                if self.lesserHeap[i] < right:
                    self.lesserHeap[i], self.lesserHeap[i*2+2] = self.lesserHeap[i*2+2], self.lesserHeap[i]
                    i = i*2+2
                else:
                    break

    def removeGreaterHeapRoot(self):
        if self.greaterHeapLength == 1:
            self.greaterHeap.pop()
            self.greaterHeapLength -= 1
            return
        self.greaterHeap[0] = self.greaterHeap.pop()
        self.greaterHeapLength -= 1
        i = 0
        while i*2+1 < self.greaterHeapLength:
            left = self.greaterHeap[i*2+1]
            if i*2+2 < self.greaterHeapLength:
                right = self.greaterHeap[i*2+2]
            else:
                right = float('inf')
            if left < right:
                if self.greaterHeap[i] > left:
                    self.greaterHeap[i], self.greaterHeap[i*2+1] = self.greaterHeap[i*2+1], self.greaterHeap[i]
                    i = i*2+1
                else:
                    break
            else:
                if self.greaterHeap[i] > right:
                    self.greaterHeap[i], self.greaterHeap[i*2+2] = self.greaterHeap[i*2+2], self.greaterHeap[i]
                    i = i*2+2
                else:
                    break

    def addNum(self, num: int) -> None:
        median = self.findMedian()
        if num < median:
            if self.lesserHeapLength > self.greaterHeapLength:
                # we need to move the max of the lesserHeap to the greaterHeap
                val = self.lesserHeap[0]
                if val > num:
                    # remove from lesserHeap
                    self.removeLesserHeapRoot()
                    # insert into greaterHeap
                    self.insertIntoGreaterHeap(val)
                else:
                    # insert into greaterHeap
                    self.insertIntoGreaterHeap(num)
                    return
            # insert in lesserHeap
            self.insertIntoLesserHeap(num)
        else:
            if self.lesserHeapLength == self.greaterHeapLength:
                # we need to move the min of the greaterHeap to the lesserHeap
                val = self.greaterHeap[0]
                if val < num:
                    # remove from greaterHeap
                    self.removeGreaterHeapRoot()
                    # insert into lesserHeap
                    self.insertIntoLesserHeap(val)
                else: 
                    # insert into lesserHeap
                    self.insertIntoLesserHeap(num)
                    return
            # insert in greaterHeap
            self.insertIntoGreaterHeap(num)
        
    def findMedian(self) -> float:
        if self.lesserHeapLength > self.greaterHeapLength:
            return self.lesserHeap[0]
        else:
            if self.lesserHeapLength == 0: return float('inf')
            return (self.lesserHeap[0] + self.greaterHeap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
for num in [-1,-2,-3,-4,-5]:
    obj.addNum(num)
    print(obj.findMedian())