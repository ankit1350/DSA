
class LibraryManager:
    def __init__(self):
        # members: dict of member_name -> borrow_count
        # books: dict of book_title -> borrow_count
        self.members = {}
        self.books = {}

    def addMember(self, name):
        if name in self.members:
            print("Member already exists.")
            return
        self.members[name] = 0
        print(f"Added member: {name}")

    def addBook(self, title):
        if title in self.books:
            print("Book already exists.")
            return
        self.books[title] = 0
        print(f"Added book: {title}")

    def recordBorrowing(self, memberName, bookTitle, count=1):
        # record that memberName borrowed bookTitle 'count' times (increment)
        if memberName not in self.members:
            print("Member not found. Use option to add member first.")
            return
        if bookTitle not in self.books:
            print("Book not found. Use option to add book first.")
            return
        if count <= 0:
            print("Invalid borrow count. Must be positive.")
            return
        self.members[memberName] += count
        self.books[bookTitle] += count
        print(f"Recorded: {memberName} borrowed '{bookTitle}' x{count}")

    def computeAverage(self):
        # Average number of books borrowed by all members
        if not self.members:
            print("No members in the system.")
            print("Time: O(1), Space: O(1)")
            return
        total = 0
        for v in self.members.values():
            total += v
        avg = total / len(self.members)
        print(f"Average books borrowed per member: {avg:.2f}")
        print("Time: O(m) where m = number of members, Space: O(1)")

    def findHighestLowestBook(self):
        # Find book(s) with highest and lowest borrow counts
        if not self.books:
            print("No books in the system.")
            print("Time: O(1), Space: O(1)")
            return
        # Find max and min counts
        counts = self.books.values()
        maxCount = max(counts)
        minCount = min(counts)
        maxBooks = [t for t, c in self.books.items() if c == maxCount]
        minBooks = [t for t, c in self.books.items() if c == minCount]
        print(f"Highest borrow count: {maxCount} -> {maxBooks}")
        print(f"Lowest borrow count: {minCount} -> {minBooks}")
        print("Time: O(b) where b = number of books, Space: O(1) extra (output lists sized by ties)")

    def countZeroBorrowMembers(self):
        # Count members with borrow count == 0
        if not self.members:
            print("No members in the system.")
            print("Time: O(1), Space: O(1)")
            return
        cnt = 0
        for v in self.members.values():
            if v == 0:
                cnt += 1
        print(f"Members who have not borrowed any books: {cnt}")
        print("Time: O(m) where m = number of members, Space: O(1)")

    def findMostFrequentBorrowedBook(self):
        # Two interpretations:
        # 1) Book(s) with highest borrow count (most borrowed)
        # 2) Mode of borrow counts across books (borrow-count value that occurs most) and books having that mode
        if not self.books:
            print("No books in the system.")
            print("Time: O(1), Space: O(1)")
            return
        # 1) Most borrowed book(s)
        counts = self.books.values()
        maxCount = max(counts)
        mostBorrowedBooks = [t for t, c in self.books.items() if c == maxCount]
        print(f"Most borrowed book(s) with highest count {maxCount}: {mostBorrowedBooks}")

        # 2) Mode of borrow counts
        freq = {}
        for c in self.books.values():
            freq[c] = freq.get(c, 0) + 1
        # find mode frequency
        modeFreq = max(freq.values())
        modes = [count for count, f in freq.items() if f == modeFreq]
        # books that have a borrow count equal to any mode value
        booksWithModeCounts = [t for t, c in self.books.items() if c in modes]
        print(f"Mode(s) of borrow counts: {modes} (appears {modeFreq} times). Books with mode counts: {booksWithModeCounts}")
        print("Time: O(b) where b = number of books, Space: O(k) where k = distinct borrow counts (<= b)")

    def displayRecords(self):
        print("\nMembers (name -> borrow_count):")
        if not self.members:
            print("  [No members]")
        else:
            for n, c in self.members.items():
                print(f"  {n} -> {c}")
        print("\nBooks (title -> borrow_count):")
        if not self.books:
            print("  [No books]")
        else:
            for t, c in self.books.items():
                print(f"  '{t}' -> {c}")
        print()

    

    def menu(self):
        while True:
            print("\nLibrary Manager Menu:")
            print("1. Add member")
            print("2. Add book")
            print("3. Record borrowing")
            print("4. Compute average books borrowed by members")
            print("5. Find book(s) with highest and lowest borrowings")
            print("6. Count members with zero borrows")
            print("7. Display most frequently borrowed book (and mode of counts)")
            print("8. Display all records")
            print("9. Load sample data")
            print("0. Exit")
            choice = input("Enter choice: ").strip()
            if choice == "1":
                name = input("Member name: ").strip()
                if name:
                    self.addMember(name)
                else:
                    print("Invalid name.")
            elif choice == "2":
                title = input("Book title: ").strip()
                if title:
                    self.addBook(title)
                else:
                    print("Invalid title.")
            elif choice == "3":
                member = input("Member name: ").strip()
                book = input("Book title: ").strip()
                try:
                    cnt = int(input("Borrow count (default 1): ").strip() or "1")
                except ValueError:
                    print("Invalid count.")
                    continue
                self.recordBorrowing(member, book, cnt)
            elif choice == "4":
                self.computeAverage()
            elif choice == "5":
                self.findHighestLowestBook()
            elif choice == "6":
                self.countZeroBorrowMembers()
            elif choice == "7":
                self.findMostFrequentBorrowedBook()
            elif choice == "8":
                self.displayRecords()
            elif choice == "9":
                self.loadSampleData()
            elif choice == "0":
                print("Exiting.")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    manager = LibraryManager()
    manager.menu()