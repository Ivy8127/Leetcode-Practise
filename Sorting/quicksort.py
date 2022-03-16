def quicksort(arr):
    #base case
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]  
        left = [i for i in arr[1:] if i<= pivot] 
        right = [i for i in arr[1:] if i > pivot]
        return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([8, 7, 2, 1, 0, 9, 6]))         