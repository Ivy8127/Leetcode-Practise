from collections import Counter
def noOfOddOccurrences(arr):
    odd = Counter(arr)
    for k,v in odd.items():
        if v % 2 != 0:
            return k

print(noOfOddOccurrences([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2 ]))            