# create head and tail
# normaly in sll the tail points to null ,here the tail points to head
class Node:
    def __init__(self,value=None):
        # just pass a argument inside the function which accepts a value , value = 0 is defined
        self.value = value
        self.next = None
class Circular_Sll:
    def __init__(self):
        self.head = None
        self.tail = None
        #iter function is nothing but to print the linked list 
    def __iter__(self):
        # node starts from head
        # enters the while loop 
        # yeild the node
        # icrement the node until tail
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    def create_csll(self,value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        
    def traversal(self):
        if self.head is None:
            print("error 404")
        else:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next
                if temp == self.tail.next:
                    break  
    def search(self,key):
        if self.head is None:
            print("error 404")
        else:
            temp = self.head
            while temp :
                if temp.value == key:
                    return temp.value
                temp = temp.next
                if temp == self.tail.next:
                    return "the node is not found"
            
            

    def insert_Csll(self,value,location):
        if self.head is None:
            print("no thanks")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "node has been successfully inserted"

    #deleting the first node for csll 
    # suppose their are only one node in the linked list then make head and tail set it to null 
    # it has multiple nodes :- update head and tail
    def delete(self,location):
        if self.head is None:
            print("the list is empty")
        else:
            if location == 0:
                # we have only one node in the circular linked list 
                if self.head == self.tail:
                    # make address field to none and head,tail is well
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next 
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempnode = self.head
                index = 0
                while index < location-1:
                    tempnode = tempnode.next
                    index += 1
                nextNode = tempnode.next
                tempnode.next = nextNode.next
    def delete_all(self):
        # here we have three reference 
        self.head = None
        self.tail.next = None
        self.tail = None


                

cll = Circular_Sll()
print(cll.create_csll(1))
cll.insert_Csll(1, 0)
cll.insert_Csll(2, 0)
cll.insert_Csll(3, 1)
cll.insert_Csll(4, 2)

print([node.value for node in cll])
#print(cll.search(3))
cll.delete(-1)

print([node.value for node in cll])
cll.delete_all()
print([node.value for node in cll])