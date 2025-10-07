class TextEditor:
    def __init__(self):
        self.doc = ""
        self.undo_stack = []
        self.redo_stack = []

    def make_change(self, change):
        self.undo_stack.append(self.doc)
        self.doc += change
        self.redo_stack.clear()
        print("Change made.")
        self.display()

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        self.redo_stack.append(self.doc)
        self.doc = self.undo_stack.pop()
        print("Undo performed.")
        self.display()

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        self.undo_stack.append(self.doc)
        self.doc = self.redo_stack.pop()
        print("Redo performed.")
        self.display()

    def display(self):
        print("Current state:")
        print(f"{self.doc}")


# Main menu loop
editor = TextEditor()

while True:
    print("\nMenu")
    print("1. Make a change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display document")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        text = input("Enter text to add: ")
        editor.make_change(text)
    elif choice == 2:
        editor.undo()
    elif choice == 3:
        editor.redo()
    elif choice == 4:
        editor.display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
