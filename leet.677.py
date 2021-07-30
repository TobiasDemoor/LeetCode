class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.map[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sum = 0
        for key in filter(lambda e : e.startswith(prefix) ,self.map.keys()):
            sum +=self.map[key]
        return sum
        


mapSum = MapSum()
mapSum.insert("apple", 3)  
print(mapSum.sum("ap"))           # return 3 (apple = 3)
mapSum.insert("app", 2)    
print(mapSum.sum("ap"))           # return 5 (apple + app = 3 + 2 = 5)