def atoi(s):
    s = s.lstrip()
    isPositive = True
    numbers = []

    for i , e in enumerate(s):
        if i == 0:
            if s[i] == '+':
                continue
            if s[i] == '-':
                isPositive = False
                continue
        if not e.isdigit(): 
            break
        if e.isdigit():
            numbers.append(e)

    if numbers == []:
        return 0
    number = int(''.join(numbers))
    minn = -2**31
    maxx = 2**31 -1
    if isPositive:
        if number > maxx:
            number = maxx
    else:
        return max(-number, minn)

    return number     

print(atoi(' -32'))       

