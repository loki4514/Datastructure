# class Node:
#     def __init__(self,value=None):
#         self.value = value
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def __iter__(self):
#         node = self.head 
#         while node:
#             yield node 
#             node = node.next
#     def create_linked(self,value):
#         newNode = Node(value)
#         newNode.next = None
#         self.head = newNode
#         self.tail = newNode
#     def insert(self,value,location):
#         newNode = Node(value)

#         if self.head is None:
#                 self.head = newNode
#                 self.tail = newNode
#         else:
#             if location == 0:
#                 newNode.next = self.head
#                 self.head = newNode
#             elif location == -1:
#                 self.tail.next = newNode
#                 self.tail = newNode
#                 newNode.next = None
#             else:
#                 index = 0
#                 tempnode = self.head 
#                 while index < location -1:
#                     tempnode = tempnode.next
#                     index += 1
#                 # tempnode.next = newNode
#                 # newNode.next = tempnode.next.next 
#                 nextNode = tempnode.next
#                 tempnode.next = newNode
#                 newNode.next = nextNode
#     def traverse(self):
#         if self.head is None:
#             print("the linked list is empty")
#         else:
#             node = self.head 
#             while node:
#                 print(f'{node.value}')
#                 node = node.next
#     def delete_sll(self,location):
#         if self.head is None:
#             print("empty dude")
#         else:
#             if location == 0:
#                 if self.head == self.tail:
#                     self.head = None
#                     self.tail = None
#                 else:
#                     self.head = self.head.next 
#             elif location == -1:
#                 if self.head == self.tail:
#                     self.head = None
#                     self.tail = None
#                 else:
#                     node = self.head
#                     while node is not None:
#                         if node.next == self.tail:
#                             break
#                         node = node.next 
#                     node = self.tail 
#                     node.next = None 
#             else :
#                 index  = 0
            

                    

            
# # sll.create_linked(24)
# sll = LinkedList()
# sll.insert(2, 0)
# sll.insert(3, 0)
# sll.insert(5, -1)
# sll.insert(6, -1)
# sll.insert(90, 1)
# sll.traverse()
# print([node.value for node in sll])
import random
class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None

    # this method is used to print the node
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self,value = None):
        self.head = None
        self.tail = None
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next 
    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next 
        return result
    
    # to add at the end ofthe ll
    def add(self,value):
        newNode = Node(value)
        if self.head is None:
            
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = None
        return self.tail 


    def generate(self,n,min_value,max_value):
        # we are creating a new linked lsit
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(random.randint(min_value,max_value))
        return self

    def traverse(self):
        if self.head is None:
            return 'none'
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next



customLinkedList = LinkedList()
# customLinkedList.generate(10, 20,245)
# print(customLinkedList)
# # customLinkedList.traverse()

