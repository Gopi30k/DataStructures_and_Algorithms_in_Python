class Node:
    """Node Class holiding data and pointer to next Node"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    """ Stack Class holding Operations on Stack """

    def __init__(self):
        self.root = None
        self.size = 0

    def isEmpty(self):
        """ Check if stack is empty or not """
        return True if self.root is None else False

    def printStack(self):
        """ Prints whole stack """
        temp = self.root
        while temp != None:
            print('|{}|'.format(temp.data))
            temp = temp.next

    def push(self, data):
        """ Push to stack """
        newElement = Node(data)
        newElement.next = self.root
        self.root = newElement
        return True

    def pop(self):
        """Pop from Stack """
        if self.isEmpty():
            return None
        temp = self.root
        self.root = temp.next
        return temp.data

    def peek(self):
        """ View Top Element of Stack """
        if self.isEmpty():
            return None
        return self.root.data


if __name__ == '__main__':
    stack = Stack()
    stack.push(5)
    stack.push(44)
    stack.push(88)
    stack.printStack()
    print('Popped Element is -> {0}'.format(stack.pop()))
    stack.printStack()
    print('Element at Top(peeking) -> {0}'.format(stack.peek()))
