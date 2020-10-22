# Author : Gopi Krishnan
# Singly Linked List

class Node:
    """Node Class holiding data and pointer to next Node"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    """ SinglyLinkedList Class holding Operations on Linked List """

    def __init__(self):
        """ Head and length Props for every linked list """
        self.head = None
        self.length = 0

    def printList(self):  # O(n)
        """ Prints the Whole List """
        temp = self.head
        while temp != None:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('|END')

    def insertAtEnd(self, data):  # O(1)
        """ Insert NewNode at End of List """
        newNode = Node(data)
        temp = self.head
        if temp == None:
            self.head = newNode
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
        self.length += 1
        return True

    def insertAtBeg(self, data):  # O(1)
        """ Insert NewNode at Beginning of List """
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length = self.length+1
        return True

    def insertAtPos(self, index, data):  # O(1)
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
        self.length += 1
        return True

    def getNodeAtIndex(self, index):  # O(n)
        """ Get Node Object at specific index provided """
        if index < 0 or index >= self.length:
            return None
        cnt = 0
        temp = self.head
        while cnt != index:
            temp = temp.next
            cnt = cnt+1
        return temp

    def getValAtIndex(self, index):  # O(n)
        """ Get Node Data at specific index provided """
        return self.getNodeAtIndex(index).data if index < self.length else None

    def deleteByValue(self, data):  # O(n)
        """ Delete Node by the data provided """
        temp = self.head
        if temp == None:
            return False
        elif temp.data == data:
            self.head = temp.next
            self.length -= 1
            return True
        else:
            prev = None
            while temp.data != data and temp.next != None:
                prev = temp
                temp = temp.next
            prev.next = temp.next
            self.length -= 1
            return True

    def deleteAtIndex(self, index):  # O(n)
        """ Delete Node by index Provided """
        valueAtIndex = self.getValAtIndex(index)
        if valueAtIndex is not None:
            return self.deleteByValue(valueAtIndex)
        else:
            return False

    def getIndexOfValue(self, data):  # O(n)
        """ Get Index of data provided in LL """
        index = 0
        temp = self.head
        while temp.next != None and data != temp.data:
            index += 1
            temp = temp.next
        if index == self.length-1 and data != temp.data:
            return -1
        return index


if __name__ == '__main__':
    sList = SinglyLinkedList()
    print("##### Inserting at End 4,5,6 ######")
    sList.insertAtEnd(4)
    sList.insertAtEnd(5)
    sList.insertAtEnd(6)
    sList.printList()
    print("##### Inserting at Beginning 60,9 #####")
    sList.insertAtBeg(60)
    sList.insertAtBeg(9)
    sList.printList()
    print("##### Get value at index 2 #####")
    print(sList.getValAtIndex(2))
    print("##### Inserting value 500 at Position3  #####")
    print(sList.insertAtPos(3, 500))
    sList.printList()
    print("##### Deleting value 4 in List #####")
    print(sList.deleteByValue(4))
    sList.printList()
    print("##### Inserting at Beginning 43 #####")
    sList.insertAtBeg(43)
    sList.printList()
    print("##### Get Value at Index 5 #####")
    print(sList.getIndexOfValue(5))
    sList.printList()
    print("##### Delete Value at Index 2 #####")
    print(sList.deleteAtIndex(2))
    sList.printList()
    print("##### Length of List #####")
    print(sList.length)
