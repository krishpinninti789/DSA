def insertion_sort(arr):
    # pivot = arr[0]
    
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i]<arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j]=temp
                print(arr)
    print("sorted array: ",arr)
                
        


arr= list(map(int,input("Enter the array: ").split()))
insertion_sort(arr)
    