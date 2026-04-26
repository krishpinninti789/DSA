def Small(arr):
    min_val = arr[0]
    for element in arr:
        if element < min_val:
            min_val = element
    return min_val


def Largest(arr):
    max_val = arr[0]
    for element in arr:
        if element> max_val:
            max_val = element
    return max_val


arr = [2,5,1,3,0]
print(Small(arr))
print(Largest(arr))

