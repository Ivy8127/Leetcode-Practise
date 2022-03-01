#tricky subsequence 2 pointer technique question
def find_minimum_chars(s,t):
    i,j = 0,0

    #armaze
    #amazon
    while i < len(s):
        if s[i] == t[j]:
            j +=1
            if j == len(t):
                return 0
        i+=1 
    return len(t) - j

print( find_minimum_chars('armaze','amazon'))          