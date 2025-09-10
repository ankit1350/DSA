class student:
    def __init__(self,name,rollNo,marks):
        self.name=name
        self.rollNo=rollNo
        self.marks=marks
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def addData(self,name,rollNo,marks):
       student1=student(name,rollNo,marks)
       if self.head is None:
            self.head=student1
       else:
            current = self.head
            while current.next:
                current = current.next
            current.next =student1

    def deleteData(self, rollNo):
        current = self.head
        prev = None
        if current and current.rollNo == rollNo:
            self.head = current.next
            print(f"Student with Roll No {rollNo} deleted.")
            return

        while current and current.rollNo != rollNo:
            prev = current
            current = current.next

        if current:
            prev.next = current.next
            print(f"Student with Roll No {rollNo} deleted.")
        else:
            print(f"Student with Roll No {rollNo} not found.")


    def searchData(self, rollNo):
        current = self.head
        while current:
            if current.rollNo == rollNo:
                print(f"Found student: name:{current.name}, rollNO:{current.rollNo}, marks={current.marks}")
                return
            current = current.next
        print(f"Student with Roll No {rollNo} not found.")

    def updateData(self, rollNo, new_name=None, new_marks=None):
        current = self.head
        while current:
            if current.rollNo == rollNo:
                if new_name is not None:
                    current.name = new_name
                if new_marks is not None:
                    current.marks = new_marks
                print(f"Student with Roll No {rollNo} updated.")
                return
            current = current.next
        print(f"Student with Roll No {rollNo} not found.")


    def displayData(self):
        current=self.head
        if not current:
          print("No student record")

        while current:
            print(f"name:{current.name}, rollNO:{current.rollNo}, marks={current.marks}")
            current=current.next

    def sortData(self, key, order='ascending'):
        if not self.head or not self.head.next:
            print("Not enough data to sort.")
            return

        students = []
        current = self.head
        while current:
            students.append(current)
            current = current.next

        
        reverse = (order == 'descending')
        if key in ['rollNo', 'marks']:
            students.sort(key=lambda s: getattr(s, key), reverse=reverse)
        else:
            print("Invalid key for sorting. Please use 'rollNo' or 'marks'.")
            return

        
        self.head = students[0]
        current = self.head
        for s in students[1:]:
            current.next = s
            current = current.next
        current.next = None

        print(f"Data sorted by {key} in {order} order.")
        print(students)




def menu():
    ll=LinkedList()
    while True:

        print("1.add data of the student.")
        print("2.show data")
        print("3.delete data")
        print("4.search data")
        print("5.update data")
        print("6.sort data")
        print("7.exit")
        choose=int(input())

        if choose == 1:
            r = int(input("Enter Roll No: "))
            n = input("Enter Name: ")
            m = float(input("Enter Marks: "))
            ll.addData(n,r,m)
        elif choose == 2:
            ll.displayData()
        elif choose == 3:
            r = int(input("Enter Roll No of student to delete: "))
            ll.deleteData(r)
        elif choose == 4:
            r = int(input("Enter Roll No of student to search: "))
            ll.searchData(r)
        elif choose == 5:
            r = int(input("Enter Roll No of student to update: "))
            n = input("Enter new Name (leave blank to keep current): ")
            m = input("Enter new Marks (leave blank to keep current): ")
            new_name = n if n else None
            new_marks = float(m) if m else None
            ll.updateData(r, new_name, new_marks)
        elif choose == 6:
            skey = input("Enter key to sort by (rollNo or marks): ")
            sorder = input("Enter sort order (ascending or descending): ")
            ll.sortData(skey, sorder)
        elif choose == 7:
            break
        else:
            print("Invalid choice. Please try again.")

menu()