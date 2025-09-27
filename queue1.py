class Queue(object):
    def __init__(self, limit=5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size <= 0
    
    def enQueue(self, item):
        if self.size >= self.limit:
            print("Queue Overflow")
            return 
        self.que.append(item)
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1
        print("Queue after enQueue:", self.que)
    
    def deQueue(self):
        if self.size <= 0:
            print("Queue Underflow")
            return
        self.que.pop(0)
        self.size -= 1
        if self.size == 0:
            self.front = self.rear = None
        else:
            self.rear = self.size - 1
        print("Queue after deQueue:", self.que)

    def queueRear(self):
        if self.rear is None:
            print("Sorry, the queue is empty")
            raise IndexError
        return self.que[self.rear]
    
    def queueFront(self):
        if self.front is None:
            print("Sorry, the queue is empty")
            raise IndexError
        return self.que[self.front]
    
    def getSize(self):
        return self.size


q = Queue()

def menu():
    while True:
        print("\nEnter your choice:")
        print("1. Add element to the queue")
        print("2. Delete an element from the queue")
        print("3. Check if the queue is empty")
        print("4. Get rear element")
        print("5. Get the front element")
        print("6. Exit")

        choice = int(input("Choice: "))
        
        if choice == 1:
            a = int(input("Enter the element you want to push: "))
            q.enQueue(a)
        elif choice == 2:
            q.deQueue()
        elif choice == 3:
            print("Is queue empty? ->", q.isEmpty())
        elif choice == 4:
            try:
                print("Rear element:", q.queueRear())
            except IndexError:
                pass
        elif choice == 5:
            try:
                print("Front element:", q.queueFront())
            except IndexError:
                pass
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

menu()

    
         