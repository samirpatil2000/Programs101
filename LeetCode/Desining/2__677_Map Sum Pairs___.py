class MapSum:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_={}

    def insert(self, key: str, val: int) -> None:
        self.dict_[key]=val

    def sum(self, prefix: str) -> int:
        return sum([self.dict_[i] for i in self.dict_ if i.startswith(prefix)])
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)