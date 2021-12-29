#------------------------------------------------------Question------------------------------------------------------#

# Describe how you could use a single array to implement three stacks.

#--------------------------------------------------------Tips--------------------------------------------------------#

# 002 - A stack is simply a data structure in which the most recently added elements are
#       removed first. Can you simulate a single stack using an array? Remember that there are
#       many possible solutions, and there are tradeoffs of each.
# 012 - We could simulate three stacks in an array by just allocating the first third of the array to
#       the first stack, the second third to the second stack, and the final third to the third stack.
#       One might actually be much bigger than the others, though. Can we be more flexible
#       with the divisions?
# 038 - If you want to allow for flexible divisions, you can shift stacks around. Can you ensure
#       that all available capacity is used?
# 058 - Try thinking about the array as circular, such that the end of the array "wraps around"to
#       the start of the array.

#------------------------------------------------------Solution------------------------------------------------------#

# Like many problems, this one somewhat depends on how well we'd like to support these stacks. If we're
# okay with simply allocating a fixed amount of space for each stack, we can do that. This may mean though
# that one stack runs out of space, while the others are nearly empty.

# We can divide the array in three equal parts and allow the individual stack to grow in that limited space.
# Note: We will use the notation "[" to mean inclusive of an end point and "(" to mean exclusive of an end
# point.
 
#   For stack 1, we will use [ 0, n/3)
#   For stack 2, we will use [ n/3, 2n/3)
#   For stack 3, we will use [ 2n/3, n)

class MultiStack:

    def __init__(self, stackCapacity):
        self.numberOfStacks = 3
        self.stackCapacity = stackCapacity # the amount of elements in each stack
        self.values = [0] * (stackCapacity * self.numberOfStacks)
        self.sizes = [0] * self.numberOfStacks # the number of elements in each stack

    # Add an item to the top of the stack.
    def Push(self, item, stackNum):
        if self.IsFull(stackNum):
            raise Exception('Stack is full')
        self.sizes[stackNum] += 1
        topIndex = self.IndexOfTop(stackNum)
        self.values[topIndex] = item

    # Remove the top item from the stack.
    def Pop(self, stackNum):
        if self.IsEmpty(stackNum):
            raise Exception('Stack is empty')
        topIndex = self.IndexOfTop(stackNum)
        value = self.values[topIndex] # Get the value at the top of the stack
        self.values[topIndex] = 0 # Clear
        self.sizes[stackNum] -= 1 # Shrink
        return value

    # Return the top of the stack.
    def Peek(self, stackNum): 
        if self.IsEmpty(stackNum):
            raise Exception('Stack is empty')
        topIndex = self.IndexOfTop(stackNum)
        return self.values[topIndex]

    # Return true if and only if the stack is empty.
    def IsEmpty(self, stackNum):
        return self.sizes[stackNum] == 0

    # Return true if and only if the stack is full.
    def IsFull(self, stackNum):
        return self.sizes[stackNum] == self.stackCapacity

    # Returns index of the top of the stack specified.
    # Where the top of the stack is shifted by one each time a value is "pushed"
    def IndexOfTop(self, stackNum):
        offset = stackNum * self.stackCapacity
        return offset + self.sizes[stackNum] - 1

def ThreeInOne():
    newstack = MultiStack(2)
    print(newstack.IsEmpty(1))
    newstack.Push(3, 1)
    print(newstack.Peek(1))
    print(newstack.IsEmpty(1))
    newstack.Push(2,1)
    print(newstack.Peek(1))
    print(newstack.Pop(1))
    print(newstack.Peek(1))
    newstack.Push(3, 1)

ThreeInOne()

# If we had additional information about the expected usages of the stacks, then we could modify this algo­
# rithm accordingly. For example, if we expected Stack 1 to have many more elements than Stack 2, we could
# allocate more space to Stack 1 and less space to Stack 2.

#-------------------------------------------------------Followup-----------------------------------------------------#

# Alternatively, we can be flexible in our space allocation, but this significantly increases the complexity of
# the problem.
