def reversefunc(s):
    def reverse(s,i,j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return s 
    i,j = 0,0
    while j < len(s):
        if s[j]== 0:
            reverse(s,i,j-1)
            i = j+1
        j+=1
    return s

print(reversefunc([45,5,6,0,5,12,0,54,3,0]))