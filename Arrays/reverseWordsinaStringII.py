def reverseString(arr):
    word = ''.join(arr)
    #print(word) #the sky is blue
    rev = ' '.join(word.split()[::-1])
    rev= list(rev)
    return rev

#print(reverseString(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))

#optimal sln , linear time and constant space sln
#1. reverse the entire string
#2. reverse the words using 2 pointers, where there is a ""
#3. Special edge case, where pointer is at the last index, reverse that too
def reverseWords(s):
    def reverse(s,i,j):
        while i < j:
            s[i] ,s[j]= s[j], s[i]
            i+=1
            j-=1
        return s 
    s = reverse(s,0, len(s)-1) #['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']
    i,j = 0,0
    while j < len(s):
        if s[j] == " ":
            reverse(s,i,j-1)
            i = j + 1
        elif j == len(s)-1:
            reverse(s,i,j)    
        j+=1 
    #reverse(i,j-1)  
    return s         
print(reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))