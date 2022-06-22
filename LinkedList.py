class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    #printing the linked list
    def printll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    #adding element at the beginning
    def push_front(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    #adding element at the end
    def push_back(self,data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    #inserting element after a given element
    def insert_after(self,data,x):
        new_node = Node(data)
        if self.head == None:
            print("Linked list is empty")
        else:
            n = self.head
            while(n !=None):
                if n.data==x:
                    break
                n = n.ref
            if n==None:
                print("element doesn't exist")
            else:
                new_node.ref = n.ref
                n.ref = new_node

    #inserting element before a given element
    def insert_before(self,data,x):
        new_node = Node(data)
        if self.head == None:
            print("Linked list is empty")
        else:
            if self.head.data==x:
                new_node.ref = self.head
                self.head = new_node
            else:
                n = self.head
                while(n.ref!=None):
                    if n.ref.data==x:
                        break
                    n = n.ref
                if n.ref == None:
                    print("Item is not present")
                else:
                    new_node.ref = n.ref
                    n.ref = new_node

    #deleting the first node
    def pop_front(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            self.head = self.head.ref

    #deleting the last node
    def pop_back(self):
        if self.head ==None:
            print("Linked list is empty")
        elif self.head.ref==None:
            self.head = None
        else:
            n = self.head
            while(n.ref.ref!=None):
                n = n.ref
            n.ref = None

    #deleting a given node
    def remove(self,data):
        if self.head ==None:
            print("Linked list is empty")
        elif self.head.data == data:
            self.head = self.head.ref
        else:
            n = self.head
            while(n.ref!=None):
                if n.ref.data==data:
                    break
                n = n.ref
            if n.ref==None:
                print('Item is not present in the linked list')
            else:
                n.ref = n.ref.ref




ll1 = LinkedList()


ll1.push_back(10)
ll1.insert_after(20,10)
ll1.insert_before(30,10)
#ll1.remove(40)
ll1.printll()
