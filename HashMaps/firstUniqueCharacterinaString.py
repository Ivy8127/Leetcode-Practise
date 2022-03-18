from collections import Counter #you can build the counter yourself though

def firstUniqChar(s):
    UniqueChar = Counter(s)
    
    for i , char in enumerate(s):
        if UniqueChar[char] == 1:
            return i
    return -1  


#time complexity -linear time bc we go through the lenght of the string only 2 times
# space complexity- constant space bc the hashmap is storing only 26 characters          
        
        