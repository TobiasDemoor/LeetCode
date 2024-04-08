class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        stack = self.stack
        currPrice, currSpan = price, 1

        while stack and stack[-1][0] <= currPrice:
            _, prevSpan = stack.pop()
            currSpan += prevSpan
    
        stack.append((currPrice, currSpan))
        return currSpan

span = StockSpanner()
print(span.next(100))
print(span.next(80))
print(span.next(60))
print(span.next(70))
print(span.next(60))
print(span.next(75))
print(span.next(85))