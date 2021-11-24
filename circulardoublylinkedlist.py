class Node:
    def __init__(self,value=None):
        self.value = value
        self.tail = None
        self.prev = None

class Circulardll:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next 
            if node == self.tail.next:
                break
    def create_cdll(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        # update previous and next reference
        newNode.prev = newNode
        newNode.next = newNode
        print('ok ')

    def insert_cdll(self,value,location):
        if self.head is None:
            return "the CDLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head 
                # prev reference should point to the last node
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                index = 0 
                tempNode = self.head
                while index < location-1:
                    tempNode = tempNode.next 
                    index += 1
                newNode.next  = tempNode.next 
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
                # nextNode = tempNode.next 
                # tempNode.next = newNode
                # newNode.next = nextNode
                # newNode.prev = tempNode
                # nextNode.prev = newNode
    def traversal(self):
        if self.head is None:
            print("empty")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next 

    def revtraversal(self):
        if self.head is None:
            print('empty')
        else:
            temp = self.tail
            while temp:
                print(temp.value)
                if temp == self.head:
                    break
                temp = temp.prev
    
    def search(self,key):
        if self.head is None:
            print('empty')
        else:
            temp = self.head
            while temp:
                if temp.value == key:
                    return temp.value
                if temp == self.tail:
                    break
                temp = temp.next 

    def delete(self,location):
        # delete at the start ,make the link disable i.e next and prev feild set it to null and then make
        # head and tail none; move head forward  
        if self.head is None:
            print("empty")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next 
                    self.head.prev = self.tail 
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                index = 0
                temp = self.head
                while index < location-1:
                    temp = temp.next 
                    index += 1
                temp.next = temp.next.next
                temp.next.prev = temp
    def delete_all(self):
        if self.head is None:
            print("empty")
        else:
            self.tail.next = None
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next 
            self.head = None
            self.tail = None 


                       

                   

cdll = Circulardll()
cdll.create_cdll(2)
cdll.insert_cdll(3, 0)
cdll.insert_cdll(4, 1)
cdll.insert_cdll(5, 2)
cdll.insert_cdll(6, 3)
cdll.insert_cdll(7, -1)

print([node.value for node in cdll])
cdll.delete(1)
cdll.delete_all()
print([node.value for node in cdll])
# cdll.revtraversal()
# print("-----------")
# print(cdll.search(5))