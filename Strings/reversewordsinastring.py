
#i'd advice not to use this method in an actual interview 
#as it does not demonstrate your problem solving skills
def reverse_word(s):
    if len(s) == 1:
        return s
    s= s.split()
    rev_str = s[::-1]
    return ' '.join(rev_str)

print(reverse_word("a good   example"))  


#Best approach

def reverse_words2(s):
    #split the words into a list
    word_list = s.split() #['a','good','example']
    res = []
    #loop through the word list
    for word in word_list:
        res.insert(0,word)
    return ' '.join(res)
print(reverse_words2("a good   example"))        
