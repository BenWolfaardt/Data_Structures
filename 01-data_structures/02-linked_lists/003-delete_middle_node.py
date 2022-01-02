#------------------------------------------------------Question------------------------------------------------------#

# Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily 
# the exact middle) of a singly linked list, given only access to that node.

#-------------------------------------------------------Example------------------------------------------------------#

# Input: the node c from the linked lista->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f

#--------------------------------------------------------Tips--------------------------------------------------------#

# 072 - Picture the list 1->5->9->12. Removing 9 would make it look like 1->5->12. You only have access to the 9 node. 
# Can you make it look like the correct answer?

#------------------------------------------------------Solution------------------------------------------------------#

# In this problem, you are not given access to the head of the linked list. You only have access to that node.
# The solution is simply to copy the data from the next node over to the current node, and then to delete the
# next node.

from LinkedList import LinkedList


def deleteMiddleNode(node):
    node.value = node.next.value
    node.next = node.next.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_multiple([1, 2, 3, 4])
    middleNode = ll.add(5)
    ll.add_multiple([7, 8, 9])

    print(ll)
    deleteMiddleNode(middleNode)
    print(ll)

#--------------------------------------------------------Tests-------------------------------------------------------#

