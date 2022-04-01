# Find the most commonly occurring word in a page and replace it with it's synonym
#"The old man was was very old." 
#"The senior man was was very senior"
#the : 1
#old : 2
#man : 1
#was : 2

#edge cases 
#1. empty string returns an empty string
# 2. If there's a tie, replace the first word with the largest count

#Pseudocode:
# 1. Converting the string to an array ["The", "old",....]
#2.dict with a counter for very single element in our array and poulating it by looping through the array
#3.Find the maximum key
#4. Loop through array to find the word that matches the maximum key and assign it a new synonym
from collections import Counter
def mostOccuringWord(page, synonym):
  if len(page) == 0:
    return ""
  page = list(page.split(' ')) #split string into array 
  Word = Counter(page) #creates a counter for each word
  maxKey = max(Word, key = Word.get) #get key with maximum value
  for idx, word in enumerate(page): 
    #enumerate goes through an index and an element at once, special python function
    if word == maxKey:
      page[idx] = synonym 
  return ' '.join(page) #return a joined string
print(mostOccuringWord("The old man was was was very old .", synonym = "senior")) 
print(mostOccuringWord("The old man  was was very old .", synonym = "senior"))
print(mostOccuringWord("", synonym = "cool"))
#Notice the difference in these last 2 print statements bc of the "."
print(mostOccuringWord( "geeks for geeks is for geeks . By geeks and for the geeks .", synonym = "nerd"))
print(mostOccuringWord( "geeks for geeks is for geeks. By geeks and for the geeks.", synonym = "nerd"))

#Time complexity 0(n)
#Space complexity 0(n)
      
    
  
  
    