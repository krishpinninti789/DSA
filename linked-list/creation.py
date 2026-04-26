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
            print(curr.data,end="->")
            curr = curr.next
ll = LinkedList()
n=int(input("Enter no of nodes u want to insert: "))
for i in range(n):
    data = int(input(f"Enter data for node {i+1}: "))
    ll.insert_node(data)
ll.print_nodes()
