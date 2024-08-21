class QueueUsingStacks:
    def __init__(self, capacity):
        self.stack1 = []
        self.stack2 = []
        self.capacity = capacity
        self.size = 0

    def enqueue(self, data):
        if self.size == self.capacity:
            print("Queue is full")
            return

        self.stack1.append(data)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty")
            return

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        self.stack2.pop()
        self.size -= 1

    def display(self):
        if self.size == 0:
            print("Queue is empty")
            return

        for i in range(len(self.stack2) - 1, -1, -1):
            print(self.stack2[i], end=" <-- ")

        for i in range(len(self.stack1)):
            print(self.stack1[i], end=" <-- ")

        print()

    def front_element(self):
        if self.size == 0:
            print("Queue is empty")
            return
        
        if self.stack2:
            print("Front element is:", self.stack2[-1])
        else:
            print("Front element is:", self.stack1[0])

if __name__ == "__main__":
    q = QueueUsingStacks(5)

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    q.display()

    q.enqueue(40)
    q.enqueue(50)

    q.display()

    q.enqueue(60)

    q.dequeue()
    q.dequeue()

    print("After two node deletions")

    q.display()

    print("After one insertion")
    q.enqueue(60)

    q.display()

    q.front_element()
