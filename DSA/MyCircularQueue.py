class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k
        self.queue = [None for i in range(k)]
        self.front = self.rear = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if (self.rear + 1) % self.size == self.front:
            print(" Queue is Full\n")
        elif self.front == -1:
            self.front == 0
            self.rear == 0
            self.queue(self.rear) == value
        else:
            self.rear = self.rear + 1
            self.queue(self.rear) == value

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.rear == -1:
            print(" Queue is Empty\n")
        elif (self.front == self.rear):  
            temp = self.queue[self.front] 
            self.front = -1
            self.rear = -1
            return temp 
        else: 
            temp = self.queue[self.front] 
            self.front = (self.front + 1) % self.size 
            return temp 

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(k)
param_1 = obj.enQueue(value)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()