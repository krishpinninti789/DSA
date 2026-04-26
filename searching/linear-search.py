
def linear_search(arr,element):
    for i in range(0,len(arr)):
        if (arr[i]==element):
            return i
    return -1
    

arr  = list(map(int,input("Enter the elements: ").split()))
element = int(input("Enter element to search: "))
# print(arr)
result = linear_search(arr,element)
print(result)

if (result==-1):
    print("Element not found")
else:
    print(f'Element {element} found at {result+1} place')

    
        
