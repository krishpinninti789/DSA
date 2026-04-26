class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next= self.head
            self.head = new_node
    def print_nodes(self):
        curr = self.head
        while(curr):
            print(curr.data,end="<-")
            curr = curr.next
        print()
    def mid_data(self,n):
        req_pos = (n//2)
        count=0
        curr = self.head
        while(curr):
            if(count==req_pos):
                return curr.data
            
            curr = curr.next
            count+=1
                
        
        
ll = LinkedList()
n=int(input("Enter no of nodes u want to insert: "))
for i in range(n):
    data = int(input(f"Enter data for node {i+1}: "))
    ll.insert_node(data)
ll.print_nodes()
req = ll.mid_data(n)
print(req)