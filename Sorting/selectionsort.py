def selection_sort(arr):
    #find the minimum element in arr
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        #swap minimum number
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
data = [64,25,12,22,11]          
print(selection_sort(data))
print(data) 
#11 12 22 25 64         
