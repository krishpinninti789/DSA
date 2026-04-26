def binary_search(arr,low,high,key):
    mid = (low+high)//2
    if arr[mid]==key:
        return mid
    elif arr[mid]<key:
        return binary_search(arr,mid+1,high,key)
    else:
        return binary_search(arr,low,mid-1,key)
    return -1

arr= list(map(int,input("Enter sorted array: ").split()))
key=int(input("Enter element to search: "))

result = binary_search(arr,0,len(arr)-1,key)

if result ==-1:
    print("Element not found")
    
else:
    print(f"Element found at {result} index")
