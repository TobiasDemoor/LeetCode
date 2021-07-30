# Solution 1: works without any issue uses a lot of memory
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


# Solution 2: a tree (does not work beacause you should overwrite key value pair)
# class TreeNode(object):
#     def __init__(self, char, val):
#         self.char = char
#         self.val = val
#         self.children = {}

# class MapSum(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = TreeNode("", 0)
        

#     def insert(self, key, val):
#         """
#         :type key: str
#         :type val: int
#         :rtype: None
#         """
#         aux = self.root
        
#         i = 0
#         while i < len(key):
#             c = key[i]
#             aux.val += val
#             if c in aux.children:
#                 aux = aux.children[c]
#                 i += 1
#             else:
#                 break

#         for c in key[i:]:
#             child = TreeNode(c, val)
#             aux.children[c] = child
#             aux = child
        

#     def sum(self, prefix):
#         """
#         :type prefix: str
#         :rtype: int
#         """
#         aux = self.root
#         for c in prefix:
#             if c in aux.children:
#                 aux = aux.children[c]
#             else:
#                 return 0
#         return aux.val
        


mapSum = MapSum()
mapSum.insert("apple", 3)  
print(mapSum.sum("ap"))           # return 3 (apple = 3)
mapSum.insert("app", 2)    
print(mapSum.sum("ap"))           # return 5 (apple + app = 3 + 2 = 5)