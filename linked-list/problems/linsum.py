class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def Lsum(self):
        sum1 = 0
        curr = self.head
        while curr!=None:
            sum1+=curr.data
            curr = curr.next
        return sum1

    def mult_2(self):
        ls = []
        curr = self.head
        while(curr):
            if(curr.data%2==0):
                ls.append(curr.data)
            curr = curr.next
        return ls
            
        
    def print_list(self):
        curr = self.head
        while(curr):
            print(curr.data,end='<-')
            curr = curr.next
        print()
 
ll = LinkedList()
n= int(input("Enter the no of  nodes  u want to insert: "))
for i in range(n):
    data = int(input(f'Enter data for node {i+1}: '))
    ll.insert(data)
# sum1 =  ll.Lsum()
ll.print_list()
mul = ll.mult_2()
# print(sum1)
print(mul)

        