def maximumSwap(self, num: int) -> int:
        if num < 11:
            return num
        if num > 10**8:
            return num
        original_num = list(str(num))
        new_num = original_num[:]

        for i in range(len(original_num)):
            for j in range(i + 1, len(original_num)):
                # Swap
                original_num[i], original_num[j] = original_num[j], original_num[i]
                if new_num < original_num:
                    new_num = original_num[:]
                # Swap back
                original_num[i], original_num[j] = original_num[j], original_num[i]

        return int("".join(new_num))


#This the bruteforce solution O(n^2)
def maximumSwap(num):
max_num = num
#num is an integer, convert it to a list

s= list(str(num)) # ['2','7','3','6']

for i in range(len(s)):
    for j in range(i+1, len(s)):
        #swap
        s[i] , s[j]= s[j], s[i]
        
        max_num = max(max_num, int(''.join(s)))
        
        #return to original num for swapping again
        #by reswapping
        s[i], s[j] = s[j], s[i]
return max_num         
            
            