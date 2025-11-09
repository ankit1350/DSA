class TextEditor:
    def __init__(self):
        self.document = ""          # Current document content
        self.undo_stack = []        # Stack to store previous states
        self.redo_stack = []        # Stack to store undone states

    # ✅ Make a new change in the document
    def make_change(self, new_text):
        self.undo_stack.append(self.document)  # Save current state before change
        self.document = new_text               # Apply new change
        self.redo_stack.clear()                # Redo is not valid after new change
        print("Change applied!")

    # ✅ Undo the most recent change
    def undo(self):
        if not self.undo_stack:
            print("No action to Undo!")
            return
        self.redo_stack.append(self.document)   # Move current state to redo stack
        self.document = self.undo_stack.pop()   # Revert to previous state
        print("Undo successful!")

    # ✅ Redo the most recently undone action
    def redo(self):
        if not self.redo_stack:
            print("No action to Redo!")
            return
        self.undo_stack.append(self.document)   # Save current state for undo later
        self.document = self.redo_stack.pop()   # Restore undone state
        print("Redo successful!")

    # ✅ Display current document text
    def display_document(self):
        print("\nCurrent Document State:")
        print(self.document if self.document != "" else "[Empty Document]")


# ✅ Main Menu-driven program
editor = TextEditor()

while True:
    print("\n---- TEXT EDITOR ----")
    print("1. Make a Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_text = input("Enter new document text: ")
        editor.make_change(new_text)
    elif choice == "2":
        editor.undo()
    elif choice == "3":
        editor.redo()
    elif choice == "4":
        editor.display_document()
    elif choice == "5":
        print("Exiting the editor!")
        break
    else:
        print("Invalid choice! Try again.")
