#Time complexity 0(n)
def isMonotonic(arr):
  if arr == sorted(arr) or arr==sorted(arr, reverse= True):
    return True
  else:
    return False  
print(isMonotonic([6,5,5,4]))          


def isMonotonic2(arr):
  decreasing = True
  increasing = True
  for i in range(1,len(arr)):
    if arr[i-1] < arr[i]:  #eg 2 3 => increasing
      decreasing = False
    elif arr[i-1] > arr[i]:#eg 4 3 => decreasing
      increasing = False
  return increasing or decreasing    
print(isMonotonic2([6,5,5,4]))  
        
