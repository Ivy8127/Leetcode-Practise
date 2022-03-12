#1000 edge cases!!!!
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #run binary search on the smaller array
        A , B = nums1, nums2
        total = len(nums1)+ len(nums2)
        half = total//2
        if len(B) < len(A):
            A , B= B, A
        left = 0
        right = len(A)-1
        while True:
            mid = (left+right)//2
            mid2 = half - mid -2
            
            Aleft = A[mid] if mid >= 0 else float("-infinity")
            Aright = A[mid+1] if (mid+1) < len(A) else float("infinity")
            Bleft =B[mid2] if mid2 >= 0 else float("-infinity")
            Bright = B[mid2+1] if (mid2+1) <len(B) else float("infinity")
            
            if Aleft <= Bright and Bleft <= Aright:
                #left partition is correct
                #check whether the total is even or odd
                if total % 2:
                    #odd 
                    return min(Aright, Bright)
                #even
                return (max(Aleft, Bleft) + min(Aright, Bright)) /2
            elif  Aleft > Bright:
                    right = mid -1
            else:
                left = mid + 1
                    