class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    # Add Student at End
    def addStudent(self, roll, name, marks):
        new_node = Node(roll, name, marks)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Display all
    def display(self):
        if not self.head:
            print("\n❌ No Student Records!")
            return
        temp = self.head
        print("\n📌 Student Records:")
        while temp:
            print(f"Roll: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
            temp = temp.next

    # Search by roll number
    def search(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print(f"\n✅ Found → Roll: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
                return
            temp = temp.next
        print("\n❌ Student Not Found")

    # Delete by roll number
    def delete(self, roll):
        if not self.head:
            print("\n⚠️ No records to delete")
            return
        if self.head.roll == roll:
            self.head = self.head.next
            print("\n✅ Record Deleted")
            return
        
        prev = self.head
        cur = self.head.next
        while cur:
            if cur.roll == roll:
                prev.next = cur.next
                print("\n✅ Record Deleted")
                return
            prev = cur
            cur = cur.next

        print("\n❌ Student Not Found")

    # Update student record
    def update(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print("\nEnter Updated Information:")
                temp.name = input("Name: ")
                temp.marks = float(input("Marks: "))
                print("\n✅ Record Updated")
                return
            temp = temp.next
        print("\n❌ Student Not Found")

    # Sorting by field (roll/marks) and order (asc/desc)
    def sort(self, key, reverse=False):
        if not self.head or not self.head.next:
            return
        
        # Bubble Sort on Linked List
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                if (not reverse and getattr(temp, key) > getattr(temp.next, key)) or \
                   (reverse and getattr(temp, key) < getattr(temp.next, key)):
                    temp.roll, temp.next.roll = temp.next.roll, temp.roll
                    temp.name, temp.next.name = temp.next.name, temp.name
                    temp.marks, temp.next.marks = temp.next.marks, temp.marks
                    swapped = True
                temp = temp.next


# ---------------- MENU DRIVEN PROGRAM ----------------
slist = StudentList()

while True:
    print("\n===== Student Record Management =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Sort by Roll (Asc)")
    print("7. Sort by Roll (Desc)")
    print("8. Sort by Marks (Asc)")
    print("9. Sort by Marks (Desc)")
    print("10. Exit")

    ch = input("Enter your choice: ")

    if ch == '1':
        roll = int(input("Roll No: "))
        name = input("Name: ")
        marks = float(input("Marks: "))
        slist.addStudent(roll, name, marks)

    elif ch == '2':
        slist.display()

    elif ch == '3':
        roll = int(input("Enter Roll No to Search: "))
        slist.search(roll)

    elif ch == '4':
        roll = int(input("Enter Roll No to Delete: "))
        slist.delete(roll)

    elif ch == '5':
        roll = int(input("Enter Roll No to Update: "))
        slist.update(roll)

    elif ch == '6':
        slist.sort("roll", reverse=False)
        print("\n✅ Sorted by Roll ASC")

    elif ch == '7':
        slist.sort("roll", reverse=True)
        print("\n✅ Sorted by Roll DESC")

    elif ch == '8':
        slist.sort("marks", reverse=False)
        print("\n✅ Sorted by Marks ASC")

    elif ch == '9':
        slist.sort("marks", reverse=True)
        print("\n✅ Sorted by Marks DESC")

    elif ch == '10':
        print("\n👋 Exiting System...")
        break

    else:
        print("\n⚠️ Invalid Choice! Try Again")