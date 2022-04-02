class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []    

    def insert(self, val: int) -> bool:
        res =  val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList) #insert into hashmap and it's value is the idx of the array so far
            self.numList.append(val) #add the value to the list as well
        return res   
        

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            #get the index that this value maps to in the hashmap
            idx = self.numMap[val]
            #get index of last value in list
            lastValue = self.numList[-1]
            self.numList[idx] = lastValue
            #pop last value from the list
            self.numList.pop()
            #update the hashmap to have the lastvalue key map to the index
            self.numMap[lastValue] = idx
            #remove the value from the hashmap
            del self.numMap[val]
        return res    
        

    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()