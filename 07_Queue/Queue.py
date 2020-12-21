class Queue:
    """ Class Holding operations on QUEUE """

    def __init__(self, QLength):
        self.QLength = QLength
        self.front = self.rear = 0
        self.size = 0
        self.queue = [None] * QLength

    def printQueue(self):
        """ Prints the Queue """
        for ele in range(self.front, self.rear):
            print(self.queue[ele], end='|')
        print("||END")

    def QisFull(self):
        """ Check if QUEUE is Full """
        return self.rear == self.QLength

    def QisEmpty(self):
        """ Check if QUEUE is Empty """
        return self.size == 0 or self.front and self.rear == 0

    def enqueue(self, data):
        """ Insert new Element to Queue """
        if self.QisFull():
            print("Queue is Full, Can't Enqueue")
            return False
        else:
            self.queue[self.rear] = data
            self.rear += 1
            self.size += 1
            print("{0} - Enqueued".format(data))
            return True

    def dequeue(self):
        """ Remove Element from the QUEUE """
        if self.QisEmpty():
            print("Queue is Empty, Can't Dequeue")
            return False
        else:
            element = self.queue[self.front]
            if self.front >= self.rear:
                self.front = self.rear = 0
            else:
                self.front += 1
                self.size -= 1
            print("Dequeued element is - {0}".format(element))
            return True


if __name__ == '__main__':
    q = Queue(5)
    q.enqueue(3)
    q.enqueue(15)
    q.enqueue(4)
    q.printQueue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(1)
    q.enqueue(2)
    q.printQueue()
    q.dequeue()
    q.printQueue()
    print("Size of QUEUE is : ", q.size)
