
class Stack:
    def __init__ (self,capacity=1):
        self.top=-1
        self.capacity=capacity
        self.A=[None]*capacity

    def push(self,data):
        if self.isFull():
            print("Trying to resize : Increase")
            self.capacity *= 2  # double the capacity
            newArray = [None] * self.capacity
            for i in range(self.top + 1):
                newArray[i] = self.A[i]
            self.A = newArray

        self.top += 1
        self.A[self.top] = data
        print(f"Pushed {data}")

    def pop(self):
        if self.top==-1:
            print("the stack is empty")
            return 
        temp=self.A[self.top]
        self.top=self.top-1
        if self.top<self.capacity//2:
            print("Trying to resize : Decrease")
            self.capacity=self.capacity//2
            newArray=[None]*self.capacity
            for i in range(self.top+1):
                newArray[i]=self.A[i]
            self.A=newArray
        return temp    
    def peek(self):
        if self.top==-1:
            print("Stack Underflow")
            return 
        print(f"Top element is {self.A[self.top]}")
        return self.A[self.top]
    def isEmpty(self):
        return self.top==-1
    
    def isFull(self):
        return self.capacity==self.top+1
    
def menu():
    stack=Stack()
    print("1.Push element to the stack.\n2.Pop topmost element from the stack.\n3.Peek the topmost element.\n4.Check if the stack is empty .\n5.Check if the stack is full.")
    
    while True:
        choose=int(input("enter your choice:"))
        if choose==1:
            data=int(input("enter the element you want to push:"))
            stack.push(data)
        elif choose==2:
            stack.pop()
        elif choose==3:
            stack.peek()
        elif choose==4:
            print(stack.isEmpty())
        elif choose==5:
            print(stack.isFull())
        else:
            break 
menu()
