#------------------------------------------------------Question------------------------------------------------------#

# Write code to remove duplicates from an unsorted linked list.

#--------------------------------------------------------Tips--------------------------------------------------------#

# 009 - Try hash table
# 040 - Without extra space, you'll need O(N^2) time. Try using two pointers, where the second one searches ahead 
#       of the first one.

#------------------------------------------------------Solution------------------------------------------------------#

# In order to remove duplicates from a linked list, we need to be able to track duplicates. A simple hash table
# will work well here.

from LinkedList import LinkedList # see the LinkedList.py file for more details on the Data Structure

# In the below solution, we simply iterate through the linked list, adding each element to a hash table. When
# we discover a duplicate element, we remove the element and continue iterating. We can do this all in one
# pass since we are using a linked list.

ll = LinkedList()
ll.generate(100, 0, 9)
print(ll)

def remove_dups(ll):
    if ll.head is None:
        return

    current = ll.head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

# The above solution takes O(N) time, where N is the number of elements in the linked list.

remove_dups(ll)
print(ll)

#-------------------------------------------------------Followup-----------------------------------------------------#

# How would you solve this problem if a temporary buffer is not allowed?

# lf we don't have a buffer, we can iterate with two pointers: current which iterates through the linked list,
# and runner which checks all subsequent nodes for duplicates.

ll.generate(100, 0, 9)
print(ll)

def remove_dups_followup(ll):
    if ll.head is None:
        return

    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    
    return ll.head

# This code runs in O (1) space, but O (N^2) time.

remove_dups_followup(ll)
print(ll)
