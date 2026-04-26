def sort(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print("Sorted array is:",arr)
    
arr= list(map(int,input("Enter the array: ").split()))

sort(arr)