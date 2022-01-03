#------------------------------------------------------Singly Linked Lists------------------------------------------------------#

# A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection 
# to another data element in form of a pointer. Python does not have linked lists in its standard library. We implement the 
# concept of linked lists using the concept of nodes.

# In this type of data structure there is only one link between any two data elements. We create such a list and create 
# additional methods to insert, update and remove elements from the list.

#----------------------------------------------------------Imports--------------------------------------------------------------#

from random import randint

#-------------------------------------------------------------------------------------------------------------------------------#

# A linked list is created by using the node class. We create a Node object and create another class to use this node object. 
# We pass the appropriate values through the node object to point the to the next data elements. 

class SinglyLinkedListNode:

    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

    def __str__(self):
        return str(self.value)

#-------------------------------------------------------------------------------------------------------------------------------#

class SinglyLinkedList:

    def __init__(self, values=None):
        self.head = None # value of the head
        # if values is not None:
        #     self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

#---------------------------------------------------------Inserting-------------------------------------------------------------#

# Inserting at the Beginning

# This involves pointing the next pointer of the new data node to the current head of the linked list. So the current head of 
# the linked list becomes the second data element and the new node becomes the head of the linked list.

    def add_to_beginning(self, value):
        # NewSinglyLinkedListNode = SinglyLinkedListNode(value)
        if self.head is None:
            # self.head = NewSinglyLinkedListNode
            # which can also be written as
            self.head = SinglyLinkedListNode(value)
        else:
            # NewSinglyLinkedListNode.next = self.head
            # self.head = NewSinglyLinkedListNode
            # which can also be written as
            self.head = SinglyLinkedListNode(value, self.head)
        return self.head
    
# Inserting at the End

# This involves pointing the next pointer of the the current last node of the linked list to the new data node. So the current 
# last node of the linked list becomes the second last data node and the new node becomes the last node of the linked list.

    def add_to_end(self, value):
        # NewSinglyLinkedListNode = SinglyLinkedListNode(value)
        if self.head is None:
            # self.head = NewSinglyLinkedListNode
            # which can also be written as
            self.head = SinglyLinkedListNode(value)
            return
        lastNode = self.head
        while(lastNode.next):
            lastNode = lastNode.next
        # lastNode.next = NewSinglyLinkedListNode
        # which can also be written as
        lastNode.next = SinglyLinkedListNode(value)

# Inserting in between two Data Nodes

# This involves changing the pointer of a specific node to point to the new node. That is possible by passing in both the new 
# node and the existing node after which the new node will be inserted. So we define an additional class which will change the 
# next pointer of the new node to the next pointer of middle node. Then assign the new node to next pointer of the middle node.

    def add_in_between(self, middleNode, value):
        if middleNode is None:
            print("the parsed node is absent")
            return

        NewSinglyLinkedListNode = SinglyLinkedListNode(value)
        NewSinglyLinkedListNode.next = middleNode.next
        middleNode.next = NewSinglyLinkedListNode

# Inserting multiple at the End

# Just as in the "Inserting at the End", this involves pointing the next pointer of the the current last node of the linked 
# list to the new data node. So the current last node of the linked list becomes the second last data node and the new node 
# becomes the last node of the linked list and then repeating this for each new "value" parsed.

    def add_multiple(self, values):
        for v in values:
            self.add_to_end(v)

#-------------------------------------------------------------------------------------------------------------------------------#

# Generate a Singly Linked List with n values that are randomly selected between minValue and maxValue (both values being 
# inclusive)

    def generate(self, n, minValue, maxValue):
        self.head = None
        for i in range(n):
            self.add_to_end(randint(minValue, maxValue))
        return self

#-------------------------------------------------------------------------------------------------------------------------------#

# Pop the "head" of the linked list
    def pop_head(self):
        if self.head is not None:
            head_to_pop = self.head
            self.head = self.head.next
            return head_to_pop

#-------------------------------------------------------------------------------------------------------------------------------#

    # Print itteratively (each item on a new line)
    def print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

#-------------------------------------------------------------------------------------------------------------------------------#

# Remove a node at a particular index, O(n)

    # WIP

    # def remove_at(self, index):
    #     # Make sure the index provided is valid
    #     if index < 0 or index >= self.size():
    #       raise ValueError("wrong index")
    
    #     # Search from the front of the list
    #     if index < self.size() / 2:
    #       i = 0
    #       trav = self.head
    #       while i != index:
    #         i += 1  
    #         trav = trav.next
          
    #     # Search from the back of the list
    #     else:
    #       i = self.size() - 1
    #       trav = self.tail
    #       while i != index:
    #         i -= 1
    #         trav = trav.prev
    
    #     return self.__remove__(trav)

#------------------------------------------------------------Playing------------------------------------------------------------#

    # WIP: used above

    # def size(self):
    #     current = self.head
    #     size = 0
    #     while current is not None:
    #         size += 1
    #         current = current.next
    #     return size

    
# TODO: finish up by ensurin that the applicable functions from https://github.com/akzare/Algorithms/blob/master/src/main/python/algorithms/datastructures/linkedlist/DoublyLinkedList.py are all implemented 
# TODO: tidy up and constant formatting

sll1 = SinglyLinkedList()
sll1.head = SinglyLinkedListNode("Mon")
node2 = SinglyLinkedListNode("Tues")
node3 = SinglyLinkedListNode("Wed")
# link first node to second node
sll1.head.next = node2

# link second Node to the third node 
node2.next = node3

print(sll1)
print("")
# Output: Mon -> Tues -> Wed

# Print itteratively (each item on a new line))
sll1.print()
print("")

# adding elements
sll1.add_to_beginning("Sun")
print(sll1)
print("")

sll1.add_to_end("Fri") # wrong
print(sll1)
print("")

sll1.add_in_between(sll1.head.next.next.next,"Thu")
print(sll1)
print("")

sll1.add_multiple(["Sat", "Sun"])
print(sll1)
print("")

# generate linked list
sll2 = SinglyLinkedList()
sll2.generate(10, 0, 1)
print(sll2)
print("")

# pop the first element
sll2.pop_head()
print(sll2)
print("")

# remove the node at the specified index
sll2.remove_at(1)
print(sll2)
print("")
