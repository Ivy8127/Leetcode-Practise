def merge(nums1, nums2,m,n):
    #create a pointer at the last position of nums1
    last = m + n -1

    #loop through while n and m >0
    while m>0 and n > 0:
        if nums2[n-1] > nums1[m-1]:
            nums1[last] = nums2[n-1]
            #decrement the m pointer
            m-=1

        else:
            nums1[last] = nums1[m-1]
            #decrement the n pointer
            n-=1

        last -= 1 #keep decrementing this pointer 

    #special edge case where nums1 is empty, add remaining values of nums2 to nums1
    while n > 0:
        nums1[last] = nums2[n-1]
        n-=1
        last-=1
         
