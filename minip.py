class BookNode:
    def __init__(self, bookId, title, author):
        self.bookId = bookId
        self.title = title
        self.author = author
        self.next = None

class BookList:
    def __init__(self):
        self.head = None

    def addBook(self, bookId, title, author):
        newNode = BookNode(bookId, title, author)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
        print("Book added successfully.")

    def displayBooks(self):
        if self.head is None:
            print("No books in the system.")
            return
        temp = self.head
        print("\nBook List:")
        print(f"{'Book ID':<10} {'Title':<30} {'Author':<20}")
        while temp:
            print(f"{temp.bookId:<10} {temp.title:<30} {temp.author:<20}")
            temp = temp.next

    def searchBook(self, bookId):
        temp = self.head
        while temp:
            if temp.bookId == bookId:
                print("Book found:")
                print("ID:", temp.bookId)
                print("Title:", temp.title)
                print("Author:", temp.author)
                return
            temp = temp.next
        print("Book not found.")

    def deleteBook(self, bookId):
        temp = self.head
        prev = None
        while temp:
            if temp.bookId == bookId:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                print("Book deleted successfully.")
                return
            prev = temp
            temp = temp.next
        print("Book not found.")

    def sortBooksById(self):
        if self.head is None or self.head.next is None:
            print("List is too short to sort.")
            return
        swapped = True
        while swapped:
            swapped = False
            prev = None
            curr = self.head
            while curr and curr.next:
                if curr.bookId > curr.next.bookId:
                    swapped = True
                    if prev is None:
                        nxt = curr.next
                        curr.next = nxt.next
                        nxt.next = curr
                        self.head = nxt
                        prev = nxt
                    else:
                        nxt = curr.next
                        curr.next = nxt.next
                        nxt.next = curr
                        prev.next = nxt
                        prev = nxt
                else:
                    prev = curr
                    curr = curr.next
        print("Books sorted by ID.")

    def sortBooksByTitle(self):
        if self.head is None or self.head.next is None:
            print("List is too short to sort.")
            return
        swapped = True
        while swapped:
            swapped = False
            prev = None
            curr = self.head
            while curr and curr.next:
                if curr.title.lower() > curr.next.title.lower():
                    swapped = True
                    if prev is None:
                        nxt = curr.next
                        curr.next = nxt.next
                        nxt.next = curr
                        self.head = nxt
                        prev = nxt
                    else:
                        nxt = curr.next
                        curr.next = nxt.next
                        nxt.next = curr
                        prev.next = nxt
                        prev = nxt
                else:
                    prev = curr
                    curr = curr.next
        print("Books sorted by Title.")

def menu():
    bookList = BookList()
    while True:
        print("\n--- Book Management System ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book by ID")
        print("4. Delete Book by ID")
        print("5. Sort Books by ID")
        print("6. Sort Books by Title")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            bookId = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            bookList.addBook(bookId, title, author)
        elif choice == 2:
            bookList.displayBooks()
        elif choice == 3:
            bookId = int(input("Enter Book ID to search: "))
            bookList.searchBook(bookId)
        elif choice == 4:
            bookId = int(input("Enter Book ID to delete: "))
            bookList.deleteBook(bookId)
        elif choice == 5:
            bookList.sortBooksById()
        elif choice == 6:
            bookList.sortBooksByTitle()
        elif choice == 7:
            print("Exiting Book Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()