def groupAnagrams(words):
    anagram = {} # aet : [eat,tea,ate]
                 # ant : [tan,nat]
                 # abt : [bat]
                 #[[eat,tea,ate],[tan,nat],[bat]]
    grouped_anagrams = []
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram:
            anagram[sorted_word] += [word]
        else:
            anagram[sorted_word] = [word]

    for k,v in anagram.items():
        grouped_anagrams.append(v)  

    return grouped_anagrams

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) 
                    #aet   aet   ant    aet   ant   abt    