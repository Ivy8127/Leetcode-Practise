from collections import Counter, defaultdict
def numSplits(s):
    #create 2 hashmaps
    #1 empty hashmap for the left substring
    #A fully populates hashmap for the right substring
    right_count = Counter(s)
    left_count = defaultdict(int)
    good_splits = 0
    #loop through every character in the input string
    #checking whether the left count is equal to the right count
    for char in s:
        right_count[char] -=1
        left_count[char] +=1
        if right_count[char] == 0: #this character does not exist, so pop it
            right_count.pop(char)
        if len(left_count) == len(right_count):
            good_splits +=1

        if len(left_count) > len(right_count): #bc you're at the end of the loop
            break
    return good_splits 

print(numSplits("aacaba"))


