def Small(arr):
    arr.sort()
    return arr[0]


def Largest(arr):
    arr.sort()
    return arr[-1]


arr = [2,5,1,3,0]
print(Small(arr))
print(Largest(arr))

