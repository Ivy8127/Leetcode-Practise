#Time complexity O(n)
def highfive(lists):
    if not lists:
        return
    hashmap = {}
    for i in range(len(lists)):
        id = lists[i][0]
        scores = lists[i][1]
        if id in hashmap:
            hashmap[id]+= [scores]
        else:
            hashmap[id] = [scores]
    result = []
    for k,v in hashmap.items():
        sorted_val = sorted(v, reverse=True)
        if len(sorted_val) >= 5:
           top_five = sorted_val[:5]
        else:
            top_five = sorted_val 
        hashmap[k] = sum(top_five)//5 
        result.append([k,hashmap[k]]) 
    return result                      

           

print(highfive([[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]))        
