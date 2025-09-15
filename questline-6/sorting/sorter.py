#simple bubble sorter

def bubble_sort(arr):
    n = len(arr)
    #sets the value of n as the length
    
    for i in range(n): #last i elements are in place, compare upto n-i-1 due to the largest elements
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]: #swap number if its found greater than the next number  
                arr[j],arr[j+1]=arr[j+1],arr[j] #swap code

    return arr #return the value like a function



print(bubble_sort([5, 2, 9, 1, 5, 6]))
