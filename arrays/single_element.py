def single_elemment(arr):
    xor = 0
    for ele in arr:
        xor= xor^ ele
    print(xor)


ls = list(map(int,input("Enter the elements: ").split(" ")))
single_elemment(ls)