# Author : Gopi Krishnan
# Doubly Linked List

class Node:
    """ Node Class holiding data and pointers to next Node & prev Node"""

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList():
    """ DoublyLinkedList Class holding Operations on Linked List """

    def __init__(self):
        """ Head and length Props for every linked list """

        self.head = None
        self.length = 0

    def printList(self):
        """ Prints the Whole List """

        temp = self.head
        while temp != None:
            # print('{0}<-{1}->{2}\t'.format(id(temp.prev),
            #  temp.data, id(temp.next)), end='')
            print('<- {} ->'.format(temp.data), end=' ')
            temp = temp.next
        print('|END')

    def getNodeAtIndex(self, index):
        """ Get Node Object at specific index provided """

        if index < 0 or index >= self.length:
            return None
        else:
            cnt = 0
            temp = self.head
            while temp != None and cnt != index:
                cnt += 1
                temp = temp.next
            return temp

    def getValueAtIndex(self, index):
        """ Get Node Data at specific index provided """

        if index < 0 or index >= self.length:
            return None
        else:
            return self.getNodeAtIndex(index).data

    def getIndexOfValue(self, data):
        """ Get Index of data provided in LL """

        index = 0
        temp = self.head
        while temp.next != None and data != temp.data:
            index += 1
            temp = temp.next
        if index == self.length-1 and data != temp.data:
            return -1
        return index

    def insertAtBeg(self, data):
        """ Insert NewNode at Beginning of List """
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1
        return True

    def insertAtEnd(self, data):
        """ Insert NewNode at End of List """

        newNode = Node(data)
        temp = self.head
        if temp == None:
            self.head = newNode
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
        self.length += 1
        return True

    def insertAtPos(self, index, data):
        """Inserting NewNode at specific Index Provided"""

        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.insertAtBeg(data)
        elif index == self.length:
            return self.insertAtEnd(data)
        newNode = Node(data)
        prevNode = self.getNodeAtIndex(index-1)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        self.length += 1
        return True

    def deleteByValue(self, data):
        """ Delete Node by the data provided """

        currentNode = self.head
        if currentNode == None:
            return None
        elif currentNode.data == data:
            currentNode.next.prev = None
            self.head = currentNode.next
            currentNode.next = None
            self.length -= 1
            return True
        else:
            prevNode = None
            while currentNode != None and currentNode.data != data:
                prevNode = currentNode
                currentNode = currentNode.next
            if prevNode and currentNode:  # If no such element to delete
                prevNode.next = currentNode.next
                if currentNode.next != None:  # Last node will not have Next Node's PREV
                    currentNode.next.prev = prevNode

                # Free up current Node's Pointers
                currentNode.next = None
                currentNode.prev = None
                self.length -= 1
                return True
            else:
                return None

    def deleteAtIndex(self, index):
        """ Delete Node by index Provided """

        if index < 0 or index > self.length:
            return None
        valueAtIndex = self.getValueAtIndex(index)
        if valueAtIndex is not None:
            self.deleteByValue(valueAtIndex)
        else:
            return False

# NA|56|E12 -> E11|76|E13 -> E13|45|NA
#    E11          E12          E13


if __name__ == '__main__':
    dList = DoublyLinkedList()
    print("##### Inserting at End 101 ######")
    dList.insertAtEnd(101)
    dList.printList()
    print("##### Inserting at Beginning 10,4,6 ######")
    dList.insertAtBeg(10)
    dList.insertAtBeg(4)
    dList.insertAtBeg(6)
    dList.printList()
    print("##### Inserting at End 34 ######")
    dList.insertAtEnd(34)
    dList.printList()
    print("##### Get Value at index 4 ######")
    print(dList.getValueAtIndex(4))
    print("##### Inserting value 1000 at position 3 ######")
    dList.insertAtPos(3, 1000)
    dList.printList()
    print("##### Deleting value 4 ######")
    dList.deleteByValue(4)
    dList.printList()
    print("##### Get Index of Value 34 ######")
    print(dList.getIndexOfValue(34))
