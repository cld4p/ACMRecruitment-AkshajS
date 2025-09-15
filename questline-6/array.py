def rotate(nums,k):
    n=len(nums)
    k%=n

    def reverse(arr,s,e):
        while s<e:
            arr[s],arr[e] = arr[e],arr[s]
            s+=1
            e-=1

    reverse(nums,0,n-1)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)


nums1 = [1,2,3,4,5,6,7]
k1=3
rotate(nums1,k1)
print("Rotated list:",nums1)
