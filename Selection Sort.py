arr = [5,1,14,3,20]

for i in range(len(arr)):
    m = i
    for j in range(i+1 , len(arr)):
        if arr[m]>arr[j]:
            m=j
    
    arr[i], arr[m] = arr[m] , arr[i]
    
print("Sorted Array: ",arr)
