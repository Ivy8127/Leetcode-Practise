def reorderData(logs):
    digit_log , letter_log = [],[]
    for log in logs:
        if (log.split()[1]).isdigit():
            digit_log.append(log)
        else:
            letter_log.append(log.split()) #split into iterable to enable lambda sorting by index
    print(letter_log)        
    letter_log.sort(key= lambda x: x[0]) #sort by identifier         
    letter_log.sort(key= lambda x: x[1:]) #sort by log letter 
    for i in range(len(letter_log)):
        letter_log[i] = " ".join(letter_log[i])
    letter_log.extend(digit_log)    
    #return letter_log    
    

print(reorderData(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))             