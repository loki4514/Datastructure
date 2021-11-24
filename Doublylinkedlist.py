# doubly linked list 
# consist of two address fields one point to previous node and at center it contains data block and next address points to next node
class Node:
    def __init__(self,value=None):
        self.value = value
        self.prev = None
        self.tail = None

class Doubly_Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next 
    def createDll(self,node):
        node = Node(node)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "created dummy"
    def insert_dll(self,value,location):
        # at start 
        # create a new node ,newnode next address points to first node and newnode's prev address is none .whereas the first node prev address points to newnode and make head as newnode
        if self.head is None: 
            print("booooo")
        else:
            newNode = Node(value)
            if location==0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            
        # insert at the end 
        # newNode next add is null and newnode prev add is last node's nextAddress
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
        # in between
        # we created new node 
        # now loop it stop where we want to insert and that is temp where the next node is nextNode
        # now we three node in hand i. tempnode ii. nextNode iii. newNode
        # newnode next address to nextnode and nextnode prev address to newnode
        # tempnode next address to newnode; newnode prev address to temp
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next 
                    index +=1 
                # newNode.next  = tempNode.next 
                # newNode.prev = tempNode
                # newNode.next.prev = newNode
                # tempNode.next = newNode
                nextNode = tempNode.next 
                tempNode.next = newNode
                newNode.next = nextNode
                newNode.prev = tempNode
                nextNode.prev = newNode
    def traversal(self):
        
        if self.head is None:
            print("almighty push")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
    def rev_traversal(self):
        if self.head is None:
            print("nah , it's empty")
        else:
            node = self.tail
            while node:
                print(node.value)
                node = node.prev
    def search(self,key):
        if self.head is None:
            return "nin tale alli jedi mannu ide"
        else:
            node = self.head
            while node:
                if node.value == key:
                    return node.value
                node = node.next 
    
            return " not found"
    def delete(self,location):
        if self.head is None:
            print("nope")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head is None
                    self.tail is None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                    if self.head == self.tail:
                        self.head is None
                        self.tail is None
                    else:
                        self.tail = self.tail.prev
                        self.tail.next = None
            else:
                temp = self.head
                index = 0
                while index < location -1:
                    temp = temp.next 
                    index += 1
                # temp.next = temp.next.next 
                # temp.next.prev = temp
    # if we set tail and head null it won't work in doubly linked list
    def deletedll(self):
        if self.head is None:
            print("empty")
        else:
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next 
            self.head = None
            self.tail = None            
            



        
linked_list = Doubly_Linked_list()
linked_list.createDll(2)
linked_list.insert_dll(0, 0)
linked_list.insert_dll(1, -1)
linked_list.insert_dll(2, -1)
linked_list.insert_dll(5, 2)
linked_list.insert_dll(10, 3)
print([node.value for node in linked_list])

linked_list.delete(2)
linked_list.deletedll()
print([node.value for node in linked_list])
#print(linked_list.search(21))
#linked_list.traversal()
#linked_list.rev_traversal()