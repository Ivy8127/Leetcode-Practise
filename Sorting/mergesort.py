def mergesort(arr):
    #if the array is 1 , it is sorted
    if len(arr) > 1:
        #divide into 2 portions
        left =arr[: len(arr)//2]
        right = arr[len(arr)//2:]

        #recursion
        mergesort(left)
        mergesort(right)


        #merge the arrays
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                #comparing the left most values of the 2 subarrays
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        #edge case - when left array is in merged array and we're left with the right array
        while j < len(right):
            arr[k] = right[j]
            k+=1
            j+=1
        #edge case - when right arr is in merged arr and the left has not been merged yet
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1

data = [6,5,12,10,9,1]
mergesort(data)
print(data)

